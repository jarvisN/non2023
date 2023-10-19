from keras_facenet import FaceNet
from mtcnn.mtcnn import MTCNN
import cv2
import numpy as np
import os
import shutil

# สร้างตัวตรวจจับใบหน้าและโมเดล FaceNet
detector = MTCNN()
embedder = FaceNet()

# โฟลเดอร์ที่มีภาพของคนที่คุณรู้จัก
known_people_folder = 'images'

known_face_encodings = []
known_face_names = []

# วนลูปผ่านภาพทั้งหมดในโฟลเดอร์
for filename in os.listdir(known_people_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        filepath = os.path.join(known_people_folder, filename)
        
        # โหลดภาพและตรวจจับใบหน้า
        image = cv2.imread(filepath)
        faces = detector.detect_faces(image)
        
        if faces:
            # แยกใบหน้าแรก (ถ้ามีหลายใบหน้า, คุณควรใช้ภาพที่มีใบหน้าเดียว)
            x, y, width, height = faces[0]['box']
            face_img = image[y:y+height, x:x+width]
            
            # สร้าง embedding ของใบหน้า
            face_encoding = embedder.extract(face_img, threshold=0.95)
            
            if face_encoding:
                known_face_encodings.append(face_encoding[0])
                known_face_names.append(filename.split('.')[0])  # ใช้ชื่อไฟล์เป็น label

# บันทึก embeddings และ labels ลงไฟล์
np.save('known_face_encodings.npy', known_face_encodings)
np.save('known_face_names.npy', known_face_names)

# บันทึกเส้นทางไปยังไฟล์ known_face_encodings.npy และ known_face_names.npy
source_encodings_path = 'known_face_encodings.npy'
source_names_path = 'known_face_names.npy'

# เส้นทางไปยังโฟลเดอร์ที่คุณต้องการย้ายไป
destination_folder = 'data'

# ย้ายไฟล์ known_face_encodings.npy ไปยังโฟลเดอร์ 'data'
shutil.move(source_encodings_path, os.path.join(destination_folder, 'known_face_encodings.npy'))

# ย้ายไฟล์ known_face_names.npy ไปยังโฟลเดอร์ 'data'
shutil.move(source_names_path, os.path.join(destination_folder, 'known_face_names.npy'))