from lib.countdown import CountdownTimer
from lib.cal import Non


# timer = CountdownTimer(60)  # Create an instance with a duration of 120 seconds
# timer.start()  # Start the countdown


a = Non()
# # print(a)

a.plus(20,30)
data = a.test()

# print(a)


print(f"data : {data}")


if data == 5678:
    print("okay")