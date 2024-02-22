import pandas as pd
import plotly.express as px
import streamlit as st
import altair as al

from data import DataCleaner

df = pd.read_csv('vehicles_us.csv') 
df = DataCleaner.cleaned_df(df)
print(df.sample(5))