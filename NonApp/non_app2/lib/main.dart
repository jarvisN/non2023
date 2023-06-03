import 'package:flutter/material.dart';
import 'data/setting_info.dart';
import 'data/config_firmware.dart';
import 'data/getLux.dart';
import 'data/getWeight.dart';
import 'dart:convert';

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
  String? dropdownValue;
  String? inputFieldData;

  @override
  void initState() {
    super.initState();
  }

  Future<void> fetchData() async {
    if (dropdownValue == 'Setting Info') {
      data = settingInfo.fetchData();
    } else if (dropdownValue == 'Config Firmware') {
      data = configFirmware.fetchData();
    } else if (dropdownValue == 'Lux') {
      data = Lux.fetchData();
    } else if (dropdownValue == 'Weight') {
      data = Weight.fetchData();
    }
    setState(() {});
  }

  String prettyPrintJson(String jsonString) {
    var json = jsonDecode(jsonString);
    var encoder = JsonEncoder.withIndent('  ');
    String prettyString = encoder.convert(json);
    return prettyString;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title!),
      ),
      body: Center(
        child: Column(
          children: [TextField(
              onChanged: (String? value) {
                setState(() {
                  inputFieldData = value;
                });
              },
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Input Field',
              ),
            ),
            DropdownButton<String?>(
              value: dropdownValue,
              items: <String?>[
                null,
                'Setting Info',
                'Config Firmware',
                'Lux',
                'Weight'
              ].map<DropdownMenuItem<String?>>((String? value) {
                return DropdownMenuItem<String?>(
                  value: value,
                  child: Text(value ?? 'None'),
                );
              }).toList(),
              onChanged: (String? newValue) {
                setState(() {
                  dropdownValue = newValue;
                  if (dropdownValue != null) {
                    fetchData();
                  } else {
                    data = null;
                  }
                });
              },
            ),
            data == null
                ? Text('No data')
                : FutureBuilder<String>(
                    future: data,
                    builder: (context, snapshot) {
                      if (snapshot.hasData) {
                        String prettyPrintedData =
                            prettyPrintJson(snapshot.data!);
                        return Text(prettyPrintedData);
                      } else if (snapshot.hasError) {
                        return Text('Error: ${snapshot.error}');
                      }
                      return CircularProgressIndicator();
                    },
                  ),
          ],
        ),
      ),
    );
  }
}
