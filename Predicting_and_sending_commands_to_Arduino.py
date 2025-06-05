import serial
import pandas as pd
import joblib  # To load the model
from datetime import datetime

# Load saved model
model = joblib.load('prediction_model.pkl')  # Replace with the actual file name

# Connecting to Arduino serial port
ser = serial.Serial('COM5', 9600)  # The appropriate port for your system

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            parts = line.split(',')
            if len(parts) == 2:
                temp = float(parts[0])
                hum = float(parts[1])
                print(f"Received: Temp={temp}, Hum={hum}")

                # predicting
                prediction = model.predict([[temp, hum]])[0]
                print(f"Decision: {'Fan ON' if prediction == 1 else 'Fan OFF'}")

                # Sending commands to Arduino
                ser.write(str(prediction).encode())

except KeyboardInterrupt:
    print("Stopped.")
    ser.close()
