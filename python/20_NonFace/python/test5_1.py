import cv2
import numpy as np
from tensorflow.keras.models import load_model

# โมเดลตรวจจับใบหน้า
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# โมเดลระบบจดจำใบหน้า
model = load_model('path_to_your_face_recognition_model.h5')

# อินเรียตกล้องเว็บแคม
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # ค้นหาใบหน้าในกรอบของภาพ
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # คัดลอกใบหน้าจากกรอบ
        face = frame[y:y+h, x:x+w]

        # ปรับขนาดใบหน้าเป็น 160x160 (ต้องปรับขนาดตามโมเดล)
        face = cv2.resize(face, (160, 160))
        face = np.expand_dims(face, axis=0)

        # ทำนายใบหน้าใช้โมเดล
        predictions = model.predict(face)

        # กำหนดข้อความที่จะแสดงบนเฟรม
        if predictions[0][0] > 0.5:
            label = "Face Detected"
        else:
            label = "No Face Detected"

        # วาดกรอบและข้อความบนเฟรม
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
