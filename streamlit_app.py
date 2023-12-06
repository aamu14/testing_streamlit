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
    code1 = '''library(readxl)
    library(cluster)
    library(factoextra)
    library(clusterSim)
    library(fpc)
    '''
    st.code(code1, language='r')

# Adjust the path to your R script file
process1 = subprocess.Popen(["Rscript", "testing.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process1.communicate()

if stderr:
    st.error(f"Error: {stderr.decode()}")
else:
    st.write("Output:")
    st.code(stdout.decode(), language='r')
