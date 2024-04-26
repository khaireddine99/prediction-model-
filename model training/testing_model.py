import pandas as pd
import joblib

# Load the saved model
model = joblib.load('model.joblib')

# Load the data you want to predict on
new_data = pd.DataFrame([[26.69335283972712,25.149596321166023,23.109346717025737,1212.0709012683844,943.7019985052672,599.2714935012543]], columns=['Temperature1', 'Temperature2', 'Temperature3', 'Light Intensity1', 'Light Intensity2', 'Light Intensity3'])

# Make predictions
predictions = model.predict(new_data)

# Print the predictions
print("Predicted Typing Speeds:")
for i, pred in enumerate(predictions):
    print(f"Typing Speeds: {pred}")