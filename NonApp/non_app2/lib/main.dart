import 'package:flutter/material.dart';
import 'data/setting_info.dart';
import 'data/config_firmware.dart';

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

  @override
  void initState() {
    super.initState();
    // Removed fetchData() from here as initially no value is selected.
  }

  Future<void> fetchData() async {
    if(dropdownValue == 'Setting Info') {
      data = settingInfo.fetchData();
    } else if(dropdownValue == 'Config Firmware') {
      data = configFirmware.fetchData();
    }
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title!),
      ),
      body: Center(
        child: Column(
          children: [
            DropdownButton<String?>(
              value: dropdownValue,
              items: <String?>[null, 'Setting Info', 'Config Firmware'].map<DropdownMenuItem<String?>>((String? value) {
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
            data == null ? Text('No data') : FutureBuilder<String>(
              future: data,
              builder: (context, snapshot) {
                if (snapshot.hasData) { // Convert the data to a Map.
                  Map<String, dynamic> dataMap = jsonDecode(snapshot.data!);
                  // Create a JsonEncoder with pretty printing.
                  JsonEncoder encoder = JsonEncoder.withIndent('  ');
                  // Use the encoder to convert the Map to a pretty printed string.
                  String prettyPrintedData = encoder.convert(dataMap);
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
