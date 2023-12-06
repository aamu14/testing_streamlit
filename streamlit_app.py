import streamlit as st
import subprocess

st.header('🎈 R x Python Streamlit App')

st.sidebar.markdown('''
# About
This demo shows the use of R in a Streamlit App by showcasing 3 example use cases.

The R code for all 3 examples is rendered on-the-fly in this app.

R packages used:

- `readxl`
- `cluster`
- `factoextra`
- `clusterSim`
- `fpc`
''')

st.subheader('1. Printing text in R')
with st.expander('See code'):
    code3 = '''library(readxl)
    library(cluster)
    library(factoextra)
    library(clusterSim)
    library(fpc)
    '''
    st.code(code1, language='r')

st.code(code3, language='R')
process3 = subprocess.Popen(["Rscript", "lipinski.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result3 = process3.communicate())
