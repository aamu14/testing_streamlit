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

# Extracting average silhouette width values
avg_width_sk2 <- sk2$avg.width
avg_width_sk3 <- sk3$avg.width
avg_width_sk4 <- sk4$avg.width
avg_width_sk5 <- sk5$avg.width
# Extracting average silhouette width values
avg_width_sk6 <- sk6$avg.width
avg_width_sk7 <- sk7$avg.width
avg_width_sk8 <- sk8$avg.width
avg_width_sk9 <- sk9$avg.width

# Extracting average silhouette width values
avg_widths <- data.frame(
  Method = c("Complete", "Complete", "Complete", "Complete", "K-Means", "K-Means", "K-Means", "K-Means"),
  Cluster = c("Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"),
  Average_Silhouette_Width = c(sk2$avg.width, sk3$avg.width, sk4$avg.width, sk5$avg.width, sk6$avg.width,sk7$avg.width, sk8$avg.width, sk9$avg.width)
)

# Saving the dataframe into a CSV file named 'silhouette.csv'
write.csv(avg_widths, file = "silhouette.csv", row.names = FALSE)
