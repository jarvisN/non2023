constexpr auto jsonConfiguration PROGMEM = "/firmwareConfiguration.json";
namespace Configuration
{
    namespace General
    {
        struct device
        {
            String serial;
            String vendor;
            String mac;
        };
    };
    namespace Connectivity
    {
        enum Select : uint8_t
        {
            WIFI,
            ETHERNET
        };
        Select type;
    }
    namespace WiFi
    {
        enum Level : uint8_t
        {
            BASIC,
            INTERMEDIATE,
            ADVANCED
        };
        struct General
        {
            String dns;
        };
        struct Station
        {
            Level level;
            // Basic
            String ssid;
            String pass;
            String hostname;
            // Intermediate
            String ipV4;
            // Advanced
            String ipV6;
            String gateway;
            String subnet;
            String primaryDNS;
            String secondaryDNS;
        };
        struct AccessPoint
        {
            Level level;
            // Basic
            String ssid;
            String pass;
            // Intermediate
            String ipV4;
            bool hidden;
            uint8_t maxConnection;
            // Advanced
            String gateway;
            String subnet;
            String primaryDNS;
            String secondaryDNS;
            uint8_t channel;
        };
    };
    namespace Ethernet
    {
        // Basic
        String mac;
        String ip;
        // Intermidiate
        String gateway;
        String subnet;
        String dns;
    }

    struct Config
    {
        // WiFi::level wifiSettingLevel;

        String dns;
        String user;
        String pass;

        uint16_t apPort;
        String apSSID;
        String apPass;

        String staSSID;
        String staPass;

        uint16_t ocppPort;
        String ocppHost;
        String ocppUrl;

        // String mdnsSTA;
        String serialID;

        // char adminPass[ACCOUNTMAXLENGTH];
        uint8_t initial;
    };

}; // namespace Configuration

Configuration::Config configuration;