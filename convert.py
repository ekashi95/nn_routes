import pandas as pd
import json

df = pd.read_excel('data.xlsx')

df = df.replace({pd.NA: None, float('nan'): None})
df = df.where(pd.notnull(df), None) 

data = []
for _, row in df.iterrows():
    data.append({
        "lat": float(row['coords'].split(', ')[0]),
        "lng": float(row['coords'].split(', ')[1]),
        "type": row['type'],
        "name": row['name'],
        "description": row['descr']
    })

with open('map_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

print("Файл map_data.json успешно создан")