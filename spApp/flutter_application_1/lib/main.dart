import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Location Demo'),
        ),
        body: Center(
          child: GetLocationButton(),
        ),
      ),
    );
  }
}

class GetLocationButton extends StatefulWidget {
  @override
  _GetLocationButtonState createState() => _GetLocationButtonState();
}

class _GetLocationButtonState extends State<GetLocationButton> {
  String _location = 'กดปุ่มเพื่อดูค่า Location';

  Future<void> _getLocation() async {
    Position position = await Geolocator.getCurrentPosition(
        desiredAccuracy: LocationAccuracy.high);
    setState(() {
      _location = 'ละติจูด: ${position.latitude}, ลองจิจูด: ${position.longitude}';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text(_location),
        ElevatedButton(
          onPressed: _getLocation,
          child: const Text('ดูค่า Location'),
        ),
      ],
    );
  }
}
