import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1kpVoNTRJilVxY9BALquZy3ErbBDdv8uN8EMv6n2Hd7E"

# Creating a connection
conn = st.connection("gsheet", type=GSheetsConnection)

# Reading the data from the specified worksheet
data = conn.read(worksheet="RESULT")

# Displaying the dataframe
st.dataframe(data)
