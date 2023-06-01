size_t sizeofConfiguration(const Configuration::Config *config);
template <typename T>
void loadConfigurationValue(const char *filename, T &configuration, bool &havingFlag);
template <typename T>
void saveConfigurationValue(const char *filename, const T &configuration, const bool &havingFlag);
template <typename T>
void loadDetailsOCPPValue(const char *filename, T &details, bool &havingFlag);
template <typename T>
void saveDetailsOCPPValue(const char *filename, const T &details, const bool &havingFlag);

void allLoading(void);

size_t sizeofConfiguration(const Configuration::Config *config)
{
    size_t size = 0;

    // iterate over members of Config struct and add up their sizes
    for (const auto &member : std::initializer_list<const String *>{
             &config->firmware.serial,
             &config->firmware.vendor,
             &config->firmware.firmwareVersion,
             &config->general.user,
             &config->general.pass,
             &config->general.dns,
             &config->station.ssid,
             &config->station.pass,
             &config->station.hostname,
             &config->accesspoint.ssid,
             &config->accesspoint.pass})
    {
        size += member->length(); // add 1 for null terminator
        size += 14;
    }

    // calculate length of non-string variables
    size += String(config->firmware.initial).length();
    size += (1 * 10) + 10;
    return size;
}

template <typename T>
void loadConfigurationValue(const char *filename, T &configuration, bool &havingFlag)
{
    auto doc = barryConfig.readJSONFromFile(filename, 12, havingFlag);

    configuration.firmware.initial = (*doc)["initial"] | 1;
    configuration.firmware.vendor = (*doc)["vendor"] | VENDOR;
    configuration.firmware.serial = (*doc)["serial"] | "FFFFFFFF";
    configuration.firmware.firmwareVersion = (*doc)["firmware_ver"] | FIRMWAREVERSION;

    configuration.general.dns = (*doc)["dns"] | "durainbill";
    configuration.general.user = (*doc)["user"] | "admin";
    configuration.general.pass = (*doc)["pass"] | "admin";

    configuration.station.ssid = (*doc)["ssid_sta"] | "durainSTA";
    configuration.station.pass = (*doc)["pass_sta"] | "12345678";
    configuration.station.hostname = (*doc)["hostname"] | "durainbill";

    configuration.accesspoint.ssid = (*doc)["ssid_ap"] | "durianAP";
    configuration.accesspoint.pass = (*doc)["pass_ap"] | "";
}
template <typename T>
void saveConfigurationValue(const char *filename, const T &configuration, const bool &havingFlag)
{
    File file = (!havingFlag) ? SPIFFS.open(filename, "a") : SPIFFS.open(filename, FILE_WRITE);

    auto doc = std::unique_ptr<DynamicJsonDocument>(new DynamicJsonDocument(JSON_OBJECT_SIZE(12) + (uint32_t)(sizeofConfiguration(&configuration) * 1.25)));
    JsonObject payload = doc->to<JsonObject>();

    payload["initial"] = configuration.firmware.initial;
    payload["vendor"] = configuration.firmware.vendor;
    payload["serial"] = configuration.firmware.serial;
    payload["firmware_ver"] = configuration.firmware.firmwareVersion;

    payload["dns"] = configuration.general.dns;
    payload["user"] = configuration.general.user;
    payload["pass"] = configuration.general.pass;

    payload["ssid_ap"] = configuration.accesspoint.ssid;
    payload["pass_ap"] = configuration.accesspoint.pass;

    payload["ssid_sta"] = configuration.station.ssid;
    payload["pass_sta"] = configuration.station.pass;
    payload["hostname"] = configuration.station.hostname;

    if (serializeJson(*doc, file) == 0)
    {
        debugln(F("Failed to write to Configuration"));
    }

    file.close();
}

void allLoading(void)
{
    barryConfig.loadAndSave(loadConfigurationValue<Configuration::Config>, saveConfigurationValue<Configuration::Config>, jsonConfiguration, configuration, hasConfiguration);
}
