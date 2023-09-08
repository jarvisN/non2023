import serial
import re

ser = serial.Serial('/dev/tty.usbserial-0001', 115200)

# Regular expression to find all numbers in a string
number_pattern = re.compile(r'\d+')

# Open the file for writing (append mode)
with open('data_log.txt', 'a') as file:
    while True:
        data = ser.readline().decode('utf-8').strip()
        print(f"data : {data} , Type : {type(data)}")
        
        # Extract all numbers from the received data
        numbers = number_pattern.findall(data)
        
        # Write the numbers to the file, separated by commas
        if numbers:
            file.write(','.join(numbers) + '\n')
