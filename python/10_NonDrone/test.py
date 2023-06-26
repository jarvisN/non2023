from djitellopy import Tello
import time
import cv2

tello = Tello()

# print("test")

tello.connect()
# tello.streamon()

# frame_read = tello.get_frame_read()

# tello.takeoff()

# cv2.imwrite("test.png",frame_read.frame)

# tello.move_forward(200)
# tello.rotate_counter_clockwise(90)
# tello.move_left(100)

# time.sleep(10)

# tello.flip("l")

# print()
tello.query_battery()


# tello.enable_mission_pads()
# tello.set_mission_pad_detection_direction(1)

# tello.land();