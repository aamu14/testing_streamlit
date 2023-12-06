library(readxl)
library(cluster)
library(factoextra)
library(fpc)
library(clusterSim)

# Read the data file
Data_Per_Kecamatan_Bandar_Lampung <- read_excel("datatest.xlsx")

# Scale the data
z <- scale(Data_Per_Kecamatan_Bandar_Lampung[,-1])

# Calculate Euclidean distance
distance <- dist(z)
distance
