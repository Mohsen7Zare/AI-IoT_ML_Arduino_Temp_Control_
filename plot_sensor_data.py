import pandas as pd
import matplotlib.pyplot as plt

# Reading CSV file
df = pd.read_csv('sensor_data.csv')

# Convert time column to datetime type
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Adjust plot size
plt.figure(figsize=(12, 6))

# Drawing a temperature graph
plt.plot(df['Timestamp'], df['Temperature'], label='Temperature (°C)', color='red', marker='o')

# Drawing a humidity plot
plt.plot(df['Timestamp'], df['Humidity'], label='Humidity (%)', color='blue', marker='x')

# plot settings
plt.title('Temperature and Humidity Over Time')
plt.xlabel('Time')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show plot
plt.show()
