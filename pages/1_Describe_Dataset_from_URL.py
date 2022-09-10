import pandas as pd
import streamlit as st

st.title('Show Describe Dataset from URL')
st.header('Output')

st.sidebar.header('input')
st.sidebar.text_input('URL', key='url')
st.warning(f"Dataset from {st.session_state.url}" if st.session_state.url != '' else 'Please enter dataset url')

data = pd.read_csv(st.session_state.url)
st.dataframe(data)

option_gb = data.columns.values
option_gb = pd.DataFrame(option_gb).append({0:'-'}, ignore_index=True).sort_values([0])

st.sidebar.selectbox('Group by', option_gb, key='groupby')
st.sidebar.write(st.session_state.groupby)
st.dataframe(option_gb)