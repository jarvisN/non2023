import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'OTP App',
      home: Scaffold(
        appBar: AppBar(
          title: Text('OTP App'),
        ),
        body: Center(
          child: ElevatedButton(
            onPressed: () {
              fetchAndVerifyOTP(context);
            },
            child: Text('เข้าใช้แอป'),
          ),
        ),
      ),
    );
  }

  void fetchAndVerifyOTP(BuildContext context) async {
    try {
      final response = await http.get(Uri.parse('http://your-server-url/generate_otp'));
      if (response.statusCode == 200) {
        final otp = response.body;

        // นี่คือตัวอย่างการส่ง OTP ไปยังแอปที่อื่น เช่นการเปิดหน้าใหม่ในแอปหรือทำการนำ OTP ไปใช้ในส่วนอื่นของแอป
        // ในตัวอย่างนี้จะแสดงแค่กล่องข้อความแสดง OTP
        showDialog(
          context: context,
          builder: (BuildContext context) {
            return AlertDialog(
              title: Text('OTP'),
              content: Text('OTP ที่ได้รับคือ: $otp'),
              actions: [
                TextButton(
                  onPressed: () {
                    Navigator.of(context).pop();
                  },
                  child: Text('ตกลง'),
                ),
              ],
            );
          },
        );
      } else {
        throw Exception('ไม่สามารถรับ OTP ได้');
      }
    } catch (error) {
      print('เกิดข้อผิดพลาดในการรับ OTP: $error');
    }
  }
}
