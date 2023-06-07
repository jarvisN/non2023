import 'package:http/http.dart' as http;
import 'dart:convert';

class TakePic {
  static Future<String> fetchData() async {
    final response =
        await http.get(Uri.parse('http://192.168.239.28:3000/ccapi/ver100/contents'));

    print(response.body);

    if (response.statusCode == 200) {
      return response.body;
    } else {
      throw Exception('Failed to load post');
    }
  }
}