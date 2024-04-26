import pandas as pd
import joblib


# function that gets input and return predicted data
def get_predictions(temp1, temp2, temp3, light1, light2, light3):
    model = joblib.load('model.joblib')
    new_data = pd.DataFrame([[temp1, temp2, temp3, light1, light2, light3]], columns=['Temperature1', 'Temperature2', 'Temperature3', 'Light Intensity1', 'Light Intensity2', 'Light Intensity3'])
    predictions = model.predict(new_data)
    print(predictions)
    
    return predictions


if __name__ == '__main__':
    get_predictions(26.819177526021974,25.34998381298152,23.346747519245124,1123.2353146084547,747.6986240736064,805.9513134817446)