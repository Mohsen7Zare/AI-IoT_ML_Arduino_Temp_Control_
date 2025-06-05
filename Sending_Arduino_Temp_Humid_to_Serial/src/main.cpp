#include <Arduino.h>

#include <Wire.h>
#include <SHTSensor.h>

SHTSensor sht;

void setup()
{
  Serial.begin(9600);
  Wire.begin();

  if (!sht.init())
  {
    Serial.println("SHT Init failed!");
    while (1)
      ;
  }
}

void loop()
{
  if (sht.readSample())
  {
    float temp = sht.getTemperature();
    float hum = sht.getHumidity();

    // فرمت ارسال: 27.38,35.24
    Serial.print(temp);
    Serial.print(",");
    Serial.println(hum);
  }
  delay(2000);
}
