import 'package:http/http.dart' as http;
import 'dart:convert';

class Weight {
  static Future<String> fetchData() async {
    final response =
        await http.get(Uri.parse('http://192.168.137.69/rest/weight'));

    print(response.body);

    if (response.statusCode == 200) {
      return response.body;
    } else {
      throw Exception('Failed to load post');
    }
  }
}
