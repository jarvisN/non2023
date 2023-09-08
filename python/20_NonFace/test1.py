import face_recognition
import cv2

def main():
    # ขั้นตอนที่ 3: โหลดและตรวจจับใบหน้า
    # โหลดภาพ
    image_path = "non.jpg"
    image = face_recognition.load_image_file(image_path)

    # ตรวจจับใบหน้า
    face_locations = face_recognition.face_locations(image)

    # ขั้นตอนที่ 4: แสดงผล
    # โหลดภาพด้วย OpenCV
    image_cv2 = cv2.imread(image_path)

    # วาดสี่เหลี่ยมรอบใบหน้าที่ตรวจจับได้
    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(image_cv2, (left, top), (right, bottom), (0, 255, 0), 2)

    # แสดงผลภาพ
    cv2.imshow("Face Recognition", image_cv2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
