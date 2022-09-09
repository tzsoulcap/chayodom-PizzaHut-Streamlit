import pandas as pd
import streamlit as st


st.title("TZSOULCAP")
st.header("This is Pizza Hut locations in US")

data = pd.read_csv("pizza_hut_locations.csv")
locations = data[['latitude', 'longitude']]

print(data.dtypes)
locations.rename({'longitude':'lon'}, axis='columns', inplace=True)
locations.rename({'latitude':'lat'}, axis='columns', inplace=True)

new_locations = locations.dropna()


lat = new_locations['lat']
lon = new_locations['lon']
locate = list(map(lambda x, y: [x, y], lat, lon))
x = pd.DataFrame(locate, columns=['lat', 'lon'])

st.map(x)
st.write(data)