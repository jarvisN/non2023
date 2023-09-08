import cv2

def capture_image():
    # เริ่มต้น webcam
    cap = cv2.VideoCapture(0)

    while True:
        # อ่านภาพจาก webcam
        ret, frame = cap.read()

        # แสดงภาพที่ได้จาก webcam
        cv2.imshow('Webcam', frame)

        # ตรวจสอบว่ามีการกดปุ่ม 'q' หรือไม่เพื่อออกจากลูปและถ่ายรูป
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # บันทึกรูปภาพลงในไฟล์
            cv2.imwrite('images/webcam_photo.jpg', frame)
            break

    # ปิด webcam และปิดหน้าต่างทั้งหมด
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_image()
