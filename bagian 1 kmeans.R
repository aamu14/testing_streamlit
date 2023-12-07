library(readxl)
library(cluster)
library(factoextra)
library(fpc)
library(knitr)

# Get content into a data frame
df <- read.csv("datatest.csv",
                header = TRUE, sep = ",")
df <- df[,-1]
# Scale the data
z <- scale(df)
# Calculate Euclidean distance
distance <- dist(z)
#set the cluster we needed. in this case, i use cluster between 2 to 5.
kc2<- kmeans(z,2)
kc3<- kmeans(z,3)
kc4<- kmeans(z,4)
kc5<- kmeans(z,5)

clusterCut_2<-kc2
clusterCut_3<-kc3
clusterCut_4<-kc4
clusterCut_5<-kc5

#use dunn index
library(clValid)
dunn(distance, clusterCut_2$cluster)
dunn(distance, clusterCut_3$cluster)
dunn(distance, clusterCut_4$cluster)
dunn(distance, clusterCut_5$cluster)
