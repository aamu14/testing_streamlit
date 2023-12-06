import streamlit as st
import subprocess
import pandas as pd

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

st.markdown("""
            **Dataset yang digunakan terdiri dari data kecamatan, data luas daerah, dan data kependidikan yang terbagi menjadi 3, yaitu:**  
            1. Jumlah Guru Tingkat TK hingga SMA sederajat
            2. Jumlah Murid Tingkat TK hingga SMA sederajat
            3. Jumlah Sekolah Tingkat TK hinga SMA sederajat
            """)

# Read the Excel file into a DataFrame
data = pd.read_csv("datatest.csv")
st.dataframe(data, height=300)

st.markdown("""
            **Berikut adalah statistika deskripsi dari dataset yang digunakan:**  
            """)
data_summary =pd.read_csv("summary.csv")
st.dataframe(data_summary, height=300)

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




    #st.code(code1, language='r')
#process1 = subprocess.Popen(["Rscript", "bagian 1 kmeans.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#result1 = process1.communicate()
#st.dataframe(result1, hide_index=True)
