import pyotp

# สร้างรหัสลับ (Secret Key) แบบสุ่ม
secret_key = pyotp.random_base32()

# สร้าง OTP
otp = pyotp.TOTP(secret_key)
otp_code = otp.now()
print("OTP:", otp_code)
