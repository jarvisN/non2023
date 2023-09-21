import socket

UDP_IP = "0.0.0.0"  # กำหนดให้ IP Address เป็น 0.0.0.0 เพื่อรับข้อมูลจาก IP ใดๆ
UDP_PORT = 12345   # กำหนด Port ที่ตรงกับ ESP32 ที่ส่งข้อมูล

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)  # รับข้อมูลแบบ UDP ขนาดไม่เกิน 1024 บายต์
    # print("Received message:", data.decode(), "from", addr)
    print(f"Test Type : {type(data.decode())} , data : {data.decode()}")
