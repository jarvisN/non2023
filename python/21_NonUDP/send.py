import socket

# กำหนด IP address และ port สำหรับการรับข้อมูล
server_ip = "0.0.0.0"  # ใช้ IP address 0.0.0.0 เพื่อให้รับข้อมูลจากทุก IP address
server_port = 12345   # ใช้พอร์ต 12345 หรือใช้พอร์ตที่คุณต้องการ

# สร้าง UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# กำหนด IP address และ port ของ server
server_address = (server_ip, server_port)
server_socket.bind(server_address)

print(f"Listening on {server_ip}:{server_port}")

while True:
    # รับข้อมูล
    data, client_address = server_socket.recvfrom(1024)  # รับข้อมูลขนาดไม่เกิน 1024 bytes

    # แสดงข้อมูลที่รับมา
    print(f"Received data from {client_address}: {data.decode()}")

    # ตอบกลับหา client (หากต้องการ)
    response_message = "Hello, ESP32!"
    # server_socket.sendto(response_message.encode(), client_address)
    server_socket.sendto(response_message.encode(), client_address)

