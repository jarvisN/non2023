import codecs

from importlib import import_module
openpaygo_token = import_module("openpaygo-token")
from helpers import *

def create_token(secret_key, starting_code, time_divider, token_count, restricted_digit_set=False, token_type=SET_TIME, value_days=None, value_raw=None):
    assert (value_days is not None) or (value_raw is not None)
    if value_raw is None:
        value_raw = value_days * time_divider
    token_count, token = openpaygo_token.OPAYGOEncoder.generate_standard_token(
        starting_code=starting_code,
        key=codecs.decode(secret_key, 'hex'),
        value=value_raw,
        count=token_count,
        restricted_digit_set=restricted_digit_set,
        mode=token_type
    )
    token = str(token).rjust(9, '0')
    token = ' '.join([token[i:i + 3] for i in range(0, len(token), 3)])
    return token


##==================     mod up      ================== ##

secret_key = 'a29ab82edc5fbbc41ec9530f6d123456' # คีย์ลับที่ใช้ในการสร้างโทเค็น มันเป็นสตริงแบบ hex ที่ใช้เป็นคีย์สำหรับการเข้ารหัส
starting_code = 123456789 # รหัสเริ่มต้นที่ใช้ในการสร้างโทเค็น มันเป็นตัวเลขที่ใช้เป็นจุดเริ่มต้นในการสร้างโทเค็น.
time_divider = 1 
token_count =  1 # นับจำนวนโทเค็นที่ถูกสร้าง ใช้ในการติดตามจำนวนโทเค็นที่ถูกสร้างแล้ว.
value_days = 10 # จำนวนวันที่ต้องการตั้ง



test_device_data = {
    'serial_number': 'changeme',
    'starting_code': starting_code,
    'key': secret_key,
    'restricted_digit_set': False,
    'time_divider': time_divider,
    'token_count': token_count
}

test_name = "Test1" # ชื่อการทดสอบ
description = f"Testing token for {value_days} days" # คำอธิบายการทดสอบ
# device_simulator = 'test_non'

#=============================================================#



token = create_token(secret_key, 
                     starting_code, 
                     time_divider,
                     token_count, 
                     value_days=value_days)

print("Generated token:", token)
print("\n")
duration_time = test_how_many_days(test_name,
                                   token, 
                                   value_days=value_days, 
                                   device_data=test_device_data, 
                                   description=description)

# test_how_many_days_validator(device_simulator, 
#                              test_name, 
#                              token, 
#                              value_days=value_days, 
#                              device_data=test_device_data, 
#                              description=description)