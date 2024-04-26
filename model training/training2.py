import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load data from CSV file
data = pd.read_csv('cleaned_data2.csv')

# Split data into 
X = data.iloc[:, 6:].values  
y = data.iloc[:, :6].values 

# train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Prediction example (replace typing_speed_values with actual values)
typing_speed_values = np.array([[61.54375000000002,61.54375000000002,61.54375000000002]])  # Example typing speed values
predictions = model.predict(typing_speed_values)
print("Predicted Temperatures and Light Intensities:", predictions)

# save the model
joblib.dump(model, 'model2.joblib')