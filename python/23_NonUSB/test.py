import serial

# กำหนดพอร์ตซีเรียลและอัตราการเชื่อมต่อ (baud rate)
serial_port = 'COM5'  # แก้ไขให้เป็นพอร์ต UART ของคุณ (เช่น '/dev/ttyUSB0' บน Linux)
baud_rate = 921600  # แก้ไขให้ตรงกับอัตราการเชื่อมต่อของอุปกรณ์ของคุณ

try:
    # เปิดการเชื่อมต่อพอร์ตซีเรียล
    ser = serial.Serial(serial_port, baud_rate, timeout=1)

    # ตรวจสอบว่าการเชื่อมต่อพอร์ตซีเรียลเปิดอยู่หรือไม่
    if ser.is_open:
        print(f"เชื่อมต่อกับ {serial_port} ที่อัตราการเชื่อมต่อ {baud_rate} baud")

        while True:
            # อ่านข้อมูลจากอุปกรณ์ UART (รอการรับข้อมูล)
            data = ser.readline().decode('utf-8').strip()
            if data:
                print(f"ได้รับ: {data}")

            # ส่งข้อมูลไปยังอุปกรณ์ UART
            message = input("ป้อนข้อความเพื่อส่ง (หรือกด Enter เพื่อออก): ")
            if message:
                ser.write(message.encode('utf-8') + b'\n')

except serial.SerialException as e:
    print(f"ข้อผิดพลาดในการเชื่อมต่อพอร์ตซีเรียล: {e}")

finally:
    if ser.is_open:
        ser.close()
        print("ปิดการเชื่อมต่อพอร์ตซีเรียล")
