import streamlit as st
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
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

st.markdown("""
           Dari tabel di atas dapat dilihat bahwa terdapat satu kecamatan yang luasnya sangat kecil, yaitu 2,03 km^2, sedangkan daerah yang paling luas memiliki ukuran sebesar 24,24 km^2.  Selanjutnya, kepadatan penduduk yang paling kecil bernilai 3336 orang/km^2 dan nilai paling besar yaitu 22018 orang/km^2.  Selain itu, terdapat indikasi pencilan (outlier) pada beberapa variabel yang dapat dilihat dari jauhnya rentang nilai minimum ke nilai maksimum dari masing-masing variabel.  Pencilan ini dapat mempengaruhi keakuratan analisis. Tetapi, tidak dilakukan penghapusan data karena semua kecamatan harus dipertimbangkan.
           """)


# Assuming your data is in a CSV file named 'data.csv'
data = pd.read_csv("datatest.csv")

# Sorting the DataFrame by 'Tingkat TK' column in descending order
sorted_data = data.sort_values(by='Tingkat TK/RA', ascending=False)

# Creating a histogram using Matplotlib
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
bars = plt.bar(sorted_data['Kecamatan'], sorted_data['Tingkat TK/RA'])
plt.xlabel('Kecamatan')
plt.ylabel('Tingkat TK')
plt.title('Histogram of Tingkat TK by Kecamatan')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability if needed

# Adding values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), va='bottom', ha='center')

plt.tight_layout()
# Saving the histogram as an image
plt.savefig('graph_1.png')  # Save the image as 'graph_1.png'
# Displaying the saved image in Streamlit
st.image('graph_1.png')


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
