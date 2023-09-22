#include <Arduino.h>

const int sensorPin1 = 34; // GPIO 34 for Force Sensor 1
const int sensorPin2 = 35; // GPIO 35 for Force Sensor 2
const int sensorPin3 = 32; // GPIO 36 for Force Sensor 3
const int sensorPin4 = 33; // GPIO 39 for Force Sensor 4
const int sensorPin5 = 25; // GPIO 4 for Force Sensor 5
const int ledPin = 2;      // Built-in LED, GPIO 2
const int motor1 = 16;

void setup()
{
  pinMode(sensorPin1, INPUT);
  pinMode(sensorPin2, INPUT);
  pinMode(sensorPin3, INPUT);
  pinMode(sensorPin4, INPUT);
  pinMode(sensorPin5, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(motor1, OUTPUT);
  Serial.begin(115200);
}

void loop()
{
  int sensorValue1 = analogRead(sensorPin1);
  int sensorValue2 = analogRead(sensorPin2);
  int sensorValue3 = analogRead(sensorPin3);
  int sensorValue4 = analogRead(sensorPin4);
  int sensorValue5 = analogRead(sensorPin5);

  // Threshold value for detecting a press
  int threshold = 1000;

  // Check if any of the sensors are pressed
  if (sensorValue1 > threshold || sensorValue2 > threshold ||
      sensorValue3 > threshold || sensorValue4 > threshold ||
      sensorValue5 > threshold)
  {
    // If any sensor is pressed, turn on the LED
    digitalWrite(ledPin, HIGH);
    digitalWrite(motor1, HIGH);
    Serial.println("Pressed!");
  }
  else
  {
    // If no sensor is pressed, turn off the LED
    digitalWrite(ledPin, LOW);
    digitalWrite(motor1, LOW);
  }

  delay(100); // Wait for a moment before reading values again
}
