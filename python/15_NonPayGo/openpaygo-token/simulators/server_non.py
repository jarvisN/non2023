from datetime import datetime, timedelta
from encode_token import OPAYGOEncoder
from shared import OPAYGOShared
from server_simulator import SingleDeviceServerSimulator

# สร้างอินสแตนซ์ของ SingleDeviceServerSimulator ด้วยค่าเริ่มต้น
starting_code = 12345
key = "my_secret_key"
simulator = SingleDeviceServerSimulator(starting_code, key)

# แสดงสถานะของเซิร์ฟเวอร์
simulator.print_status()

# # สร้างโทเค็นสำหรับปิดการใช้งาน PAYG
# disable_token = simulator.generate_payg_disable_token()
# print(f"PAYG Disable Token: {disable_token}")

# # สร้างโทเค็นสำหรับซิงค์ค่านับ
# sync_token = simulator.generate_counter_sync_token()
# print(f"Counter Sync Token: {sync_token}")

# สร้างโทเค็นจากวันหมดอายุใหม่
new_expiration_date = 30
token_from_date = simulator.generate_token_from_date(new_expiration_date)
print(f"Token from Date: {token_from_date}") 


