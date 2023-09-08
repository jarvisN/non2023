#include <Arduino.h>
#include "BluetoothSerial.h"

BluetoothSerial SerialBT;



const int fsrPin = 36;             // Analog pin connected to the FSR
const int knownResistance = 10000; // Resistance of the known resistor in ohms

const int buttonPin = 2;            // Pin connected to the button
int buttonState = HIGH;             // Current state of the button
int lastButtonState = HIGH;         // Previous state of the button
unsigned long lastDebounceTime = 0; // Last time the button state was toggled
unsigned long debounceDelay = 50;   // Debounce time in milliseconds
int clickCount = 0;                 // Counter for button clicks

const int PRESS_THRESHOLD = 300;  // Adjust this value based on your sensor's sensitivity
bool wasPressed = false;

void setup()
{
  Serial.begin(115200);             // Initialize serial communication
  pinMode(buttonPin, INPUT_PULLUP); // Set the button pin as input with pull-up resistor
}

void loop()
{
  int fsrValue = analogRead(fsrPin);                                       // Read the analog value from the FSR pin
  float fsrVoltage = fsrValue * (5.0 / 1023.0);                            // Convert analog value to voltage
  float fsrResistance = (5.0 - fsrVoltage) * knownResistance / fsrVoltage; // Calculate FSR resistance

  // Calculate force based on calibration data
  // float force1 = map(fsrResistance, 1000, 10000, 0, 100) + 94; // Example calibration, adjust based on your FSR characteristics
  int force1 = map(fsrResistance, 1000, 10000, 0, 100) + 94; // Example calibration, adjust based on your FSR characteristics

  if (force1 > 0 and force1 != 83)
  {
    Serial.println(force1);
  }

  // Serial.println(force);

  // Check if the sensor is being pressed
  if (fsrValue > PRESS_THRESHOLD && !wasPressed)
  {
    wasPressed = true;
    clickCount++;
    // Serial.println("Sensor pressed!");
    // Here you can send data based on the press if required
  }
  else if (fsrValue <= PRESS_THRESHOLD && wasPressed)
  {
    wasPressed = false;
  }

  delay(300); // Delay for stability
}