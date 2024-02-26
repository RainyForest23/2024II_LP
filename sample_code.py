import streamlit as st
import gspread
from gspread_dataframe import get_as_dataframe

st.title("학습원리팀 Test")
st.markdown("2024.02.26")

url = "https://docs.google.com/spreadsheets/d/1kpVoNTRJilVxY9BALquZy3ErbBDdv8uN8EMv6n2Hd7E/edit#gid=1235239897"

# Specify the path to your service account JSON file
service_account_file = "/Users/rainyforest/Desktop/SDIJ_FSRT/2024II_학습원리/lib/learningprinciple-75fb3f0829c7.json"

# Authenticate with Google Sheets using the service account JSON file
gc = gspread.service_account(filename=service_account_file)
sh = gc.open_by_url(url)

# Reading the data from the specified worksheet
worksheet_name = "PERCENT(test)"

# Get the worksheet by title
worksheet = sh.worksheet(worksheet_name)

# Convert worksheet data to DataFrame
exist_data = get_as_dataframe(worksheet)

# Displaying the dataframe
st.dataframe(exist_data)
