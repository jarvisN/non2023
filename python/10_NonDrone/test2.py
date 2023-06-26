from djitellopy import Tello
import cv2


# create and connect

tello = Tello()
tello.connect()
tello.streamon()

# configure drone
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(0)  # forward detection only 

tello.takeoff()
pic = tello.get_frame_read()
cv2.imwrite("picture.png", pic.frame)

pad = tello.get_mission_pad_id()
window_name = 'image'


# detect and react to pads until we see pad #1

while pad != 1:
    if pad == 3:
        

        tello.move_back(30)
        tello.rotate_clockwise(90)

        break

    if pad == 8:
        tello.move_up(30)
        tello.flip_forward()

    pad = tello.get_mission_pad_id()

# graceful termination
# 安全结束程序
tello.disable_mission_pads()
tello.land()
tello.end()