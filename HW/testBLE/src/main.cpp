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

// const int fsrPin = 36;  // Analog pin connected to the FSR
// const int knownResistance = 10000;  // Resistance of the known resistor in ohms

// const int buttonPin = 2;  // Pin connected to the button
// int buttonState = HIGH;   // Current state of the button
// int lastButtonState = HIGH;  // Previous state of the button
// unsigned long lastDebounceTime = 0;  // Last time the button state was toggled
// unsigned long debounceDelay = 50;    // Debounce time in milliseconds
// int clickCount = 0;  // Counter for button clicks


// void setup() {
//   Serial.begin(9600);  // Initialize serial communication
//   pinMode(buttonPin, INPUT_PULLUP);  // Set the button pin as input with pull-up resistor
// }

// void loop() {
//   int fsrValue = analogRead(fsrPin);  // Read the analog value from the FSR pin
//   float fsrVoltage = fsrValue * (5.0 / 1023.0);  // Convert analog value to voltage
//   float fsrResistance = (5.0 - fsrVoltage) * knownResistance / fsrVoltage;  // Calculate FSR resistance

//   // Calculate force based on calibration data
//   float force = map(fsrResistance, 1000, 10000, 0, 100) + 94;  // Example calibration, adjust based on your FSR characteristics




//   if (force >0){
//     Serial.println(force);
//   }
  

//   delay(300);  // Delay for stability
// }