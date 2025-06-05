import pandas as pd
import matplotlib.pyplot as plt

# خواندن فایل CSV
df = pd.read_csv('sensor_data.csv')

# تبدیل ستون زمان به نوع datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# تنظیم اندازه نمودار
plt.figure(figsize=(12, 6))

# رسم دما
plt.plot(df['Timestamp'], df['Temperature'], label='Temperature (°C)', color='red', marker='o')

# رسم رطوبت
plt.plot(df['Timestamp'], df['Humidity'], label='Humidity (%)', color='blue', marker='x')

# تنظیمات نمودار
plt.title('Temperature and Humidity Over Time')
plt.xlabel('Time')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

# نمایش نمودار
plt.show()
