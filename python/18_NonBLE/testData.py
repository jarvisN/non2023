import serial

ser = serial.Serial('/dev/tty.usbserial-0001', 115200)

while True:
    data = ser.readline().decode('utf-8').strip()
    # data = ser.readline()
    print(f"data : {data} , Type : {type(data)}")
