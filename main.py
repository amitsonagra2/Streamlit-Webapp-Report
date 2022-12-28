import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt
import calendar
from datetime import datetime
from streamlit_option_menu import option_menu
import database as db

# stramlit
# https://www.youtube.com/watch?v=3egaMfE9388&ab_channel=CodingIsFun
# render
# https://www.youtube.com/watch?v=4SO3CUWPYf0&ab_channel=CodingIsFun

# --------------------------------settings
Make = ['Honda','Toyota','Ford','Mazda','Chevrolet','Pontiac','Accura',
'Dodge','Mercury','Jaguar','Nisson','VW','Saab','Saturn','Porche','BMW','Mecedes','Ferrari','Lexus']
AccidentArea = ["Urban","Rural"]
# Sex
# 'MaritalStatus'
Fault = ["Policy Holder", "Third Party"]
# PolicyType = ["Sedan - All Perils","Sedan - Collision","Sedan - Liability","Sport - All Perils","Sport - Collision",
# "Sport - Liability","Utility - All Perils","Utility - Collision","Utility - Liability"]
VehicleCategory = ["Sedan","Sport","Utility"]
VehiclePrice = ["20000 to 29000","30000 to 39000","40000 to 59000","60000 to 69000","Less Than 20000","More Than 69000"]
Deductible = [300,400,500,700]
# 'Days_Policy_Claim',
PastNumberOfClaims = ["None","1","2 To 4","More Than 4"]
AgeOfVehicle = ["New","2 Years","3 Years","4 Years","5 Years","6 Years","7 Years","More Than 7"]
# AgeOfPolicyHolder = [""]
PoliceReportFiled = ["Yes","No"]
WitnessPresent = ["No","Yes"]
AgentType = ["Internal","External"]
NumberOfSuppliments = ["None","1 To 2","3 To 5","More Than 5"]
#  'AddressChange_Claim', 
NumberOfCars = ["1","2","3 To 4","5 To 8","More Than 8"]
BasePolicy = ["All Perils","Collision","Liability"]


page_title = "Vechicle Insurance Fraud Finder :umbrella_with_rain_drops:"
# page_icon = ":money:"
layout = "centered"


st.set_page_config(page_title=page_title, layout=layout)
st.title(page_title)

filler = "<p style='font-family: Arial'>Fill the below form to find out if your claim is eligible for insurance</p>"
st.markdown(filler, unsafe_allow_html=True)

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
# years = [datetime.today().year, datetime.today().year+1]
# months = list(calendar.month_name[1:])


# ------------------------------Navigation Menu
# selected = option_menu(menu_title=None,
#                         options=['Problem Statement', 'Solution Using ML'],
#                         icons=['bi bi-card-text','bi bi-robot'],
#                         orientation="horizontal")

# ------------------------------Input and Save periods
st.header(f"Enter your values :spiral_note_pad:")

with st.form(key="ml_form", clear_on_submit=True):
    
    st.selectbox("Make:", Make, key="k_Make")
    st.selectbox("Base Policy:", BasePolicy, key="k_BasePolicy")
    st.selectbox("Fault:", Fault, key="k_Fault")

    st.selectbox("Vehicle Category:", VehicleCategory, key="k_VehicleCategory")
    st.selectbox("Vehicle Price:", VehiclePrice, key="k_VehiclePrice")
    st.selectbox("Deductible Amount:", Deductible, key="k_Deductible")

    st.selectbox("Past Number Of Claims:", PastNumberOfClaims, key="k_PastNumberOfClaims")
    st.selectbox("Age Of Vehicle:", AgeOfVehicle, key="k_AgeOfVehicle")
    st.selectbox("Police Report Filed?:", PoliceReportFiled, key="k_PoliceReportFiled")
    
    st.selectbox("Witness Present?:", WitnessPresent, key="k_WitnessPresent")
    st.selectbox("Agent Type:", AgentType, key="k_AgentType")
    st.selectbox("Number Of Suppliments:", NumberOfSuppliments, key="k_NumberOfSuppliments")

    st.selectbox("Number Of Cars:", NumberOfCars, key="k_NumberOfCars")
    st.selectbox("Accident Area:", AccidentArea, key="k_AccidentArea")
    "---"

    placeholder_val = ''
    st.text_area('Comments', placeholder_val, height = 5, key = "k_Comments")

    submitted = st.form_submit_button("Save Data")
    if submitted:

        Make = st.session_state['k_Make']
        BasePolicy = st.session_state['k_BasePolicy']
        Fault = st.session_state['k_Fault']

        VehicleCategory = str(st.session_state["k_VehicleCategory"])
        VehiclePrice = str(st.session_state["k_VehiclePrice"])
        Deductible = (st.session_state["k_Deductible"])

        PastNumberOfClaims = str(st.session_state["k_PastNumberOfClaims"])
        AgeOfVehicle = str(st.session_state["k_AgeOfVehicle"])
        PoliceReportFiled = str(st.session_state["k_PoliceReportFiled"])

        WitnessPresent = str(st.session_state["k_WitnessPresent"])
        AgentType = str(st.session_state["k_AgentType"])
        NumberOfSuppliments = str(st.session_state["k_NumberOfSuppliments"])

        NumberOfCars = str(st.session_state["k_NumberOfCars"])
        AccidentArea = str(st.session_state["k_AccidentArea"])

        Comments = str(st.session_state["k_Comments"])
    
        # db.insert(period, comment)
        st.success("Data Processed!")

# testing
# st.write(st.session_state['k_Comments'])


cols = ['Make_Accura', 'Make_BMW', 'Make_Chevrolet', 'Make_Dodge',
       'Make_Ferrari', 'Make_Ford', 'Make_Honda', 'Make_Jaguar', 
       'Make_Lexus',
       'Make_Mazda', 'Make_Mecedes', 'Make_Mercury', 'Make_Nisson',
       'Make_Pontiac', 'Make_Porche', 'Make_Saab', 'Make_Saturn',
       'Make_Toyota', 'Make_VW', 'AccidentArea_Rural', 'AccidentArea_Urban',
       'Fault_Policy Holder', 'Fault_Third Party', 'VehicleCategory_Sedan', 'VehicleCategory_Sport', 
       'VehicleCategory_Utility',
       'VehiclePrice_20000 to 29000', 'VehiclePrice_30000 to 39000',
       'VehiclePrice_40000 to 59000', 'VehiclePrice_60000 to 69000',
       'VehiclePrice_less than 20000', 'VehiclePrice_more than 69000',
       'Deductible_300', 'Deductible_400', 'Deductible_500', 'Deductible_700',
       'PastNumberOfClaims_1', 'PastNumberOfClaims_2 to 4',
       'PastNumberOfClaims_more than 4', 'PastNumberOfClaims_none',
       'AgeOfVehicle_2 years', 'AgeOfVehicle_3 years', 'AgeOfVehicle_4 years',
       'AgeOfVehicle_5 years', 'AgeOfVehicle_6 years', 'AgeOfVehicle_7 years',
       'AgeOfVehicle_more than 7', 'AgeOfVehicle_new', 'PoliceReportFiled_No',
       'PoliceReportFiled_Yes', 'WitnessPresent_No', 'WitnessPresent_Yes',
       'AgentType_External', 'AgentType_Internal',
       'NumberOfSuppliments_1 to 2', 'NumberOfSuppliments_3 to 5',
       'NumberOfSuppliments_more than 5', 'NumberOfSuppliments_none',
       'NumberOfCars_1 vehicle', 'NumberOfCars_2 vehicles',
       'NumberOfCars_3 to 4', 'NumberOfCars_5 to 8',
       'NumberOfCars_more than 8', 'BasePolicy_All Perils',
       'BasePolicy_Collision', 'BasePolicy_Liability']

df_model = pd.DataFrame(columns=cols)
df_model.loc[0] = 66*[0]

df_model["Make_"+str(Make)] = 1
df_model["BasePolicy_"+str(BasePolicy)] = 1
df_model["Fault_"+str(Fault)] = 1

df_model["VehicleCategory_"+str(VehicleCategory)] = 1
df_model["VehiclePrice_"+str(VehiclePrice)] = 1
df_model["Deductible_"+str(Deductible)] = 1

df_model["PastNumberOfClaims_"+(str(PastNumberOfClaims)).lower()] = 1

df_model["AgeOfVehicle_"+str(AgeOfVehicle).lower()] = 1

df_model["PoliceReportFiled_"+str(PoliceReportFiled)] = 1

df_model["WitnessPresent_"+str(WitnessPresent)] = 1
df_model["AgentType_"+str(AgentType)] = 1


df_model["NumberOfSuppliments_"+str(NumberOfSuppliments).lower()] = 1

if NumberOfCars == "1":
    df_model["NumberOfCars_1 vehicle"] = 1
elif NumberOfCars == "2":
    df_model["NumberOfCars_2 vehicles"] = 1
else:
    df_model["NumberOfCars_"+str(NumberOfCars).lower()] = 1


df_model["AccidentArea_"+str(AccidentArea)] = 1

#testing
# df_model

import pickle
pkl = open("./Xgboost.pkl",'rb')
model = pickle.load(pkl)


import matplotlib.pyplot as plt
import xgboost



res = model.predict(df_model)
if res==0:
    st.text('Good news! Your claim will be processed by insurance company')
else: 
    st.text('Your claim will be Denied by insurance company')
    st.text('The below factors are contributing to the Denial')
    fig = xgboost.plot_importance(model,max_num_features=15)
    st.pyplot() 

