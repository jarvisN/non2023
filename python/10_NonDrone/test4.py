from djitellopy import Tello
import cv2
from pyzbar.pyzbar import decode

tello = Tello()

tello.connect()
tello.streamon()

frame_read = tello.get_frame_read()

while True:
    # Get the latest frame
    img = frame_read.frame

    # Decode any QR codes in the frame
    for qr in decode(img):
        print('Decoded data: ', qr.data.decode())

    # Display the frame
    cv2.imshow("Drone", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
tello.streamoff()
