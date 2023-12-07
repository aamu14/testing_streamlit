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

library(cluster)

# Your code to generate the plots
sk2 <- silhouette(clusterCut_2$cluster, distance)
sk3 <- silhouette(clusterCut_3$cluster, distance)
sk4 <- silhouette(clusterCut_4$cluster, distance)
sk5 <- silhouette(clusterCut_5$cluster, distance)

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

