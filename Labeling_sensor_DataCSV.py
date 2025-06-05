import pandas as pd

df = pd.read_csv('sensor_data.csv')

# Simple rule for labeling control data
df['Fan'] = ((df['Temperature'] > 30) | (df['Humidity'] > 60)).astype(int)

# Save new dataset
df.to_csv('labeled_data.csv', index=False)

print(df.head())
