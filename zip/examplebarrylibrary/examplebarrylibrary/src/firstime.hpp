void textToHex(const char *input, char *output);
String createSerialNumber(String const &prefix);
void firstTimeSetting(uint8_t &check);

void textToHex(const char *input, char *output)
{
    register int loop;
    register int i;

    i = 0;
    loop = 0;

    while (input[loop] != '\0')
    {
        sprintf((char *)(output + i), "%02X", input[loop]);
        loop += 1;
        i += 2;
    }
    // insert NULL at the end of the output string
    output[i++] = '\0';
}
String createSerialNumber(String const &prefix)
{
    std::unique_ptr<String> result(new String(prefix)); // Initialize result with prefix
    register uint32_t chipId;
    register uint32_t counter;
    chipId = 0;
    for (counter = 0; counter < 17; counter = counter + 8)
    {
        chipId |= ((ESP.getEfuseMac() >> (40 - counter)) & 0xff) << counter;
    }
    *result += chipId;

    register uint32_t len;
    len = result->length();
    std::unique_ptr<char[]> hexStr(new char[(len * 2) + 1]);
    textToHex(result->c_str(), hexStr.get()); // Convert result to hex, not prefix

    *result = hexStr.get();
    return *result;
}
void firstTimeSetting(uint8_t &check)
{
    if (check != 1)
    {
        return;
    }

    configuration.firmware.serial = createSerialNumber("DURIAN");

    check = 0;

    saveConfigurationValue<Configuration::Config>(jsonConfiguration, configuration, hasConfiguration);

    delay(100);
    WiFi.disconnect(true);
    ESP.restart();
}
