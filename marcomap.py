import pandas as pd
import numpy as np
import pydeck as pdk
import streamlit as st
import pandas

cd = pandas.read_csv('hypdatacoord.csv', header='infer')
cleaned = cd[cd['dem_coordinates'].notna()]
df = cleaned
df['lat'] = df.dem_coordinates.str.split(',', expand = True)[0]
df['lon'] = df.dem_coordinates.str.split(',', expand = True)[1]
df['lat'] = df.lat.str.strip()
df['lon'] = df.lon.str.strip()
df = df[df['lat'].notna()]
df = df[df['lon'].notna()]
df["lat"] = [float(i) for i in df["lat"]]
df["lon"] = [float(i) for i in df["lon"]]
chart_data = df[['lat', 'lon']]

firstSeries = df.loc[df['erad_an'] == 'Yes']
secondSeries = df.loc[df['erad_an'] == "No"]
erad = firstSeries[['lat', 'lon', 'erad_an']]
notErad = secondSeries[['lat', 'lon', 'erad_an']]
print(erad.head())
print(notErad.head())


st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=42.204700,
        longitude= -71.002490,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'ScatterplotLayer',
           data=erad,
           get_position='[lon, lat]',
            get_color='[100, 30, 0, 160]',
            get_radius=200,

        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=notErad,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
