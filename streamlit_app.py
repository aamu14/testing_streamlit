import streamlit as st
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from st_aggrid import AgGrid
import seaborn as sns
# Configure
st.set_page_config(
    page_title="Project Intern BPS Kota Bandar Lampung",
    layout="wide", page_icon="📈"
)
st.header('🐍®️ R x Python Streamlit App 🐍®️')
st.sidebar.markdown('''
# About
This project is using the combination of R, Python. Some graphs are created with Tableau. The consideration will be written on the end of this project.
R packages used:
- `readxl`
- `cluster`
- `factoextra`
- `fpc`
- `knitr`
- `dplyr`
- `reshape`
Python libraries used:
- `streamlit==1.12.0`
- `matplotlib`
- `pandas`
- `pillow`
- `streamlit-aggrid`
- `seaborn`

''')
st.markdown("""
**Clustering adalah proses pengelompokan data serupa ke dalam kelompok-kelompok yang lebih kecil berdasarkan pada kesamaan karakteristik tertentu. 
Tujuannya adalah untuk mengidentifikasi pola atau struktur dalam data yang kompleks. 
Cara kerjanya mirip dengan mengumpulkan barang serupa ke dalam kelompok yang sama berdasarkan ciri-ciri yang mereka miliki. 
Misalnya, dalam pengelompokan warna, objek-objek dengan warna yang mirip akan dikelompokkan bersama. Hal yang sama berlaku dalam clustering data, 
di mana data dengan karakteristik yang mirip dikelompokkan bersama berdasarkan pada atribut-atribut tertentu.**
""")

st.markdown("""
Adapun metode clustering yang digunakan ada 2, yaitu Hierarchical Agglomerative Clustering dan Non-Hierarchical Clustering. Metode-metode yang akan digunakan adalah:
1. Average Linkage (Hierarchical)
2. Complete Linkage (Hierarchical)
3. Ward's Method (Hierarchical)
4. K-means (Non-Hierarchical)

Semua metode akan digunakan dan dibandingkan dengan beberapa uji metrik untuk menentukan metode mana yang paling baik digunakan untuk data yang digunakan.
""")

st.markdown("""---""")
url = "https://bit.ly/publikasibps2023"
st.markdown("""
            **Data yang digunakan berasal dari publikasi Badan Pusat Statistik (BPS) Kota Bandar Lampung, yaitu Kota Bandar Lampung Dalam Angka Tahun 2023 (%s).**""" % url)
st.markdown("""Data yang digunakan adalah data tahun 2022 yang terdiri dari data kecamatan, data luas daerah, dan data kependidikan. Adapun data kependidikan tersebut terbagi menjadi 3, yaitu:  
            1. Jumlah Guru Tingkat TK hingga SMA sederajat
            2. Jumlah Murid Tingkat TK hingga SMA sederajat
            3. Jumlah Sekolah Tingkat TK hinga SMA sederajat
            """)

# Read the Excel file into a DataFrame
data = pd.read_csv("datatest.csv")
st.dataframe(data)
st.markdown("""
            **Berikut adalah statistika deskriptif dari dataset yang digunakan:**  
            """)
data_summary = data
# Calculate summary statistics using describe()
summary_stats = data_summary.describe().loc[['min', '25%', '50%', '75%', 'mean', 'max']]
# Rename the index labels
summary_stats = summary_stats.rename(index={'min': 'Min', 'mean': 'Mean', 'max': 'Max', '25%': 'Q1', '50%': 'Median', '75%': 'Q3'})
# Round the summary statistics to 3 decimal places
summary_stats = summary_stats.round(2)
st.dataframe(summary_stats)
st.markdown("""
Dari tabel tersebut, terlihat bahwa ada satu kecamatan yang memiliki luas yang sangat kecil, hanya 2,03 km^2, sementara kecamatan terluas mencapai 24,24 km^2. Selanjutnya, rentang kepadatan penduduk dari yang terendah, 3336 orang per km^2, hingga tertinggi, 22018 orang per km^2. Data pendidikan mencakup berbagai tingkat sekolah yang setara, memberikan gambaran yang lebih komprehensif. Terdapat indikasi adanya beberapa nilai yang terletak jauh dari rentang nilai minimum hingga maksimum pada beberapa variabel, menunjukkan kemungkinan adanya pencilan (outlier). Keberadaan pencilan ini, meski mempengaruhi analisis, tidak dihapus karena pentingnya mempertimbangkan semua kecamatan dalam evaluasi data.
            """)

st.markdown("""---""")

# Assuming your data is in a CSV file named 'data.csv'
#data = pd.read_csv("datatest.csv")

 #Header 1

st.header('Observasi Luas Daerah, Kepadatan Penduduk, dan Jumlah Sekolah')

# Secara Keseluruhan Penggunaan
ikelompok = st.selectbox('Observasi Berdasarkan Tingkat',
                               ['TK/RA', 'SD/MI', 'SMP/MTs', 'SMA/SMK/MA'], key="kelompok 1")
if ikelompok == 'TK/RA':
    st.image("fig1.png")
    st.markdown("""
    Berdasarkan gambar di atas, terdapat beberapa hal yang menarik untuk diperhatikan. Pertama, jumlah TK/RA paling sedikit ada di Kecamatan Enggal dan Teluk Betuk Barat (TBB) dengan jumlah 8 sekolah. Kedua, Kecamatan Kemiling memiliki jumlah sekolah di tingkat TK/RA terbanyak, yaitu 47 sekolah dengan kepadatan penduduk yang kecil yaitu 3,792 dan daerah yang luas yaitu sebesar 24,24 km2. Ketiga, Kecamatan Bumi Waras dan Tanjung Karang Timur (TKT) adalah daerah dengan jumlah TK/RA yang cukup sedikit, yaitu masing-masing sebanyak 11 dan 10 sekolah. Tetapi, kepadatan penduduknya cukup besar dengan luas daerah yang kecil.
    """)
elif ikelompok == 'SD/MI':
    st.image("fig2.png")
    st.markdown("""
    Berdasarkan gambar di atas, dapat dilihat bahwa semua kecamatan telah memiliki sekolah di tingkat SD/MI. Jumlah sekolah terbanyak terdapat di Kecamatan Teluk Betung Selatan (TBS) dengan jumlah 22 sekolah dan paling sedikit terdapat di Kecamatan Enggal dengan jumlah hanya 7 sekolah.
    """)
elif ikelompok == 'SMP/MTs':
    st.image("fig3.png")
    st.markdown("""
    Berdasarkan gambar di atas, dapat dilihat bahwa jumlah sekolah di tingkat SMP/MTs terbanyak terdapat di Kecamatan Kemiling, Rajabasa, dan Tanjung Karang Pusat (TKP) sebanyak 14 sekolah, sedangkan jumlah sekolah paling sedikit terdapat di Kecamatan Way Halim sebanyak 3 sekolah.
    """)
else:
    st.image("fig4.png")
    st.markdown("""
    Berdasarkan gambar di atas, dapat dilihat bahwa jumlah sekolah di tingkat SMA/SMK/MA terbanyak terdapat di Kecamatan Kemiling dan Sukarame sebanyak 14 sekolah, sedangkan jumlah sekolah paling sedikit terdapat di Kecamatan Way Halim sebanyak 1 sekolah.
    """)


#col1, col2 = st.columns(2)
# Displaying the saved image in Streamlit
#with col1:
#   st.header('Untuk Sekolah Tingkat TK/RA')
 #  st.image("fig1.png")

#with col2:
 #  st.header("Untuk Tingkat SD/MI")
 #  st.image("fig2.png")
    
#col3, col4 = st.columns(2)
#with col3:
#   st.header("Untuk Tingkat SMP/MTs")
 #  st.image("fig3.png")

#with col4:
#   st.header("Untuk Tingkat SMA/SMK/MA")
 #  st.image("fig4.png")

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

# Secara Keseluruhan Penggunaan
ikelompok2 = st.selectbox('Observasi Berdasarkan Tingkat',
                               ['TK/RA', 'SD/MI', 'SMP/MTs', 'SMA/SMK/MA'], key="Kelompok 2")
if ikelompok2 == 'TK/RA':
    st.image("fig5.png")
    st.markdown("""
    Berdasarkan gambar di bawah, dapat dilihat bahwa banyaknya murid dan guru sebanding dengan jumlah sekolah di setiap kecamatan. Semakin banyak jumlah sekolah di tingkat TK/RA, maka jumlah murid dan guru di tingkat TK/RA akan meningkat, begitu juga sebaliknya.
    """)
elif ikelompok2 == 'SD/MI':
    st.image("fig6.png")
    st.markdown("""
    Berdasarkan gambar di atas, dapat dilihat bahwa banyaknya murid dan guru sebanding dengan jumlah sekolah di setiap kecamatan. Semakin banyak jumlah sekolah di tingkat SD/MI, maka jumlah murid dan guru di tingkat SD/MI akan meningkat, begitu juga sebaliknya.
    """)
elif ikelompok2 == 'SMP/MTs':
    st.image("fig7.png")
    st.markdown("""
    Berdasarkan gambar di atas, dapat dilihat bahwa banyaknya murid dan guru sebanding dengan jumlah sekolah di setiap kecamatan. Semakin banyak jumlah sekolah di tingkat SMP/MTs, maka jumlah murid dan guru di tingkat SMP/MTs akan meningkat, begitu juga sebaliknya.
    """)
else:
    st.image("fig8.png")
    st.markdown("""
    Berdasarkan gambar di atas, dapat dilihat bahwa banyaknya murid dan guru sebanding dengan jumlah sekolah di setiap kecamatan. Semakin banyak jumlah sekolah di tingkat SMA/SMK/MA, maka jumlah murid dan guru di tingkat SMA/SMK/MA akan meningkat, begitu juga sebaliknya.
    """)

st.header("""
Observasi Korelasi Antar Variabel
""")
st.markdown("""
Analisis korelasi (correlation) dilakukan untuk melihat bagaimana hubungan antar variabel satu sama lain. Perlu dicatat bahwa korelasi tidak sama dengan kausalitas (causalty), sehingga tidak dapat secara langsung apakah satu variabel menjadi penyebab bagi variabel lainnya.
""")
# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('datatest.csv')

# Assuming the first column is text, and you want correlations only between numerical columns
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Calculate the correlation matrix for numerical columns only
correlation_matrix = df[numerical_columns].corr()

# Plotting the correlation matrix as a heatmap
cor_graph= plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
st.pyplot(cor_graph)
st.markdown("""
1. Luas Daerah (km^2) dan Kepadatan Penduduk per km^2:  Korelasi negatif yang kuat (-0.78) menunjukkan bahwa semakin besar luas daerah, kepadatan penduduknya cenderung lebih rendah, dan sebaliknya.
2. Pendidikan dan Luas Daerah:  Tingkat TK/RA memiliki korelasi positif yang cukup kuat dengan luas daerah (0.65), menandakan bahwa dengan bertambahnya luas daerah, tingkat TK/RA cenderung naik. Korelasi positif yang lebih rendah terlihat pada tingkat SD/MI (0.39), tingkat SMP/MTs (0.37), dan tingkat SMA/SMK/MA (0.25).
3. Pendidikan dan Kepadatan Penduduk:  Tingkat pendidikan (TK/RA, SD/MI, SMP/MTs, SMA/SMK/MA) memiliki korelasi negatif dengan kepadatan penduduk. Ini menunjukkan bahwa semakin padat penduduknya, tingkat pendidikan cenderung lebih rendah.
4. Hubungan antara Jumlah Murid dan Tingkat Pendidikan:  Ada korelasi positif antara jumlah murid pada tingkat pendidikan (TK/RA, SD/MI, SMP/MTs, SMA/SMK/MA). Semakin tinggi tingkat pendidikan, jumlah muridnya cenderung lebih tinggi. Tingkat TK/RA memiliki korelasi paling kuat dengan jumlah murid pada tingkat tersebut (0.57).
5. Hubungan antara Jumlah Guru dan Tingkat Pendidikan:  Korelasi positif juga terlihat antara jumlah guru dengan tingkat pendidikan, menunjukkan semakin tinggi tingkat pendidikan, jumlah guru cenderung lebih tinggi.
6. Hubungan antara Jumlah Murid dan Jumlah Guru:  Korelasi antara jumlah murid dengan jumlah guru pada berbagai tingkat pendidikan juga tampak. Tingkat pendidikan yang lebih tinggi cenderung memiliki hubungan yang lebih tinggi antara jumlah murid dan guru.
""")
# Horizontal Divider
st.markdown("""---""")

st.header('Melakukan Analisis Cluster (Clustering)')
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
st.subheader('Menentukan Jumlah Kluster Terbaik dengan Uji Menggunakan Beberapa Metrik'
            )
st.markdown("""
            Setiap metrik mempunyai kriterianya sendiri dalam penentuan model terbaik. Adapun kriterianya adalah:
            1. Silhouette Score: Semakin besar nilainya, semakin baik modelnya
            2. Calinski-Harabasz Index: Semakin besar nilainya, semakin baik modelnya
            3. Davies Bouldin Index: Semakin kecil nilainya, semakin baik modelnya
            4. Dunn Index: Semakin besar nilainya, semakin baik modelnya

            Kriteria ini akan menentukan hasil akhir dari pengujian masing-masing metode clustering. Adapun hasilnya dapat dilihat pada tabel di bawah ini.
""")

with st.expander('See R code'):
  code1 = '''library(readxl, quietly = T)
library(cluster, quietly = T)
suppressMessages(library("factoextra"))
library(fpc, quietly = T)
library(knitr, quietly = T)
suppressMessages(library(dplyr))
suppressMessages(library(reshape2))

# Get content into a data frame
df_real <- read.csv("datatest.csv",
                header = TRUE, sep = ",")
df <- df_real[,-1]
# Scale the data
z <- scale(df)
# Calculate Euclidean distance
distance <- dist(z)
hc.c<-hclust(distance)
#plot(hc.c, labels=Data_Per_Kecamatan_Bandar_Lampung$Kecamatan,cex=.7)
#complete linkage

#kmeans
kc2<- kmeans(z,2)
kc3<- kmeans(z,3)
kc4<- kmeans(z,4)
kc5<- kmeans(z,5)
clusterCut_6<-kc2
clusterCut_7<-kc3
clusterCut_8<-kc4
clusterCut_9<-kc5
#set the cluster we needed. in this case, i use cluster between 2 to 5.
clusterCut_2<-cutree(hc.c,2)
clusterCut_3<-cutree(hc.c,3)
clusterCut_4<-cutree(hc.c,4)
clusterCut_5<-cutree(hc.c,5)
#silhouette complete linkage
sc2 <-silhouette(clusterCut_2,distance)
sc3 <-silhouette(clusterCut_3,distance)
sc4 <-silhouette(clusterCut_4,distance)
sc5 <-silhouette(clusterCut_5,distance)

#silhouette kmeans
sk2 <-silhouette(clusterCut_6$cluster,distance)
sk3 <-silhouette(clusterCut_7$cluster,distance)
sk4 <-silhouette(clusterCut_8$cluster,distance)
sk5 <-silhouette(clusterCut_9$cluster,distance)

#average
hc.a<- hclust(distance, method = "average")
clusterCut_10<-cutree(hc.a,2)
clusterCut_11<-cutree(hc.a,3)
clusterCut_12<-cutree(hc.a,4)
clusterCut_13<-cutree(hc.a,5)


#ward's
hc.w<- hclust(distance, method = "ward.D")
clusterCut_14<-cutree(hc.w,2)
clusterCut_15<-cutree(hc.w,3)
clusterCut_16<-cutree(hc.w,4)
clusterCut_17<-cutree(hc.w,5)

#silhouette average
sa2 <-silhouette(clusterCut_10,distance)
sa3 <-silhouette(clusterCut_11,distance)
sa4 <-silhouette(clusterCut_12,distance)
sa5 <-silhouette(clusterCut_13,distance)

#silhouette ward's
sw2 <-silhouette(clusterCut_14,distance)
sw3 <-silhouette(clusterCut_15,distance)
sw4 <-silhouette(clusterCut_16,distance)
sw5 <-silhouette(clusterCut_17,distance)

# Extracting silhouette widths and calculating averages
sil_widths_sc2 <- mean(sc2[, "sil_width"])
sil_widths_sc3 <- mean(sc3[, "sil_width"])
sil_widths_sc4 <- mean(sc4[, "sil_width"])
sil_widths_sc5 <- mean(sc5[, "sil_width"])
sil_widths_sk2 <- mean(sk2[, "sil_width"])
sil_widths_sk3 <- mean(sk3[, "sil_width"])
sil_widths_sk4 <- mean(sk4[, "sil_width"])
sil_widths_sk5 <- mean(sk5[, "sil_width"])
sil_widths_sa2 <- mean(sa2[, "sil_width"])
sil_widths_sa3 <- mean(sa3[, "sil_width"])
sil_widths_sa4 <- mean(sa4[, "sil_width"])
sil_widths_sa5 <- mean(sa5[, "sil_width"])
sil_widths_sw2 <- mean(sw2[, "sil_width"])
sil_widths_sw3 <- mean(sw3[, "sil_width"])
sil_widths_sw4 <- mean(sw4[, "sil_width"])
sil_widths_sw5 <- mean(sw5[, "sil_width"])
# Creating dataframes for each cluster
# Generating repeated sequences for each method
repeats <- 4
complete_method <- rep("Complete", repeats)
kmeans_method <- rep("K-Means", repeats)
average_method <-rep("Average", repeats)
wards_method <-rep("Ward's", repeats)

# Creating the Method column in your dataframe
method_column <- c(complete_method, kmeans_method, average_method, wards_method)

# Define the number of rows you need
df_sill <- data.frame(
  Method = c(complete_method, kmeans_method, average_method, wards_method),
  # Your existing Cluster and sil_score columns
  Cluster = rep(c("Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"), length.out = length(method_column)),
  Sil_score = c(
    sil_widths_sc2, sil_widths_sc3, sil_widths_sc4, sil_widths_sc5,
    sil_widths_sk2, sil_widths_sk3, sil_widths_sk4, sil_widths_sk5,
    sil_widths_sa2, sil_widths_sa3, sil_widths_sa4, sil_widths_sa5,
    sil_widths_sw2, sil_widths_sw3, sil_widths_sw4, sil_widths_sw5
  )
)

# Arrange the dataframe by calinhara in descending order
sill_df_sorted <- df_sill %>% arrange(desc(Sil_score))
# Saving the dataframe into a CSV file named 'silhouette.csv'
write.csv(sill_df_sorted, file = "silhouette.csv", row.names = FALSE)


#for calinhara
#calinhara for complete
c_ca2<-calinhara(z,clusterCut_2)
c_ca3<-calinhara(z,clusterCut_3)
c_ca4<-calinhara(z,clusterCut_4)
c_ca5<-calinhara(z,clusterCut_5)

#calinhara for kmeans
k_ca2<-calinhara(z,clusterCut_6$cluster)
k_ca3<-calinhara(z,clusterCut_7$cluster)
k_ca4<-calinhara(z,clusterCut_8$cluster)
k_ca5<-calinhara(z,clusterCut_9$cluster)

#calinhara for average
a_ca2<-calinhara(z,clusterCut_10)
a_ca3<-calinhara(z,clusterCut_11)
a_ca4<-calinhara(z,clusterCut_12)
a_ca5<-calinhara(z,clusterCut_13)

#calinhara for wards
w_ca2<-calinhara(z,clusterCut_14)
w_ca3<-calinhara(z,clusterCut_15)
w_ca4<-calinhara(z,clusterCut_16)
w_ca5<-calinhara(z,clusterCut_17)

# Creating a dataframe
# Creating dataframes for each cluster
# Generating repeated sequences for each method
repeats <- 4
complete_method <- rep("Complete", repeats)
kmeans_method <- rep("K-Means", repeats)
average_method <-rep("Average", repeats)
wards_method <-rep("Ward's", repeats)

df_calinski <- data.frame(
  Method = c(complete_method, kmeans_method, average_method, wards_method),
  # Your existing Cluster and DBI_score columns
  Cluster = rep(c("Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"), length.out = length(method_column)),
  Calinski_value = c(
    c_ca2, c_ca3, c_ca4, c_ca5,
    k_ca2, k_ca3, k_ca4, k_ca5,
    a_ca2, a_ca3, a_ca4, a_ca5,
    w_ca2, w_ca3, w_ca4, w_ca5
  )
)
# Arrange the dataframe by calinhara in descending order
calinhara_df_sorted <- df_calinski %>% arrange(desc(Calinski_value))
# Saving the dataframe into a CSV file named 'calinhara.csv'
write.csv(calinhara_df_sorted, file = "calinhara.csv", row.names = FALSE)")
  '''
  st.code(code1, language='R')
process1 = subprocess.Popen(["Rscript", "sil&calins.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
col9, col10, col11, col12 = st.columns(4)
# Displaying the saved image in Streamlit
with col9:
    st.markdown("""
            Silhouette Score
            """)
    # Read the Excel file into a DataFrame
    data4 = pd.read_csv("silhouette.csv")
    st.dataframe(data4, height=300, width=600)
with col10:
    st.markdown("""
        Calinski-Harabasz Index
        """)
    # Read the Excel file into a DataFrame
    data3 = pd.read_csv("calinhara.csv")
    st.dataframe(data3, height=300)
with col11:
    st.markdown("""
        Davies-Bouldin Index
        """)
    # Read the Excel file into a DataFrame
    data5 = pd.read_csv("dbi.csv")
    st.dataframe(data5, height=300)
with col12:
    st.markdown("""
            Dunn Index
            """)
    # Read the Excel file into a DataFrame
    data6 = pd.read_csv("dunn.csv")
    st.dataframe(data6, height=300)
st.markdown("""
Dari tabel di atas dapat dilihat bahwa average linkage dan complete linkage memenuhi dua kriteria metrik dan menjadi model terbaik. Tetapi karena nilai dari average linkage dan complete linkage memiliki nilai yang sama, maka akan dipilih salah satu metode yang akan dilanjutkan untuk dilihat karakteristik dari klusternya, yaitu metode complete linkage dengan tiga kluster.
""")
st.markdown("""---""")
#show characteristic
st.subheader('Karakteristik Masing-Masing Kluster')
with st.expander('See R code'):
  code2 = '''#show the characteristic of complete linkage
t<-aggregate(df_real[,-c(1,1)],list(clusterCut_3),mean)

library(reshape2)

# Assuming your 't' dataframe is named 'result'
result <- dcast(melt(as.data.frame(t), id.vars = "Group.1"), variable ~ Group.1)
# Rename the columns to match your desired format
colnames(result)[-1] <- paste("Kluster", colnames(result)[-1])
# Rename the 'variable' column to 'Variabel'
colnames(result)[1] <- "Variabel"
# Assuming 'result' is your final dataframe
write.csv(result, file = "characteristic.csv", row.names = FALSE)
  '''
  st.code(code2, language='R')

data7 = pd.read_csv("characteristic.csv")
st.dataframe(data7, height=500)
st.markdown("""
Tabel ini mencerminkan karakteristik dari masing-masing kluster. Metode yang terpilih adalah metode hierarchical (agglomerative) clustering, terutama menggunakan metode complete linkage untuk membentuk tiga kluster. Pemilihan ini didasarkan pada kriteria yang tidak terpenuhi oleh metode lain dalam lebih dari satu metrik evaluasi.

Kluster 1 memiliki luas daerah yang moderat, kepadatan penduduk tinggi, dan variabel jumlah sekolah, guru, dan murid di tingkat TK/RA dan SD/MI berada di antara kluster 2 dan 3. Namun, variabel yang sama di tingkat SMP/MTs dan SMA/SMK/MA memiliki nilai paling rendah, menandakan fokus pendidikan yang lebih rendah di tingkat ini.

Kluster 2 memiliki luas daerah terkecil, kepadatan penduduk cukup tinggi, dan nilai jumlah sekolah di tingkat SMP/MTs dan SMA/SMK/MA tinggi, sementara jumlah murid dan guru di tingkat yang sama sangat tinggi. Ini menandakan fokus yang lebih besar pada tingkat pendidikan lanjutan di kluster ini.

Kluster 3 memiliki luas daerah terbesar dengan kepadatan penduduk yang rendah. Daerah dalam kluster ini tampaknya lebih fokus pada pendidikan dengan nilai variabel pendidikan yang tinggi di semua tingkatan.

Namun, beberapa kecamatan mungkin terletak di kluster yang tidak sepenuhnya mencerminkan luas wilayahnya karena analisis kluster dilakukan secara umum untuk beberapa karakteristik, bukan untuk mendefinisikan satu daerah secara eksklusif. Disamping itu, kemungkinan hasil yang berbeda bisa disebabkan oleh relatif kecilnya perbedaan nilai dalam pengecekan metrik yang memungkinkan adanya bias dalam hasil.
""")
#dendogram
st.subheader('Plot Cluster Dendogram'
            )
with st.expander('See R code'):
  code3 = '''#show dendogram
png("cluster_dend.png", width = 800, height = 600)  # Specify file path and dimensions
plot(hc.c, labels = df_real$Kecamatan, cex = 1.5)
# Adding a horizontal line at y = 3
abline(h = 7.5, col = "darkgreen", lty = 1, lwd = 1.5) # Adjust color and line type as needed
# Plot with labels
dev.off()  # Close the PNG device
  '''
  st.code(code3, language='R')
st.image("cluster_dend.png")
st.markdown("""
            Dendogram tersebut menyajikan anggota kluster, dalam hal ini adalah kecamatan mana saja yang berada pada kluster 1,2, dan 3.
            Agar lebih mudah dilihat, akan dibuat visualisasi dari masing-masing kluster ke dalam bentuk peta.
""")

st.subheader("""Visualisasi dari Kluster""")
st.image("Keterangan Peta.png")
st.markdown("""
Hasil dendogram kluster menunjukkan bahwa terdapat 3 kluster dengan kluster pertama yang terdiri dari 16 kecamatan dan kluster kedua yang terdiri dari 1 kecamatan, dan kluster ketiga terdiri dari 3 kecamatan. Anggota dari masing-masing kluster adalah:
1.	Kluster Pertama: Teluk Betung Barat, Teluk Betung Timur, Teluk Betung Selatan, Bumi Waras, Panjang, Tanjung Karang Timur, Kedamaian, Teluk Betung Utara, Tanjung Karang Pusat, Tanjung Karang Barat, Langkapura, Kedaton, Tanjung Senang, Labuhan Ratu, Sukabumi, Way Halim
2.	Kluster Kedua: Enggal
3.	Kluster Ketiga: Kemiling, Rajabasa, Sukarame
""")
st.header('Kesimpulan & Saran'
         )
st.subheader('Kesimpulan'
            )
st.markdown("""
1.	Jumlah sekolah, murid, dan guru memiliki hubungan yang sebanding. Semakin banyak sekolah, maka semakin banyak murid dan guru yang ada. Tetapi, terdapat beberapa hal yang dapat diperhatikan, seperti kecamatan yang penduduknya tidak terlalu padat tetapi daerahnya cukup luas, dan sebaliknya.
2.	Hasil analisis kluster dengan agglomerative clustering memberikan lima rekomendasi model terbaik dan dengan k-means memberikan satu rekomendasi model terbaik. Model clustering yang dievaluasi dengan empat jenis metrik memberikan hasil bahwa metode average linkage dan complete linkage adalah metode yang terbaik dengan memberikan hasil yang sama. Oleh karena itu, hanya metode complete linkage dengan tiga kluster yang akan digunakan.
3.	Kluster 1 adalah daerah dengan kecamatan yang cukup luas dan sangat padat penduduk, dan daerah yang cukup fokus di pendidikan tingkat TK/RA dan SD/MI. Kluster 2 adalah daerah yang kecil dengan kepadatan penduduk menengah, lalu pendidikannya berfokus pada SMP/MTs dan SMA/SMK/MA. Kluster 3 adalah daerah yang terluas tetapi sedikit penduduk dan merupakan daerah yang fokus pada pendidikan di semua tingkat.
""")
################################
st.subheader('Saran'
            )
st.markdown("""
Berdasarkan hasil dan pembahasan yang diperoleh, adapun saran yang dapat diberikan adalah:
1.	Menambahkan jenis metrik untuk mengevaluasi model kluster. Hal ini dikarenakan bahwa masih terdapat berbagai jenis metrik yang memiliki masing-masing ketentuannya dalam menentukan kluster terbaik
2.	Menggunakan metode kluster lainnya seperti PAM, CLARA, dan lain sebagainya. Menambahkan metode lain dapat menambahkan pertimbangan dalam memilih metode terbaik yang sesuai dengan data.
""")

#################################
st.markdown("""---""")
st.caption('CATATAN')
st.caption('1. Beberapa package dari R tidak dapat di-import seperti clusterSim dan clValid, sehingga harus menggunakan alternatif seperti menyimpan hasil outputnya ke dalam bentuk gambar atau file terlebih dahulu.')
st.caption('2. Beberapa output grafik dilakukan dengan menggunakan Tableau dikarenakan harus nampilkannya dalam 1 plot secara bersamaan untuk kepentingan analisis.')
st.caption('3. Streamlit ini digunakan dengan tujuan untuk melihat bagaimana penggunaan R dan Python secara bersamaan dalam Streamlit.')
st.caption('4. Lalu terdapat beberapa penyesuaian agar mempermudah penggunaan streamlit ini.'
          )

st.markdown("""---""")
