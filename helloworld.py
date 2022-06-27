import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px

# core packages
import streamlit as st
import streamlit.components.v1 as stc

# additional packages
# Load EDA packages
import pandas as pd

# Data Viz Packages

import matplotlib.pyplot as plt
import matplotlib


# text cleaning packages
import neattext as nt
import neattext.functions as nfx


# utils
from collections import Counter
from wordcloud import WordCloud
import base64
import time
import re

'''
# Club and Nationality App

This very simple webapp allows you to select and visualize players from certain clubs and certain nationalities.
'''
df = st.cache(pd.read_csv)("football_data.csv")

clubs = st.sidebar.multiselect('Show Player for clubs?', df['Club'].unique())
nationalities = st.sidebar.multiselect('Show Player from Nationalities?', df['Nationality'].unique())

new_df = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(nationalities))]
st.write(new_df)

# Create distplot with custom bin_size
fig = px.scatter(new_df, x ='Overall',y='Age',color='Name')

'''
### Here is a simple chart between player age and overall
'''

st.plotly_chart(fig)
