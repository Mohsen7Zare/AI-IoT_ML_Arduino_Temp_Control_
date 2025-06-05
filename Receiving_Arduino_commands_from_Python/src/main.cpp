#include <Arduino.h>

#include <Wire.h>
#include <SHTSensor.h>

SHTSensor sht;
int fanPin = 7;

void setup()
{
    Serial.begin(9600);
    Wire.begin();
    pinMode(fanPin, OUTPUT);

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

        // Sending data to Python
        Serial.print(temp);
        Serial.print(",");
        Serial.println(hum);
    }

    // Checking receiving commands from Python
    if (Serial.available())
    {
        char command = Serial.read();
        if (command == '1')
        {
            digitalWrite(fanPin, HIGH);
        }
        else if (command == '0')
        {
            digitalWrite(fanPin, LOW);
        }
    }

    delay(2000);
}