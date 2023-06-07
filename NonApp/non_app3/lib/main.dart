import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
// import 'package:non_app3/takePic.dart';
import 'dart:convert';
import 'autoFocus.dart';
import 'takePic.dart';


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
        await http.get(Uri.parse('http://192.168.137.233:3000/ccapi'));

    if (response.statusCode == 200) {
      // print(response.body);
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
                  return Text("Status connect with camera : ok");
                } else if (snapshot.hasError) {
                  return Text('Error: ${snapshot.error}');
                }
                // By default, show a loading spinner.
                return CircularProgressIndicator();
              },
            ),
            ElevatedButton(
              onPressed: () {
                setState(() {
                  data = fetchData();
                });
              },
              child: Text('Check Connection'),
            ),

            ElevatedButton(
              onPressed: () {
                setState(() {
                  AutoFocus();
                });
              },
              child: Text('Auto Focus'),
            ),

            ElevatedButton(
                onPressed: () {
                  setState(() {
                    TakePic();
                  });
                },
                child: Text('Take Image'),
                ),

          ],
        ),
      ),
    );
  }
}
