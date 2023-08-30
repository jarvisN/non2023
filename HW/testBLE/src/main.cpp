#include <Arduino.h>
#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32test"); //Name of your Bluetooth Signal
  Serial.println("The device started, now you can pair it with bluetooth!");
  randomSeed(analogRead(0)); // Initialize random number generator
}

void loop() {
  int randomNumber = random(1, 6); // Generate random number between 1 and 5
  String randomNumberString = String(randomNumber); // Convert random number to string
  SerialBT.println(randomNumberString); //Send Data
  Serial.println(randomNumber);
  delay(500); // Delay for 1 second
}
