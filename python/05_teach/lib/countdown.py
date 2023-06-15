import time

class CountdownTimer:
    def __init__(self, duration):
        self.duration = duration

    def start(self):
        t = self.duration
        while t:
            mins, secs = divmod(t, 60)
            hours, mins = divmod(mins, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

        print('Time is up!')
