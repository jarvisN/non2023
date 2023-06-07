#include "HX711.h"

float calibration_factor =3032.00; //need new value
#define zero_factor 8296081 //need new value
#define DOUT  23
#define CLK   22
#define DEC_POINT  2

float offset=0;
float get_units_kg();

HX711 scale(DOUT, CLK);

void setup() 
{
  Serial.begin(115200);
  Serial.println("Load Cell");
  scale.set_scale(calibration_factor); 
  scale.set_offset(zero_factor);   
}
void loop() 
{ 
  Serial.print("Reading: ");
  String data = String(get_units_kg()+offset, DEC_POINT);
  Serial.print(data);
  Serial.println(" kg");
}
float get_units_kg()
{
  return(scale.get_units()*0.453592);
}