#include "head.hpp"

// put function declarations here:
int myFunction(int, int);

void setup()
{
  Serial.begin(115200);
  barryConfig.fsInit();
  allLoading();
  firstTimeSetting(configuration.firmware.initial);

  barryNet.wifiSetup(true, configuration.station.ssid, configuration.station.pass, configuration.accesspoint.ssid, configuration.accesspoint.pass, configuration.general.dns);

  webserverMangement();
}

void loop()
{
  // put your main code here, to run repeatedly:
}

// put function definitions here:
int myFunction(int x, int y)
{
  return x + y;
}