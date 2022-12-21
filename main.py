import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt

image = Image.open('./logo.jpg')

st.image(image, use_column_width = True)


header = st.container()

features = st.container()

with header:
    st.title('Predicting the sentiments of the user reviews for hotels')
    st.text('Use this pretrained model to get prediction for your data')

placeholder_val = 'sample@gmail.com'

st.text_area('Email', placeholder_val, height = 5)

