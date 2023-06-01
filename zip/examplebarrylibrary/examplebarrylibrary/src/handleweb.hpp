void notFound(AsyncWebServerRequest *request);
void webserverMangement(void);

void notFound(AsyncWebServerRequest *request)
{
    request->send(404, "text/plain", "Page Not found");
}
void webserverMangement()
{
    server = new AsyncWebServer(80);

    server->on("/rest/lux", HTTP_GET, [](AsyncWebServerRequest *request)
               {
        uint8_t lux = 123;
        auto jsonBuffer = std::unique_ptr<DynamicJsonDocument>(new DynamicJsonDocument(
            JSON_OBJECT_SIZE(1) + strlen(String(lux).c_str()) + 1));

        JsonObject root = jsonBuffer->to<JsonObject>();
  
        root["lux"] = lux;

        std::unique_ptr<String> dataSend(new String());

        if (serializeJson(*jsonBuffer, *dataSend) == 0)
    {
        debugln(F("Failed to pack LUX"));
    }
    request->send_P(201, "application/json", dataSend->c_str()); });

    server->onNotFound(notFound);
    server->begin();
}