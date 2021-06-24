import csv
import pandas as pd

data1 = []
data2 = []

with open(r'Projects\C129\venv\NewSolarUpdated.csv', 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)

    for row in csvreader:
        data1.append(row)


with open(r'Projects\C127\venv\data.csv', 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)

    for row in csvreader:
        data2.append(row)

headers1 = data1[0]
star_data1 = data1[1:]

headers2 = data2[0]
star_data2 = data2[1:]

headers = headers1 + headers2
star_data = []

for index in range(len(star_data1)):
    star_data.append(star_data1[index] + star_data2[index])

star_data_df = pd.DataFrame(star_data, columns=headers)

star_data_df.to_csv(r'Projects\C129\venv\FinalMerged.csv', index=False)
