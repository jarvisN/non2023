from flask import Flask, request
from flask_cors import CORS
import pyotp



app = Flask(__name__)
CORS(app)

# @app.route('/data', methods=['GET'])
# def receive_data():
#     data = request.form.get('data')
#     if data:
#         # Do something with the received data
#         return 'Data received: ' + data
#     else:
#         return 'No data received.'

@app.route('/data', methods=['GET'])
def receive_data():
    data = request.args.get('data')
    if data:
        print(data)
        return 'Data received: ' + data
    else:
        return 'No data received.'
@app.route('/test', methods = ['GET'])
def test():
    return "test"

@app.route('/generate_otp')
def generate_otp():
    # สร้างรหัสลับ (Secret Key) แบบสุ่ม
    secret_key = pyotp.random_base32()

    # สร้าง OTP
    otp = pyotp.TOTP(secret_key)
    otp_code = otp.now()

    return {'otp': otp_code}

if __name__ == '__main__':
    app.run()
