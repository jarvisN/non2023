import 'package:http/http.dart' as http;
import 'dart:convert';

class AutoFocus {
  static Future<void> performAction() async {
    final response = await http.post(
      Uri.parse(
          'http://192.168.137.233:3000/ccapi/ver100/shooting/control/shutterbutton'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, bool>{"af": true}),
    );

    if (response.statusCode == 200) {
      print(response.body);
    } else {
      throw Exception('Failed to trigger camera shutter');
    }
  }
}
