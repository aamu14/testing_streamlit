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
hc.c<-hclust(distance)
#plot(hc.c, labels=Data_Per_Kecamatan_Bandar_Lampung$Kecamatan,cex=.7)
#complete linkage
#set the cluster we needed. in this case, i use cluster between 2 to 5.
clusterCut_2<-cutree(hc.c,2)
clusterCut_3<-cutree(hc.c,3)
clusterCut_4<-cutree(hc.c,4)
clusterCut_5<-cutree(hc.c,5)

sk2 <-silhouette(clusterCut_2,distance)
sk3 <-silhouette(clusterCut_3,distance)
sk4 <-silhouette(clusterCut_4,distance)
sk5 <-silhouette(clusterCut_5,distance)

#kmeans
kc2<- kmeans(z,2)
kc3<- kmeans(z,3)
kc4<- kmeans(z,4)
kc5<- kmeans(z,5)
clusterCut_6<-kc2
clusterCut_7<-kc3
clusterCut_8<-kc4
clusterCut_9<-kc5

sk6 <-silhouette(clusterCut_6$cluster,distance)
sk7 <-silhouette(clusterCut_7$cluster,distance)
sk8 <-silhouette(clusterCut_8$cluster,distance)
sk9 <-silhouette(clusterCut_9$cluster,distance)

# Open PNG devices to save the plots
png("sk2_plot.png")
plot(sk2)
dev.off()

png("sk3_plot.png")
plot(sk3)
dev.off()

png("sk4_plot.png")
plot(sk4)
dev.off()

png("sk5_plot.png")
plot(sk5)
dev.off()

png("sk6_plot.png")
plot(sk6)
dev.off()

png("sk7_plot.png")
plot(sk7)
dev.off()

png("sk8_plot.png")
plot(sk8)
dev.off()

png("sk9_plot.png")
plot(sk9)
dev.off()

#calinhara for complete
c_a1<-calinhara(z,clusterCut_2)
c_a2<-calinhara(z,clusterCut_3)
c_a3<-calinhara(z,clusterCut_4)
c_a4<-calinhara(z,clusterCut_5)

#calinhara for kmeans
k_ca1<-calinhara(z,clusterCut_2$cluster)
k_ca2<-calinhara(z,clusterCut_3$cluster)
k_ca3<-calinhara(z,clusterCut_4$cluster)
k_ca4<-calinhara(z,clusterCut_5$cluster)

# Creating a dataframe
dataconvert <- data.frame(
  Method = c("Complete", "Complete", "Complete", "Complete", "K-Means", "K-Means", "K-Means", "K-Means"),
  Metric = c("Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"),
  Value = c(c_a1, c_a2, c_a3, c_a4, k_ca1, k_ca2, k_ca3, k_ca4)
)

# Printing the dataframe
print(dataconvert)
