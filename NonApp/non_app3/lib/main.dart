import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

// flutter run -d chrome --web-browser-flag "--disable-web-security"

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'HTTP Request Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'HTTP Request Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, this.title}) : super(key: key);

  final String? title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  Future<String>? data;

  Future<String> fetchData() async {
    final response =
        await http.get(Uri.parse('http://192.168.239.28:3000/ccapi'));

    if (response.statusCode == 200) {
      print(response.body);
      return response.body;
    } else {
      throw Exception('Failed to load post');
    }
  }



  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title!),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            FutureBuilder<String>(
              future: data,
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  return Text("status connect with camera : ok");
                } else if (snapshot.hasError) {
                  return Text('Error: ${snapshot.error}');
                }
              },
            ),
            // ElevatedButton(
            //   onPressed: () {
            //     setState(() {
            //       MyLib.performAction();
            //     });
            //   },
            //   child: Text('Fetch Data'),
            // ),
          ],
        ),
      ),
    );
  }
}
