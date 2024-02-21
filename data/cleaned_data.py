import pandas as pd
from data import functions

class DataCleaner:
    def __init__(self,df):
        self.df = df

    def cleaned_df(self):

        cleaned_df = self
        
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
        cleaned_df['cylinders'] = cleaned_df['cylinders'].fillna(cleaned_df['type'].apply(functions.cyl)).astype(int)

        #Add make column from model
        #split the column up into 5 columns by spaces
        cleaned_df[['make','model','filler','filler1','filler2']] = cleaned_df['model'].str.split(' ',expand=True)

        #combine the last 4 columns back into the model column
        cleaned_df['model'] = cleaned_df['model'] + ' ' + cleaned_df['filler'].fillna('') + ' ' + cleaned_df['filler1'].fillna('') + ' ' + cleaned_df['filler2'].fillna('')

        #drop the filler columns
        cleaned_df.drop(['filler','filler1','filler2'],axis=1,inplace=True)
        
        return cleaned_df

