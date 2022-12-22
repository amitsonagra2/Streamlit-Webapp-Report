import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt
import calendar
from datetime import datetime
from streamlit_option_menu import option_menu
import database as db



# --------------------------------settings
income = ["Salary", "Blog", "Other"]
expenses = ["Rent", "Utilities", "Car"]
page_title = "Income and Expense Tracker"
# page_icon = ":money:"
layout = "centered"


st.set_page_config(page_title=page_title, layout=layout)
st.title(page_title)
st.text('Use this pretrained model to get prediction for your data')

# --------------------------Hide streamlit styles
hide_st_style = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# ------------------------------Drop down values
years = [datetime.today().year, datetime.today().year+1]
months = list(calendar.month_name[1:])


# ------------------------------Navigation Menu
selected = option_menu(menu_title=None,
                        options=['Problem Statement', 'Solution Using ML'],
                        icons=['bi bi-card-text','bi bi-robot'],
                        orientation="horizontal")

# ------------------------------Input and Save periods
st.header(f"Enter your values")

with st.form("entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    col1.selectbox("Select Month:", months, key="month")
    col2.selectbox("Select Year:", years, key="year")

    "---"
    with st.expander("Income"):
        for income in income:
            st.number_input(f"{income}:", min_value=0, format="%i", key=income)

    "---"

    submitted = st.form_submit_button("Save Data")
    if submitted:
        period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
        comment = str(st.session_state["comment"])
        db.insert(period, comment)
        # st.success("Data Saved")



# image = Image.open('./logo.jpg')

# st.image(image, use_column_width = True)


placeholder_val = 'Please Enter Your Feedback, We Take It Very Seriously Here'

st.text_area('Comments', placeholder_val, height = 5)





