import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    print('Time is up!')

hours = int(input("Enter the number of hours for the countdown: "))
duration = hours * 60 * 60
countdown(duration)
