import folium
import pandas as pd


partnerships_data = pd.read_csv('partnership_data.csv')
partnerships_map = folium.Map(location=[0, 0], zoom_start=2)

for index, row in partnerships_data.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']],
                  popup=row['Partner']).add_to(partnerships_map)

partnerships_map.save('partnerships_map.html')

