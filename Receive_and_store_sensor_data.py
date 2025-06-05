import serial
import pandas as pd
from datetime import datetime

# ⚠ Enter your appropriate port, for example COM5 in Windows.
ser = serial.Serial('COM5', 9600)
data = []

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            parts = line.split(',')
            if len(parts) == 2:
                temp = float(parts[0])
                hum = float(parts[1])
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{timestamp}] Temp: {temp} °C | Hum: {hum} %")
                data.append([timestamp, temp, hum])

except KeyboardInterrupt:
    print("\nStopping... Saving to CSV.")
    df = pd.DataFrame(data, columns=['Timestamp', 'Temperature', 'Humidity'])
    df.to_csv('sensor_data.csv', index=False)
    print("Data saved to sensor_data.csv")
