import socket
import json

# Define the server's IP address and port
# Replace with the IP address of the UDP server you want to communicate with
server_ip = "192.168.43.153"
server_port = 23456  # Replace with the port number the UDP server is listening on

while True:

    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Create a Python dictionary to represent your data
    data_dict = {"order": "vibrate", "level": 2, "duration": 1}

    # Convert the dictionary to a JSON string
    json_data = json.dumps(data_dict)

    # Send the JSON data to the server
    client_socket.sendto(json_data.encode(), (server_ip, server_port))
    # client_socket.sendto(23, (server_ip, server_port))

    # Close the socket when you're done sending data
    client_socket.close()
