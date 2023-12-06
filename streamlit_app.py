import streamlit as st
import subprocess

st.header('🎈 R x Python Streamlit App')

st.sidebar.markdown('''
# About
Testing R di Streamlit

R packages used:

- `readxl`
- `cluster`
- `factoextra`
- `fpc`
''')

st.subheader('1. Printing text in R')
with st.expander('See code'):
    code1 = '''library(readxl)
library(cluster)
library(factoextra)
library(fpc)

# Read the data file
Data_Per_Kecamatan_Bandar_Lampung <- read_excel("datatest.xlsx")

# Scale the data
z <- scale(Data_Per_Kecamatan_Bandar_Lampung[,-1])

# Calculate Euclidean distance
distance <- dist(z)
distance
    '''
    st.code(code1, language='r')
process1 = subprocess.Popen(["Rscript", "testing.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.write(result1)
