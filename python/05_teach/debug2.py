import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5) # set timeout to 5 seconds
try:
    client_socket.connect(('localhost', 8888))
    message = "Hello from client!"
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print(f"Received message: {response}")
except socket.timeout:
    print("Timeout error occurred.")
except ConnectionRefusedError:
    print("Server refused connection.")
finally:
    client_socket.close()
