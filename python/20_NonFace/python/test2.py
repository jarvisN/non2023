import cv2
from mtcnn.mtcnn import MTCNN
import numpy as np

# สร้างตัวตรวจจับใบหน้า
detector = MTCNN()

# เปิดการใช้ webcam
video_capture = cv2.VideoCapture(0)

while True:
    # ดึงเฟรมภาพมาจากวีดีโอ
    ret, frame = video_capture.read()

    # ตรวจจับใบหน้าในภาพ
    faces = detector.detect_faces(frame)
    
    for face in faces:
        x, y, width, height = face['box']
        cv2.rectangle(frame, (x, y), (x+width, y+height), (0,255,0), 2)
        
        # คุณสามารถเพิ่มโค้ดเพื่อจดจำใบหน้าที่นี่

    # แสดงรูปภาพผลลัพธ์
    cv2.imshow('Video', frame)

    # กด 'q' เพื่อปิด!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
