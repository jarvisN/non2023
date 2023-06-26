from djitellopy import Tello
import time
import cv2




tello = Tello()
tello.connect()

tello.query_battery()


tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
cv2.imwrite("picture.png", frame_read.frame)

tello.streamoff()
tello.land()