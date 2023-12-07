import streamlit as st
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
# Configure
st.set_page_config(
    page_title="Project Intern BPS Kota Bandar Lampung",
    layout="wide", page_icon="📈"
)
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

st.markdown("""---""")

# Assuming your data is in a CSV file named 'data.csv'
#data = pd.read_csv("datatest.csv")

 #Header 1

st.header('Observasi Luas Daerah, Kepadatan Penduduk, dan Jumlah Sekolah')
col1, col2 = st.columns(2)
# Displaying the saved image in Streamlit
with col1:
   st.header('Untuk Sekolah Tingkat TK/RA')
   st.image("fig1.png")

with col2:
   st.header("Untuk Tingkat SD/MI")
   st.image("fig2.png")
    
col3, col4 = st.columns(2)
with col3:
   st.header("Untuk Tingkat SMP/MTs")
   st.image("fig3.png")

with col4:
   st.header("Untuk Tingkat SMA/SMK/MA")
   st.image("fig4.png")

#tab1, tab2, tab3 = st.tabs(['Luas Daerah (km^2) VS Kecamatan',
#                      'Kepadatan Penduduk (per km^2) VS Kecamatan', 'Jumlah Sekolah di Tingkat TK/RA VS Kecamatan'])
#with tab1:
    #subheader 1
#           st.subheader('Perbandingan Luas Daerah Setiap Kecamatan')
           # Sorting the DataFrame by 'Tingkat TK' column in descending order
    #       sorted_data = data.sort_values(by='Luas Daerah (km^2)', ascending=False)
     # Creating a histogram using Matplotlib
  #         plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
  #         bars = plt.bar(sorted_data['Kecamatan'], sorted_data['Luas Daerah (km^2)'])
   #        plt.xlabel('Kecamatan')
   #        plt.ylabel('Luas Daerah')
   #        plt.title('Histogram of Luas Daerah by Kecamatan')
      #     plt.xticks(rotation=90)  # Rotate x-axis labels for better readability if needed
           # Adding values on top of the bars
  #         for bar in bars:
    #           yval = bar.get_height()
   #            plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), va='bottom', ha='center')
 #          plt.tight_layout()
 #          plt.savefig('graph_1.png')  # Save the image as 'graph_1.png'

           # Displaying the saved image in Streamlit
#           st.image('graph_1.png')

#with tab2:
               # Subheader 2
   #        st.subheader('Perbandingan Kepadatan Penduduk Setiap Kecamatan')
           # Sorting the DataFrame by 'Tingkat TK' column in descending order
  #         sorted_data = data.sort_values(by='Kepadatan Penduduk per km^2', ascending=False)
     # Creating a histogram using Matplotlib
    #       plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    #       bars = plt.bar(sorted_data['Kecamatan'], sorted_data['Kepadatan Penduduk per km^2'])
    #       plt.xlabel('Kecamatan')
   #        plt.ylabel('Kepadatan Penduduk')
   #        plt.title('Histogram of Kepadatan Penduduk by Kecamatan')
    #       plt.xticks(rotation=90)  # Rotate x-axis labels for better readability if needed
           # Adding values on top of the bars
   #        for bar in bars:
   #            yval = bar.get_height()
   #            plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), va='bottom', ha='center')
  #         plt.tight_layout()
           # Saving the histogram as an image
  #         plt.savefig('graph_2.png')  # Save the image as 'graph_1.png'
           # Displaying the saved image in Streamlit
  #         st.image('graph_2.png')
#with tab3:
               # Subheader 3
   #        st.subheader('Perbandingan Banyaknya Sekolah Tingkat TK/RA Setiap Kecamatan')
           # Sorting the DataFrame by 'Tingkat TK' column in descending order
   #        sorted_data = data.sort_values(by='Tingkat TK/RA', ascending=False)
  #         # Creating a histogram using Matplotlib
  #         plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
  #         bars = plt.bar(sorted_data['Kecamatan'], sorted_data['Tingkat TK/RA'])
   #        plt.xlabel('Kecamatan')
  #         plt.ylabel('Tingkat TK/RA')
  #         plt.title('Histogram of Tingkat TK/RA by Kecamatan')
   #        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability if needed
           
           # Adding values on top of the bars
#           for bar in bars:
  #             yval = bar.get_height()
    #           plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), va='bottom', ha='center')
  #         plt.tight_layout()
           # Saving the histogram as an image
#           plt.savefig('graph_3.png')  # Save the image as 'graph_1.png'
           # Displaying the saved image in Streamlit
#           st.image('graph_3.png')

# Header 2
#tab4, tab5, tab6 = st.tabs(['Jumlah Sekolah di Tingkat SD/MI VS Kecamatan',
 #                     'Jumlah Sekolah di Tingkat SMP/MTs VS Kecamatan', 'Jumlah Sekolah di Tingkat SMA/MA/SMK VS Kecamatan'])
#with tab4:
    #subheader 4
          # st.subheader('Perbandingan Luas Daerah Setiap Kecamatan')
           # Sorting the DataFrame by 'Tingkat TK' column in descending order
          # sorted_data = data.sort_values(by='Tingkat SD/MI', ascending=False)
     # Creating a histogram using Matplotlib
           #plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
           #bars = plt.bar(sorted_data['Kecamatan'], sorted_data['Tingkat SD/MI'])
          # plt.xlabel('Kecamatan')
         #  plt.ylabel('Tingkat SD/MI')
        #   plt.title('Histogram of Tingkat SD/MI by Kecamatan')
       #    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability if needed
           # Adding values on top of the bars
      #     for bar in bars:
     #          yval = bar.get_height()
    #           plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), va='bottom', ha='center')
   #        plt.tight_layout()
  #         plt.savefig('graph_4.png')  # Save the image as 'graph_1.png'

           # Displaying the saved image in Streamlit
 #          st.image('graph_4.png')

#with tab5:
               # Subheader 2
#           st.subheader('Perbandingan Tingkat SMP/MTs Setiap Kecamatan')
           # Sorting the DataFrame by 'Tingkat TK' column in descending order
#           sorted_data = data.sort_values(by='Tingkat SMP/MTs', ascending=False)
     # Creating a histogram using Matplotlib
 #          plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
 #          bars = plt.bar(sorted_data['Kecamatan'], sorted_data['Tingkat SMP/MTs'])
 #          plt.xlabel('Kecamatan')
  #         plt.ylabel('Tingkat SMP/MTs')
 #          plt.title('Histogram of Tingkat SMP/MTsk by Kecamatan')
 #          plt.xticks(rotation=90)  # Rotate x-axis labels for better readability if needed
           # Adding values on top of the bars
#           for bar in bars:
#               yval = bar.get_height()
#               plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), va='bottom', ha='center')
#           plt.tight_layout()
           # Saving the histogram as an image
#           plt.savefig('graph_5.png')  # Save the image as 'graph_1.png'
           # Displaying the saved image in Streamlit
 #          st.image('graph_5.png')
#with tab6:
               # Subheader 3
           #st.subheader('Perbandingan Banyaknya Sekolah Tingkat SMA/MA/SMK Setiap Kecamatan')
           # Sorting the DataFrame by 'Tingkat TK' column in descending order
           #sorted_data = data.sort_values(by='Tingkat SMA/SMK/MA', ascending=False)
           # Creating a histogram using Matplotlib
           #plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
          # bars = plt.bar(sorted_data['Kecamatan'], sorted_data['Tingkat SMA/SMK/MA'])
         #  plt.xlabel('Kecamatan')
        #   plt.ylabel('Tingkat SMA/SMK/MA')
       #    plt.title('Histogram of Tingkat Tingkat SMA/SMK/MA by Kecamatan')
      #     plt.xticks(rotation=90)  # Rotate x-axis labels for better readability if needed
     #      
    #       # Adding values on top of the bars
   #        for bar in bars:
  #             yval = bar.get_height()
 #              plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), va='bottom', ha='center')
 #          plt.tight_layout()
#           # Saving the histogram as an image
#           plt.savefig('graph_6.png')  # Save the image as 'graph_1.png'
#           # Displaying the saved image in Streamlit
#           st.image('graph_6.png')

# Horizontal Divider
st.markdown("""---""")

 #Header 2

st.header('Observasi Jumlah Sekolah, Jumlah Guru, dan Jumlah Murid')
col5, col6 = st.columns(2)
# Displaying the saved image in Streamlit
with col5:
   st.header('Untuk Sekolah Tingkat TK/RA')
   st.image("fig5.png")

with col6:
   st.header("Untuk Tingkat SD/MI")
   st.image("fig6.png")
    
col7, col8 = st.columns(2)
with col7:
   st.header("Untuk Tingkat SMP/MTs")
   st.image("fig7.png")

with col8:
   st.header("Untuk Tingkat SMA/SMK/MA")
   st.image("fig8.png")

# Horizontal Divider
st.markdown("""---""")



st.subheader('1. Printing text in R')
st.markdown("""
            Langkah selanjutnya adalah melakukan Clustering. Ada 2 jenis metode clustering yang akan digunakan, yaitu hierarchical dan non-hierarchical. metode hierarchical yang akan digunakan adalah K-means, sedangkan metode non-hierarchical yang akan digunakan adalah average linkage; complete linkage; ward's method.  Adapun tahapannya adalah sebagai berikut:
            1. melakukan normalisasi data (jika dibutuhkan) dan menghitung jarak euclidean.
            2. menentukan banyak cluster 
            3. menguji masing-masing jumlah cluster agar mendapatkan jumlah cluster yang terbaik untuk masing-masing metode.
            4. membandingkan hasil dari semua pengujian, lalu dibandingkan dengan masing-masing metode
            5. metode dengan hasil pengujian yang valid paling banyak akan menjadi metode cluster terbaik
            6. menampilkan cluster dendogram dari metode cluster yang terpilih
            7. melakukan visualisasi dari metode cluster yang terpilih
            """)


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
process1 = subprocess.Popen(["Rscript", "bagian 1 kmeans.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.dataframe(result1)
