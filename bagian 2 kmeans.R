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

png("sk6_plot.png")
plot(sk6)
dev.off()
