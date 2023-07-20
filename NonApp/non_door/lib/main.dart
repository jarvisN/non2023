import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  String responseText = '';

  Future<void> _sendRequest() async {
    const url = 'http://127.0.0.1:5000';
    const message = 'open';

    try {
      final response = await http.get(Uri.parse('$url/data?data=$message'));

      if (response.statusCode == 200) {
        setState(() {
          responseText = 'Response from server: ' + response.body;
        });
      } else {
        setState(() {
          responseText = 'Request failed with status: ${response.statusCode}.';
        });
      }
    } catch (e) {
      setState(() {
        responseText = 'Error sending request: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('HTTP Request Example'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              ElevatedButton(
                onPressed: _sendRequest,
                child: const Text('Send Request'),
              ),
              const SizedBox(height: 20),
              Text(responseText),
            ],
          ),
        ),
      ),
    );
  }
}
