constexpr auto jsonConfiguration PROGMEM = "/firmwareConfiguration.json";
namespace Configuration
{
    namespace GENERAL
    {
        struct device
        {
            String serial;
            String vendor;
            uint8_t initial;
            String firmwareVersion;
        };
    };
    namespace WIFI
    {
        struct General
        {
            String dns;
            String user;
            String pass;
        };
        struct Station
        {
            // Basic
            String ssid;
            String pass;
            String hostname;
        };
        struct AccessPoint
        {
            // Basic
            String ssid;
            String pass;
        };
    };
    struct Config
    {
        // WiFi::level wifiSettingLevel;
        GENERAL::device firmware;
        WIFI::General general;
        WIFI::Station station;
        WIFI::AccessPoint accesspoint;
    };
}; // namespace Configuration
Configuration::Config configuration;

namespace Sensor
{
    struct Value
    {
        float lux[TOTALLIGHTSENSOR];
        float weight;
    };
};
Sensor::Value sensor;