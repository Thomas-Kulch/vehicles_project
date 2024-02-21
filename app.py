import pandas as pd
import plotly.express as px
import streamlit as st
import altair as al
from data import DataCleaner

df = pd.read_csv(r'C:\Users\trkjr\OneDrive\Code_Learning_Master\vehicles_project\vehicles_us.csv') 

df = DataCleaner.cleaned_df(df)

print(df)