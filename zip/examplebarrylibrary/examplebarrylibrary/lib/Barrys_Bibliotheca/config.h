#define LINE 1
#define RTCPCB 0 // 0 1307, 1 3231
#define WIFI_ARDUINO_EVENT 1 // 0 = system, 1 = arduino

// #define DEBUG 0 // 0 = NO-DEBUG, 1 = DEBUG
// #define LITTLE 1
#define swDelay(x) vTaskDelay(x / portTICK_PERIOD_MS)


#define PINHIGH 0x1 // 0x1 = high, 0x0 = low
#define PINLOW 0x0 // 0x1 = high, 0x0 = low

#define POWERPIN 32
#define RFIDPIN 15
#define BUZZPIN 33

#define LITTLE 1