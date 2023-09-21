import time

try:
    while True:
        print("test 1")
        time.sleep(1)
except KeyboardInterrupt:
    print("Program interrupted by user")
