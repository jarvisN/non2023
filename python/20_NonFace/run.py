from mtcnn.mtcnn import MTCNN
from keras_facenet import FaceNet
import cv2
import numpy as np

# สร้างตัวตรวจจับใบหน้าและโมเดล FaceNet
detector = MTCNN()
embedder = FaceNet()

# เปิดการใช้ webcam
video_capture = cv2.VideoCapture(0)

# โหลด embeddings และ labels ของใบหน้าที่คุณรู้จัก (คุณต้องสร้าง embeddings นี้ล่วงหน้า)
known_face_encodings = np.load('data/known_face_encodings.npy')
known_face_names = np.load('data/known_face_names.npy')

# Check if known_face_encodings is not empty
if known_face_encodings.size > 0:
    # Convert known_face_encodings to a 2D array if it's 1D
    if known_face_encodings.ndim == 1:
        known_face_encodings = np.vstack(known_face_encodings)
else:
    print("No known face encodings found.")

while True:
    # ดึงเฟรมภาพมาจากวีดีโอ
    ret, frame = video_capture.read()

    # ตรวจจับใบหน้าในภาพ
    faces = detector.detect_faces(frame)
    
    face_encodings = []
    for face in faces:
        x, y, width, height = face['box']
        cv2.rectangle(frame, (x, y), (x+width, y+height), (0,255,0), 2)
        
        # แยกใบหน้าจากภาพ
        face_img = frame[y:y+height, x:x+width]
        
        # สร้าง embedding ของใบหน้า
        face_encoding = embedder.extract(face_img, threshold=0.95)
        
        if face_encoding:
            face_encodings.append(face_encoding[0])

    # จดจำใบหน้า
    face_names = []
    for face_encoding in face_encodings:
        face_encoding = np.expand_dims(face_encoding, axis=0)
        # distances = np.linalg.norm(known_face_encodings - face_encoding, axis=1)
        distances = np.linalg.norm(known_face_encodings - face_encoding)
        best_match_index = np.argmin(distances)
        
        # if distances[best_match_index] < 0.6:
        if distances and 0 <= best_match_index < distances.size and distances[best_match_index] < 0.6:
            name = known_face_names[best_match_index]
        else:
            name = "Unknown"
        face_names.append(name)

    # แสดงชื่อบนภาพ
    for (face, name) in zip(faces, face_names):
        x, y, width, height = face['box']
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

    # แสดงเฟรมภาพผลลัพธ์
    cv2.imshow('Video', frame)

    # กด 'q' เพื่อปิด!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
