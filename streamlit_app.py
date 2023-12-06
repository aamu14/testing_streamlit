import streamlit as st
import subprocess
import pandas as pd
import openpyxl
st.header('🎈 R x Python Streamlit App')

st.sidebar.markdown('''
# About
Testing R di Streamlit

R packages used:

- `readxl`
- `cluster`
- `factoextra`
- `fpc`
- `clusterSim`
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




# Read the Excel file into a DataFrame
file_path = 'datatest.xlsx'
df = pd.read_excel(file_path)

# Display summary statistics
summary = df.describe()

st.dataframe(df, hide_index=True)
st.write(summary)


    #st.code(code1, language='r')
#process1 = subprocess.Popen(["Rscript", "bagian 1 kmeans.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#result1 = process1.communicate()
#st.dataframe(result1, hide_index=True)
