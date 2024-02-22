import pandas as pd
import plotly.express as px
import streamlit as st

from data import DataCleaner

#load the data and clean the data. Function for cleaning data located in /data/cleaned_data.py
df = pd.read_csv('vehicles_us.csv') 
df = DataCleaner.cleaned_df(df)


##Variables

unique_manufacturer = sorted(df['make'].unique())
unique_condition = sorted(df['condition'].unique())
listed_one_week = df[df['days_listed'] <= 7]
cheap_cars = df[df['price'] < 10000]
min_year,max_year = int(df[df['model_year'] > 0]['model_year'].min()), int(df['model_year'].max())

##Streamlit - Inventory Table

#headers
st.header('CarMin - Used Car Market')
st.markdown('##### The best used cars on the market!')
st.write('')
st.write('Filter our inventory by your preferred Make, Condition, and Model Year')

#selection box for manufacturers
selection = st.selectbox('Select a Manufacturer', unique_manufacturer,index=None)
selection_1 = st.selectbox('Select Condition', unique_condition,index=None)

#slider range
year_range = st.slider('Model Year Filter',value=(min_year,max_year),min_value=min_year,max_value=max_year)
actual_range = list(range(year_range[0],year_range[1]+1))

#recent days listed checkbox
recent_listings = st.checkbox('Show Cars Listed in the Last Week')

if recent_listings:
    displayed_df = listed_one_week[(listed_one_week.make == selection) & (listed_one_week.condition == selection_1) & (listed_one_week.model_year.isin(actual_range))]
else:
    displayed_df = df[(df.make == selection) & (df.condition == selection_1) & (df.model_year.isin(actual_range))]

#change the order of the indexes
new_order = [14,2,1,8,0,3,6,4,5,7,9,10,11,12,13,15]
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
                                                                           'Car Age (Years)':'{:}',
                                                                           'Price':'{:,.2f}'}))


##Streamlit - Histogram for Types of Cars by Manufacturer

#header
st.write('')
st.write('')
st.write('')
st.markdown('#### Compare Types of Cars Available by Manufacturer')

#create 2 select boxes for both manufacturers to be compared in the histogram
manufacturer_list1 = unique_manufacturer
manufacturer_list2 = unique_manufacturer

man_select_1 = st.selectbox('Select Manufacturer 1', unique_manufacturer,index=None)
man_select_2 = st.selectbox('Select Manufacturer 2', unique_manufacturer,index=None)

histo_df = df[(df['make'].isin([man_select_1,man_select_2]))]

#cheap cars checkbox
cheap_select = st.checkbox('Show Cars that cost under $10,000')

if cheap_select:
    histo_df = cheap_cars[(cheap_cars['make'].isin([man_select_1,man_select_2]))]
else:
    histo_df = df[(df['make'].isin([man_select_1,man_select_2]))]

#create histogram
fig1 = px.histogram(histo_df,
                    x='type',
                    color='make',
                    labels={'type':'Type'},                   
                    title='<b> Car Types by Manufacturer <b>',
                    barmode='overlay',
                    template='plotly_dark')


fig1.update_layout(yaxis_title='Amount in Inventory',height=700)

#show the histogram
st.plotly_chart(fig1)


##Streamlit - Scatterplot for Mileage vs Price

#header
st.write('')
st.write('')
st.write('')
st.markdown('#### Mileage vs. Price')


#make the scatterplot
fig2 = px.scatter(df[df['age'].notna()],
                  x='odometer',
                  y='price',
                  color='age',
                  hover_data={'odometer': ':,', 'price': ':,.2f', 'age': ':'},
                  labels={'odometer':'Odometer Reading','price':'Price'},
                  template='plotly_dark')

fig2.update_xaxes(range=[0, 200000])
fig2.update_yaxes(range=[0, 75000])
fig2.update_layout(height=900,width=1100)

#show the plot
st.plotly_chart(fig2)
