
#if LINE == 1
#define linea(x) Serial.print(x)
#define nvlinea(x) Serial.println(x)
#else
#define linea(x)
#define nvlinea(x)
#endif

#if DEBUG == 1
#define debug(x) linea(x)
#define debugln(x) nvlinea(x)
#else
#define debug(x)
#define debugln(x)
#endif

#if RTCPCB == 1
#define RTCIC RTC_DS3231
#else
#define RTCIC RTC_DS1307
#endif

#include <memory>

// INTERNET WIFI
#if defined(ESP8266)
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
ESP8266WiFiMulti WiFiMulti;
#elif defined(ESP32)
#include <WiFi.h>
#else
#error only ESP32 or ESP8266 supported at the moment
#endif
#include <ESPmDNS.h>
// #include <ESP32Ping.h>
//INTERNET LAN
#include <SPI.h>
#include <Ethernet.h>

// CONFIGURATION
#include "FS.h"
#define FORMAT_IF_FAILED true
#if LITTLE == 1
#include <LITTLEFS.h>
#define SPIFFS LITTLEFS
#else
#include "SPIFFS.h"
#endif

// TIME
#include "RTClib.h"
#include <TimeLib.h>

// RFID
#include <RFID.h>

// UTILITY
#include <Update.h>

#include <ArduinoJson.h>
// #include "external/barryJson.hpp"