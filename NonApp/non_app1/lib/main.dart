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
  late Future<String> data;

  @override
  void initState() {
    super.initState();
    data = fetchData();
  }

  Future<String> fetchData() async {
    final response =
        await http.get(Uri.parse('http://192.168.137.69/rest/setting/info'));

    print(response.body);
    

    if (response.statusCode == 200) {
      // If the server returns a 200 OK response, parse the JSON.
      // return jsonDecode(response.body)['key'];

      return response.body;
    } else {
      // If the server did not return a 200 OK response,
      // then throw an exception.
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
        child: FutureBuilder<String>(
          future: data,
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return Text('${snapshot.data}');
            } else if (snapshot.hasError) {
              return Text('Error: ${snapshot.error}');
            }
            // By default, show a loading spinner.
            return CircularProgressIndicator();
          },
        ),
      ),
    );
  }
}
