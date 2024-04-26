import pandas as pd
import joblib

# load the saved model
model = joblib.load('model2.joblib')

# load the data you want
new_data = pd.DataFrame([[61.54375000000002,61.54375000000002,61.54375000000002]], columns=['Typing Speed1 (words per minute)','Typing Speed2 (words per minute)','Typing Speed3 (words per minute)'])

# make predictions
predictions = model.predict(new_data)

# print predictions
print("predicted optimal temperature and lighting:")

for i, pred in enumerate(predictions):
    print(f'optimal temperature and lighting: {pred}')