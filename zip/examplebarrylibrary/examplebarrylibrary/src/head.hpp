#define DEBUG 1 // 0 = NO-DEBUG, 1 = DEBUG
#define LITTLE 1

#define FIRMWAREVERSION 224928052023
#define VENDOR "DURIANBILL"
#define TOTALLIGHTSENSOR 8

#include <Arduino.h>
#include <memory>
#include <functional>
// #include <FS.h>
// #include <LITTLEFS.h>
// #include <WiFi.h>
// #include <ESPmDNS.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>
// #include <Update.h>

#include "bibliotheca_esp32.hpp"

Barry::INTERNET barryNet;
Barry::CONFIGURATION barryConfig;
Barry::UTILITY barryUtility;

AsyncWebServer *server;

#include "structure.hpp"
#include "flag.h"
#include "loadconfig.hpp"
#include "firstime.hpp"
#include "handleweb.hpp"