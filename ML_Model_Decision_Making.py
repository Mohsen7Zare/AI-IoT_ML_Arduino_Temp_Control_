from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd


# Reading a labeled dataset
df = pd.read_csv('labeled_data.csv')
print(df.columns)

X = df[['Temperature', 'Humidity']]
y = df['Fan']

# Splitting data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# prediction
y_pred = model.predict(X_test)

# Model accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
