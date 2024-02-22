import pandas as pd
import plotly.express as px
import streamlit as st
import altair as al

from data import DataCleaner

#load the data and clean the data
df = pd.read_csv('vehicles_us.csv') 
df = DataCleaner.cleaned_df(df)

'''
Variables
'''

unique_manufacturer = df['make'].unique()
unique_condition = df['condition'].unique()
listed_one_week = df[df['days_listed'] <= 7]

#assign min and max year to functions for the year slider on the app
min_year,max_year = int(df['model_year'].min()), int(df['model_year'].max())

'''
Streamlit
'''

#headers
st.header('CarMin - Used Car Market')
st.write('The best used cars on the market!')

#Sselection box for manufacturers
selection = st.selectbox('Select a Manufacturer', unique_manufacturer)

#slider range
year_range = st.slider('Model Year Filter',value=(min_year.max_year),min_value=min_year,max_value=max_year)
actual_range = list(range(year_range[0],year_range[1]+1))

#recent days listed checkbox
recent_listings = st.checkbox('Show Cars Listed in the Last Week')

if recent_listings:
    displayed_df = listed_one_week[(listed_one_week.make == selection) & (listed_one_week.model_year.isin(actual_range))]
else:
    displayed_df = df[(df.make == selection) & (df.model_year.isin(actual_range))]

st.table(displayed_df)
