import pandas as pd
import streamlit as st


st.title("TZSOULCAP")
st.header("This is Pizza Hut locations in US")



data = pd.read_csv("pizza_hut_locations.csv")
data = data.dropna(how='any', subset=['latitude', 'longitude'])
data.rename({'latitude':'lat'}, axis='columns', inplace=True)
data.rename({'longitude':'lon'}, axis='columns', inplace=True)

# locations = data[['latitude', 'longitude']]

types = pd.DataFrame(data.groupby('type')['type'])
types.rename({0:'types'}, axis='columns', inplace=True)
types = types.append({'types':'All'}, ignore_index=True).sort_values(['types']).reset_index().loc[:, ['types']]

st.sidebar.subheader('input')
st.sidebar.selectbox('Types', types, key='type')
st.sidebar.write(f"#### You selected {st.session_state['type']}")

if st.session_state['type'] == 'All':
    locations = data.loc[:, ['lat', 'lon']].reset_index(drop=True)
else:
    locations = data.query(f"type == '{st.session_state['type']}'").loc[:, ['lat', 'lon']].reset_index(drop=True)
st.sidebar.write('example data')
st.sidebar.table(locations[:10])
st.sidebar.table(types.loc[:, 'types'])



# locations.rename({'longitude':'lon'}, axis='columns', inplace=True)
# locations.rename({'latitude':'lat'}, axis='columns', inplace=True)

# new_locations = locations.dropna()


# lat = new_locations['lat']
# lon = new_locations['lon']
# locate = list(map(lambda x, y: [x, y], lat, lon))
# x = pd.DataFrame(locate, columns=['lat', 'lon'])

st.map(locations)
# st.write(data)