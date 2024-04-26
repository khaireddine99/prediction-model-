import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import joblib

# load the dataset
data = pd.read_csv('cleaned_data2.csv')

# Split into features and target variables
features = data[['Temperature1', 'Temperature2', 'Temperature3', 
                 'Light Intensity1', 'Light Intensity2', 'Light Intensity3']]

target = data[['Typing Speed1 (words per minute)', 
               'Typing Speed2 (words per minute)', 
               'Typing Speed3 (words per minute)']]

# train the model
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.1, random_state=42)
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# prediction test
new_data = pd.DataFrame([[22.5,22.5,22.5,200.0,200.0,200.0]], columns=features.columns)  # Example new data
prediction = model.predict(new_data)
print("Predicted Typing Speed:", prediction)

# save the model 
joblib.dump(model, 'decision_tree_model.joblib')
