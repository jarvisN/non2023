// header file - your-library/header1.h

#ifndef BIBLIOTHECA_H
#define BIBLIOTHECA_H

#include "config.h"
#include "esp32_superhead.hpp"

namespace Barry
{
    class UTILITY
    {
    public:
        void powerInit(uint8_t const &pin = POWERPIN, uint8_t const &active = PINLOW);
        void resetPower(uint8_t const &pin = POWERPIN, uint8_t const &active = PINHIGH);
        bool ota(WiFiClient &client, String const &host, uint16_t port, String const &bin);

    private:
        long contentLength = 0;
        bool isValidContentType = false;
        String getHeaderValue(String const &header, String const &headerName);
        // void setPIN();
    };
    class CONFIGURATION
    {
    public:
        bool formatFS(bool const &execute);
        std::unique_ptr<DynamicJsonDocument> readJSONFromFile(const char *filename, std::size_t fieldCount, bool &flag);
        void printFile(const char *filename);
        void fsInit(void);
        template <typename T>
        void loadAndSave(void (*load)(const char *, T &, bool &), void (*save)(const char *, const T &, const bool &), const char *filename, T &stucture, bool &havingFlag);

    private:
        Barry::UTILITY utilityInstance;
    };
    class INTERNET
    {
    public:
        void wifiSetup(bool const &activate, String const &ssidSTA, String const &passSTA, String const &ssidAP, String const &passAP, String const &domain);
        void lanSetup(uint8_t const &csPin, byte *mac, const IPAddress &ip);
        // bool checkInternetConnection(const uint8_t &sec);
        String getLocalIP(const char &prefix);
        int8_t wifiRSSI(const int8_t &RSSI = WiFi.RSSI());
        uint8_t getRSSIPercentage(const int8_t &RSSI = WiFi.RSSI());

    private:
        struct Shared
        {
            String ssidSTA;
            String passSTA;
            String dns;
        };
        static Shared shared;
        static void WiFiStationConnected(WiFiEvent_t event, WiFiEventInfo_t info);
        static void WiFiGotIP(WiFiEvent_t event, WiFiEventInfo_t info);
        static void WiFiStationDisconnected(WiFiEvent_t event, WiFiEventInfo_t info);
        // static void WiFiEventHandler(WiFiEvent_t event, WiFiEventInfo_t info);
        // static void (*wifiEventFunctions[])(WiFiEvent_t, WiFiEventInfo_t);
    };
    class TIME
    {
    public:
        void rtcInit();
        void readTime(const char &prefix); // E = rtc, I = ESP
        void printTime(const char &prefix);
        void adjustTime(const char &prefix, uint16_t const &yy, uint8_t const &mt, uint8_t const &dd, uint8_t const &hh, uint8_t const &mm, uint8_t const &ss);
        struct DateTimeValues
        {
            uint16_t year;
            uint8_t month;
            uint8_t day;
            uint8_t hour;
            uint8_t minute;
            uint8_t second;
        };

        // std::unique_ptr<DateTimeValues> dateTime;
        DateTimeValues external;
        DateTimeValues internal;

    private:
        DateTime now;
        DateTime lastBoot;
        RTCIC rtc;
        Barry::UTILITY utilityInstance;
    };
    class RFID
    {
    public:
        void rfidInit(uint8_t const &pin = RFIDPIN, uint8_t const &active = PINLOW);
        bool readRFID(const char &prefix, uint32_t const &readTime, String &result);

    private:
        RFIDLIB rfid;
        Barry::UTILITY utilityInstance;
    };
    class BUZZER
    {
    public:
        void buzzerInit(uint8_t const &pin = BUZZPIN, uint8_t const &active = PINLOW);
        void beep(uint32_t const &interval, uint32_t const &count);

    private:
        uint8_t unactive;
        uint8_t pin;
    };
}
#endif // BIBLIOTHECA_H

// BUZZER
void Barry::BUZZER::buzzerInit(uint8_t const &pin, uint8_t const &active)
{
    pinMode(pin, OUTPUT);
    digitalWrite(pin, active);
    delay(15);

    Barry::BUZZER::pin = pin;
    Barry::BUZZER::unactive = active;
}
void Barry::BUZZER::beep(uint32_t const &interval, uint32_t const &count)
{
    for (register uint32_t i = 1; i <= count; i++)
    {
        digitalWrite(Barry::BUZZER::pin, Barry::BUZZER::unactive ^ 0x1);
        swDelay(interval);
        digitalWrite(Barry::BUZZER::pin, Barry::BUZZER::unactive);
        if (i < count)
        {
            swDelay(interval);
        }
    }
}

// RFID
void Barry::RFID::rfidInit(uint8_t const &pin, uint8_t const &active)
{
    pinMode(pin, OUTPUT);
    digitalWrite(pin, active);
    delay(15);

    if (!rfid.init())
    {
        Serial.println(F("RFID Fail"));
        utilityInstance.resetPower();
        return;
    }
    Serial.println(F("RFID Ready"));
}

bool Barry::RFID::readRFID(const char &prefix, uint32_t const &readTime, String &result)
{
    register bool success = false;
    if (prefix == 'D')
    {
        rfid.getIdDecimal(result, success, readTime);
    }
    else if (prefix == 'H')
    {
        rfid.getIdHex(result, success, readTime);
    }

    return success;
}

// UTILITY

// void Barry::UTILITY::setPIN()
// {
//     pinMode(POWERPIN, OUTPUT);
//     digitalWrite(POWERPIN, LOW);
// }
void Barry::UTILITY::powerInit(uint8_t const &pin, uint8_t const &active)
{
    pinMode(pin, OUTPUT);
    digitalWrite(pin, active);
    delay(15);
}

void Barry::UTILITY::resetPower(uint8_t const &pin, uint8_t const &active)
{
    debugln(F("RESET POWER..."));
    digitalWrite(pin, active); // reset power
    delay(5000);
    debugln(F("FAILED RESET POWER..."));
}

String Barry::UTILITY::getHeaderValue(String const &header, String const &headerName)
{
    return header.substring(strlen(headerName.c_str()));
}

bool Barry::UTILITY::ota(WiFiClient &client, String const &host, uint16_t port, String const &bin)
{
    bool result = false;

    Serial.println("Connecting to: " + String(host));
    // Connect to S3
    if (client.connect(host.c_str(), port))
    {
        // Connection Succeed.
        // Fecthing the bin
        Serial.print(F("Fetching Bin: "));
        Serial.println(String(bin));

        // Get the contents of the bin file
        client.print(String("GET ") + bin + " HTTP/1.1\r\n" +
                     "Host: " + host + "\r\n" +
                     "Cache-Control: no-cache\r\n" +
                     "Connection: close\r\n\r\n");

        // Check what is being sent
        //    Serial.print(String("GET ") + bin + " HTTP/1.1\r\n" +
        //                 "Host: " + host + "\r\n" +
        //                 "Cache-Control: no-cache\r\n" +
        //                 "Connection: close\r\n\r\n");

        unsigned long timeout = millis();
        while (client.available() == 0)
        {
            if (millis() - timeout > 5000)
            {
                Serial.println(F("Client timeout !"));
                client.stop();
                return false;
            }
        }
        // Once the response is available,
        // check stuff

        /*
           Response Structure
            HTTP/1.1 200 OK
            x-amz-id-2: NVKxnU1aIQMmpGKhSwpCBh8y2JPbak18QLIfE+OiUDOos+7UftZKjtCFqrwsGOZRN5Zee0jpTd0=
            x-amz-request-id: 2D56B47560B764EC
            Date: Wed, 14 Jun 2017 03:33:59 GMT
            Last-Modified: Fri, 02 Jun 2017 14:50:11 GMT
            ETag: "d2afebbaaebc38cd669ce36727152af9"
            Accept-Ranges: bytes
            Content-Type: application/octet-stream
            Content-Length: 357280
            Server: AmazonS3

            {{BIN FILE CONTENTS}}

        */
        while (client.available())
        {
            // read line till /n
            String line = client.readStringUntil('\n');
            line.trim();
            // remove space, to check if the line is end of headers
            line.trim();

            // if the the line is empty,
            // this is end of headers
            // break the while and feed the
            // remaining `client` to the
            // Update.writeStream();
            if (!line.length())
            {
                // headers ended
                break; // and get the OTA started
            }

            // Check if the HTTP Response is 200
            // else break and Exit Update
            if (line.startsWith("HTTP/1.1"))
            {
                if (line.indexOf("200") < 0)
                {
                    Serial.println(F("Got a non 200 status code from server. Exiting OTA Update."));
                    break;
                }
            }

            // extract headers here
            // Start with content length
            if (line.startsWith("Content-Length: "))
            {
                contentLength = atol((getHeaderValue(line, "Content-Length: ")).c_str());
                Serial.print(F("Got "));
                Serial.print(String(contentLength));
                Serial.println(F(" bytes from server"));
            }

            // Next, the content type
            if (line.startsWith("Content-Type: "))
            {
                String contentType = getHeaderValue(line, "Content-Type: ");
                Serial.print(F("Got "));
                Serial.print(contentType[0]);
                Serial.print(F(" payload."));
                if (contentType == "application/octet-stream")
                {
                    isValidContentType = true;
                }
            }
        }
    }
    else
    {
        // Connect to S3 failed
        // May be try?
        // Probably a choppy network?
        Serial.print(F("Connection to "));
        Serial.print(String(host));
        Serial.println(F(" failed. Please check your setup"));
        // retry??
        // execOTA();
    }

    // Check what is the contentLength and if content type is `application/octet-stream`
    Serial.print(F("contentLength : "));
    Serial.print(String(contentLength));
    Serial.print(F(", isValidContentType : "));
    Serial.println(String(isValidContentType));

    // check contentLength and content type
    if (contentLength && isValidContentType)
    {
        // Check if there is enough to OTA Update
        bool canBegin = Update.begin(contentLength);

        // If yes, begin
        if (canBegin)
        {
            Serial.println(F("Begin OTA. This may take 2 - 5 mins to complete. Things might be quite for a while.. Patience!"));
            // No activity would appear on the Serial monitor
            // So be patient. This may take 2 - 5mins to complete
            size_t written = Update.writeStream(client);

            if (written == contentLength)
            {
                Serial.print(F("Written : "));
                Serial.print(String(written));
                Serial.print(F(" successfully"));
            }
            else
            {
                Serial.print(F("Written only : "));
                Serial.print(String(written));
                Serial.print(F("/"));
                Serial.print(String(contentLength));
                Serial.print(F(". Retry?"));
                // retry??
                // execOTA();
            }

            if (Update.end())
            {
                Serial.println("OTA done!");
                if (Update.isFinished())
                {
                    Serial.println(F("Update successfully completed. Rebooting."));
                    result = true;
                    return true;
                    // ESP.restart();
                }
                else
                {
                    Serial.println(F("Update not finished? Something went wrong!"));
                }
            }
            else
            {
                Serial.print(F("Error Occurred. Error #: "));
                Serial.println(String(Update.getError()));
            }
        }
        else
        {
            // not enough space to begin OTA
            // Understand the partitions and
            // space availability
            Serial.println(F("Not enough space to begin OTA"));
            client.flush();
        }
    }
    else
    {
        Serial.println(F("There was no content in the response"));
        client.flush();
    }

    return result ? true : false;
}

// CONFIGURATION

bool Barry::CONFIGURATION::formatFS(bool const &execute)
{
    if (!execute)
    {
        return false;
    }

    if (SPIFFS.format())
    {
        debugln(F("SPIFFS file system formatted successfully"));

        utilityInstance.resetPower();

        ESP.restart();
        return true;
    }
    else
    {
        debugln(F("An error occurred while formatting SPIFFS file system"));
        return false;
    }
}

std::unique_ptr<DynamicJsonDocument> Barry::CONFIGURATION::readJSONFromFile(const char *filename, std::size_t fieldCount, bool &havingFlag)
{
    File file = SPIFFS.open(filename);
    auto doc = std::unique_ptr<DynamicJsonDocument>(new DynamicJsonDocument(JSON_OBJECT_SIZE(fieldCount) + (uint32_t)file.size() * 1.25));
    DeserializationError error = deserializeJson(*doc, file);

    if (error)
    {
        nvlinea(F("Failed to read JSON, using default JSON"));
        havingFlag = false;
    }

    file.close();
    return doc;
}

void Barry::CONFIGURATION::printFile(const char *filename)
{
    File file = SPIFFS.open(filename);
    if (!file)
    {
        nvlinea(F("Failed to read file"));
        return;
    }
    while (file.available())
    {
        linea(static_cast<char>(file.read()));
    }
    nvlinea();

    file.close();
}

void Barry::CONFIGURATION::fsInit(void)
{
    if (!SPIFFS.begin(FORMAT_IF_FAILED))
    {
        nvlinea(F("File System Mount Failed"));
        return;
    }
}
template <typename T>
void Barry::CONFIGURATION::loadAndSave(void (*load)(const char *, T &, bool &), void (*save)(const char *, const T &, const bool &), const char *filename, T &stucture, bool &havingFlag)
{
    nvlinea(F("Loading..."));
    load(filename, stucture, havingFlag);

    if (!havingFlag)
    {
        nvlinea(F("Not found. Saving default value..."));
        save(filename, stucture, havingFlag);
        havingFlag = true;
    }

    nvlinea(F("Displaying file contents..."));
    printFile(filename);
}

// INTERNET

Barry::INTERNET::Shared Barry::INTERNET::shared;

// void (*Barry::INTERNET::wifiEventFunctions[])(WiFiEvent_t, WiFiEventInfo_t) = {
//     &Barry::INTERNET::WiFiStationConnected,
//     &Barry::INTERNET::WiFiGotIP,
//     &Barry::INTERNET::WiFiStationDisconnected};

void Barry::INTERNET::WiFiStationConnected(WiFiEvent_t event, WiFiEventInfo_t info)
{
    nvlinea(F("Connected to AP successfully!"));
}
void Barry::INTERNET::WiFiGotIP(WiFiEvent_t event, WiFiEventInfo_t info)
{
    // while (WiFi.waitForConnectResult() != WL_CONNECTED)
    // {
    //     linea(F("9"));
    //     // yield();
    //     delay(1000);
    // }
    nvlinea(F("WiFi connected"));
    linea(F("Local IP: "));
    nvlinea(WiFi.localIP());
    linea(F("Subnet Mask: "));
    nvlinea(WiFi.subnetMask());
    linea(F("Gateway IP: "));
    nvlinea(WiFi.gatewayIP());
    linea(F("Primary DNS: "));
    nvlinea(WiFi.dnsIP(0));
    linea(F("Secondary DNS: "));
    nvlinea(WiFi.dnsIP(1));
    linea(F("Hostname: "));
    nvlinea(WiFi.getHostname());
    // String taskMessage = "WIFI running on core ";
    // taskMessage = taskMessage + xPortGetCoreID();
    // Serial.println(taskMessage);
}
void Barry::INTERNET::WiFiStationDisconnected(WiFiEvent_t event, WiFiEventInfo_t info)
{
    nvlinea(F("Disconnected from WiFi access point"));
    nvlinea(F("Trying to Reconnect"));
    linea(F("SSID : "));
    linea(Barry::INTERNET::shared.ssidSTA);
    linea(F(", PASS : "));
    linea(Barry::INTERNET::shared.passSTA);
    linea(F(", MDNS : "));
    nvlinea(Barry::INTERNET::shared.dns);
    WiFi.begin(Barry::INTERNET::shared.ssidSTA.c_str(), Barry::INTERNET::shared.passSTA.c_str());

    if (!MDNS.begin(Barry::INTERNET::shared.dns.c_str()))
    {
        nvlinea(F("Error starting mDNS"));
        // return;
    }
}

// void Barry::INTERNET::WiFiEventHandler(WiFiEvent_t event, WiFiEventInfo_t info)
// {
//     if (event >= ARDUINO_EVENT_WIFI_STA_CONNECTED && event <= ARDUINO_EVENT_WIFI_STA_DISCONNECTED)
//     {
//         wifiEventFunctions[event - ARDUINO_EVENT_WIFI_STA_CONNECTED](event, info);
//     }
// }

void Barry::INTERNET::wifiSetup(bool const &activate, String const &ssidSTA, String const &passSTA, String const &ssidAP, String const &passAP, String const &domain)
{
    if (!activate)
    {
        nvlinea(F("WiFi is not ACTIVATE"));
        return;
    }

    shared.ssidSTA = ssidSTA;
    shared.passSTA = passSTA;
    shared.dns = domain;

    WiFi.mode(WIFI_AP_STA);

    linea(F("Setting AP (Access Point)…"));
    WiFi.softAP(ssidAP.c_str(), passAP.c_str());

    linea(F("AP IP : "));
    nvlinea(WiFi.softAPIP());

    WiFi.disconnect(true);

#if WIFI_ARDUINO_EVENT == 1
    WiFi.onEvent(WiFiStationConnected, ARDUINO_EVENT_WIFI_STA_CONNECTED);
    WiFi.onEvent(WiFiGotIP, ARDUINO_EVENT_WIFI_STA_GOT_IP);
    WiFi.onEvent(WiFiStationDisconnected, ARDUINO_EVENT_WIFI_STA_DISCONNECTED);
#else
    WiFi.onEvent(WiFiStationConnected, SYSTEM_EVENT_STA_CONNECTED);
    WiFi.onEvent(WiFiGotIP, SYSTEM_EVENT_STA_GOT_IP);
    WiFi.onEvent(WiFiStationDisconnected, SYSTEM_EVENT_STA_DISCONNECTED);
#endif

    WiFi.setHostname(ssidAP.c_str());

    WiFi.begin(ssidSTA.c_str(), passSTA.c_str());
    if (!MDNS.begin(domain.c_str()))
    {
        nvlinea(F("Error starting mDNS"));
    }
}

void Barry::INTERNET::lanSetup(uint8_t const &csPin, byte *mac, const IPAddress &ip)
{
    Ethernet.init(5); // MKR ETH shield
    // start the Ethernet connection and the server:
    if (Ethernet.begin(mac) == 0)
    {
        nvlinea(F("Failed to configure Ethernet using DHCP"));
        // If DHCP fails, you may want to assign a static IP as a fallback
        Ethernet.begin(mac, ip);
    }
    // Check for Ethernet hardware present
    if (Ethernet.hardwareStatus() == EthernetNoHardware)
    {
        nvlinea(F("Ethernet shield was not found.  Sorry, can't run without hardware. :("));
        while (true)
        {
            delay(1); // do nothing, no point running without Ethernet hardware
        }
    }
    if (Ethernet.linkStatus() == LinkOFF)
    {
        nvlinea(F("Ethernet cable is not connected."));
    }
    nvlinea(F("server is at "));
    nvlinea(Ethernet.localIP());
}

// bool Barry::INTERNET::checkInternetConnection(const uint8_t &sec)
// {
//     bool success = Ping.ping("www.google.com", sec);
//     return success;
// }

String Barry::INTERNET::getLocalIP(const char &prefix)
{
    if (prefix == 'W')
    {
        IPAddress temp = WiFi.localIP();
        std::unique_ptr<String> result(new String());

        for (register uint8_t counter = 0; counter < 4; counter++)
        {
            *result += counter ? "." + String(temp[counter]) : String(temp[counter]);
        }
        return *result;
    }
    else if (prefix == 'L')
    {
        // ipToString(Ethernet.localIP());
        IPAddress temp = Ethernet.localIP();
        std::unique_ptr<String> result(new String());

        for (register uint8_t counter = 0; counter < 4; counter++)
        {
            *result += counter ? "." + String(temp[counter]) : String(temp[counter]);
        }
        return *result;
    }
}

int8_t Barry::INTERNET::wifiRSSI(const int8_t &RSSI)
{
    return RSSI;
}

uint8_t Barry::INTERNET::getRSSIPercentage(const int8_t &RSSI)
{
    if (RSSI <= -100)
    {
        return 0;
    }
    else if (RSSI >= -50)
    {
        return 100;
    }
    else
    {
        return 2 * (RSSI + 100);
    }
}

// TIME

void Barry::TIME::rtcInit()
{

#ifndef ESP8266
    while (!Serial)
        ; // wait for serial port to connect. Needed for native USB
#endif

    if (!rtc.begin())
    {
        Serial.println(F("Couldn't find RTC"));
        Serial.flush();
        // resetPower(POWERPIN);
        utilityInstance.resetPower();
    }

#if RTCPCB == 0
    if (!rtc.isrunning())
    {
        Serial.println(F("RTC is NOT running, let's set the time!"));
        rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
    }
#endif
    lastBoot = DateTime(F(__DATE__), F(__TIME__));

    Serial.print(F("UPLOAD FIRMWARE TIME : "));
    Serial.println(lastBoot.timestamp());

    DateTime dt = rtc.now();
    std::unique_ptr<char[]> buffer(new char[20]);
    snprintf(buffer.get(), 20, "%04d-%02d-%02dT%02d:%02d:%02dZ", dt.year(), dt.month(), dt.day(), dt.hour(), dt.minute(), dt.second());
    Serial.println(buffer.get());
}

// Access the date and time values using rtcReader.dateTime->year, rtcReader.dateTime->month, rtcReader.dateTime->day, rtcReader.dateTime->hour, rtcReader.dateTime->minute, rtcReader.dateTime->second
void Barry::TIME::readTime(const char &prefix)
{
    if (prefix == 'E')
    {
        now = rtc.now();

        external.year = now.year();
        external.month = now.month();
        external.day = now.day();
        external.hour = now.hour();
        external.minute = now.minute();
        external.second = now.second();
    }
    else if (prefix == 'I')
    {
        internal.year = year();
        internal.month = month();
        internal.day = day();
        internal.hour = hour();
        internal.minute = minute();
        internal.second = second();
    }
}

void Barry::TIME::printTime(const char &prefix)
{
    if (prefix == 'E')
    {
        debug(F("RTC: "));
        debug(external.year);
        debug(F("/"));
        debug(external.month);
        debug(F("/"));
        debug(external.day);
        debug(F(" "));
        debug(external.hour);
        debug(F(":"));
        debug(external.minute);
        debug(F(":"));
        debug(external.second);
        debugln(F(""));
    }
    else if (prefix == 'I')
    {
        debug(F("ESP: "));
        debug(internal.year);
        debug(F("/"));
        debug(internal.month);
        debug(F("/"));
        debug(internal.day);
        debug(F(" "));
        debug(internal.hour);
        debug(F(":"));
        debug(internal.minute);
        debug(F(":"));
        debug(internal.second);
        debugln(F(""));
    }
}

void Barry::TIME::adjustTime(const char &prefix, uint16_t const &yy, uint8_t const &mt, uint8_t const &dd, uint8_t const &hh, uint8_t const &mm, uint8_t const &ss)
{
    if (prefix == 'E')
    {
        rtc.adjust(DateTime(yy, mt, dd, hh, mm, ss));
    }
    else if (prefix == 'I')
    {
        setTime(hh, mm, ss, dd, mt, yy);
    }
}
