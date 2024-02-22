import pandas as pd
import plotly.express as px
import streamlit as st
import altair as al

from data import DataCleaner

#load the data and clean the data
df = pd.read_csv('vehicles_us.csv') 
df = DataCleaner.cleaned_df(df)


##Variables

unique_manufacturer = df['make'].unique()
unique_condition = df['condition'].unique()
listed_one_week = df[df['days_listed'] <= 7]
min_year,max_year = int(df[df['model_year'] > 0]['model_year'].min()), int(df['model_year'].max())

##Streamlit - Inventory Table

#headers
st.header('CarMin - Used Car Market')
st.write('The best used cars on the market!')

#selection box for manufacturers
selection = st.selectbox('Select a Manufacturer', unique_manufacturer)

#slider range
year_range = st.slider('Model Year Filter',value=(min_year,max_year),min_value=min_year,max_value=max_year)
actual_range = list(range(year_range[0],year_range[1]+1))

#recent days listed checkbox
recent_listings = st.checkbox('Show Cars Listed in the Last Week')

if recent_listings:
    displayed_df = listed_one_week[(listed_one_week.make == selection) & (listed_one_week.model_year.isin(actual_range))]
else:
    displayed_df = df[(df.make == selection) & (df.model_year.isin(actual_range))]

#change the order of the indexes
new_order = [13,2,1,8,0,3,6,4,5,7,9,10,11,12,14,15]
reordered_df = displayed_df.iloc[:,new_order]

#renaming dataframe columns to clean it up on the app
reordered_df.rename(columns={'make':'Make',
                             'model':'Model',
                             'model_year':'Model Year',
                             'price':'Price',
                             'condition':'Condition',
                             'odometer':'Odometer',
                             'cylinders':'Cylinders',
                             'fuel':'Engine Type',
                             'transmission':'Transmission',
                             'type':'Type',
                             'paint_color':'Paint Color',
                             'is_4wd':'4WD?',
                             'date_posted':'Post Date',
                             'day_listed':'Days Listed',
                             'year_range':'Era',
                             'age':'Car Age (Years)'},inplace=True)

#display the dataframe
st.dataframe(reordered_df.set_index(reordered_df.columns[0]).style.format({'Odometer':'{:,}',
                                                                           'Model Year':'{}',
                                                                           'Price':'{:,.2f}'}))

#headers for graphs
st.header('')

