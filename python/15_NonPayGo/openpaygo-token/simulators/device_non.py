from datetime import datetime, timedelta
from shared import OPAYGOShared
from decode_token import OPAYGODecoder
from device_simulator import *

# ใส่โค้ดของคลาส DeviceSimulator ที่นี่

# สร้างอินสแตนซ์ของ DeviceSimulator ด้วยค่าเริ่มต้น
starting_code = 739798799
key = "my_secret_key"
simulator = DeviceSimulator(starting_code, key)

# แสดงสถานะของอุปกรณ์
simulator.print_status()

# # ตรวจสอบว่าอุปกรณ์ยังใช้งานได้หรือไม่
# if simulator.is_active():
#     print("Device is active.")
# else:
#     print("Device is not active.")

# # ป้อนโทเค็นเข้าสู่อุปกรณ์
# token = "739798799"
# result = simulator.enter_token(token)
# if result == 1:
#     print("Token is valid.")
# elif result == -1:
#     print("Token is invalid.")
# elif result == -2:
#     print("Token is old.")
# else:
#     print("Token entry is blocked.")

# # แสดงวันที่เหลือของอุปกรณ์
# days_remaining = simulator.get_days_remaining()
# print(f"Days remaining: {days_remaining}")

# # คุณสามารถเรียกใช้ฟังก์ชันอื่นๆ ในคลาสตามต้องการ
# a = "739798799"
# print(len(a))

# print(simulator.enter_token(token="739798799"))
# print(simulator.enter_token(token="123456789"))
print(simulator.enter_token(token="739798799"))
