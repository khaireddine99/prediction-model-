import pandas as pd

file = pd.read_csv("training_dataset_combined.csv")
selected_colums = file[['Temperature1', 'Temperature2', 'Temperature3', 'Light Intensity1', 'Light Intensity2', 'Light Intensity3',
                     'Typing Speed1 (words per minute)', 'Typing Speed2 (words per minute)', 'Typing Speed3 (words per minute)']]

selected_colums.to_csv("cleaned_data1.csv", index=False)