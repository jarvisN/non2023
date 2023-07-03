from djitellopy import Tello

tello = Tello() # Call Function
tello.connect() # Connect Drone

# ============================================ #

tello.streamon() 
tello.streamoff()

# ============================================ #

tello.move_up()
tello.move_down()
tello.move_left()
tello.move_right()
tello.move_forward()
tello.move_back()

# ============================================ #

tello.rotate_clockwise()
tello.rotate_counter_clockwise()

# ============================================ #

tello.flip_forward()
tello.flip_back()
tello.flip_left()
tello.flip_right()

# ============================================ #

tello.enable_mission_pads()
tello.disable_mission_pads()

# 0 : downwards / 1 : forwards only / 2 : both directions
tello.set_mission_pad_detection_direction() 

