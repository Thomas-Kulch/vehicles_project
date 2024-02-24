import pandas as pd
from data import functions

class DataCleaner:
    def __init__(self,data):
        self.data = data

    def cleaned_df(self):

        cleaned_df = self

        #add age column. Doing this before filling the missing age values so the NaN model_year's aren't included in the calculation and the visualizations wont be affected.
        cleaned_df['age'] = 2024 - cleaned_df['model_year']

        #Fix data types and missing values
        #price
        cleaned_df['price'] = cleaned_df['price'].astype(float)
        #is_4wd
        cleaned_df['is_4wd'] = cleaned_df['is_4wd'].fillna(0).astype(int)
        #odometer
        cleaned_df['odometer'] = cleaned_df['odometer'].fillna(0).astype(int)
        #model_year values
        cleaned_df['model_year'] = cleaned_df['model_year'].fillna(0).astype(int)
        #cylinders
        cleaned_df = functions.cylinder_estimation(cleaned_df)
        #filling the remaining missing values with average cylinder by car type
        cleaned_df['cylinders'] = cleaned_df['cylinders'].fillna(cleaned_df['type'].apply(functions.cyl)).astype(int)

        #Add make column from model
        #split the column up into 5 columns by spaces
        cleaned_df[['make','model','filler','filler1','filler2']] = cleaned_df['model'].str.split(' ',expand=True)

        #combine the last 4 columns back into the model column
        cleaned_df['model'] = cleaned_df['model'] + ' ' + cleaned_df['filler'].fillna('') + ' ' + cleaned_df['filler1'].fillna('') + ' ' + cleaned_df['filler2'].fillna('')

        #drop the filler columns
        cleaned_df.drop(['filler','filler1','filler2'],axis=1,inplace=True)

        #add the year_range column
        cleaned_df['year_range'] = cleaned_df['model_year'].apply(functions.year_range)

        #add condition column
        cleaned_df['condition'] = cleaned_df['odometer'].apply(functions.condition)

        #sort and drop duplicates
        #sort the records by the records with less NaN values to be on top
        df_sorted = cleaned_df.iloc[cleaned_df.isnull().sum(axis=1).argsort()]

        #drop duplicates based on the columns model, price, model_year,odometer which keeping the first instance
        cleaned_df_no_dups = df_sorted.drop_duplicates(subset=['model','price','model_year','cylinders','odometer','fuel','transmission','type','is_4wd','paint_color'],keep='first')

        
        return cleaned_df_no_dups

