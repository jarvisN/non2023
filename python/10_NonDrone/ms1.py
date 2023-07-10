from djitellopy import Tello
import time

tello = Tello() # Call Function
tello.connect() # Connect Drone
# tello.query_flight_time()
tello.get_flight_time()

tello.turn_motor_on()
tello.takeoff()

tello.move_up(20)
time.sleep(1)
print(f'height : {tello.get_height()}')



tello.move_up(20)
time.sleep(1)
print(f'height : {tello.get_height()}')

print(f'x : {tello.get_acceleration_x()}')
time.sleep(1)
tello.move_back(20)
time.sleep(1)
print(f'x : {tello.get_acceleration_x()}')

time.sleep(20)

tello.land()
tello.turn_motor_off()
tello.end()