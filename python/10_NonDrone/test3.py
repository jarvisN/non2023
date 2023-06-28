from djitellopy import Tello
import time
import cv2




tello = Tello()
tello.connect()

tello.query_battery()


# tello.streamoff()

tello.streamon()
frame_read = tello.get_frame_read()

print("\n=================================\n")
print(type(frame_read))

print("\n=================================\n")
print(frame_read)

tello.streamoff()
# tello.takeoff()
# cv2.imwrite("picture.png", frame_read.frame)

# tello.land()