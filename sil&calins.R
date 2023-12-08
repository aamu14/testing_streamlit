library(readxl, quietly = T)
library(cluster, quietly = T)
suppressMessages(library("factoextra"))
library(fpc, quietly = T)
library(knitr, quietly = T)

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
#silhouette complete linkage
sc2 <-silhouette(clusterCut_2,distance)
sc3 <-silhouette(clusterCut_3,distance)
sc4 <-silhouette(clusterCut_4,distance)
sc5 <-silhouette(clusterCut_5,distance)

#kmeans
kc2<- kmeans(z,2)
kc3<- kmeans(z,3)
kc4<- kmeans(z,4)
kc5<- kmeans(z,5)
clusterCut_6<-kc2
clusterCut_7<-kc3
clusterCut_8<-kc4
clusterCut_9<-kc5
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

#silhouette average
sa2 <-silhouette(clusterCut_10,distance)
sa3 <-silhouette(clusterCut_11,distance)
sa4 <-silhouette(clusterCut_12,distance)
sa5 <-silhouette(clusterCut_13,distance)

#ward's
hc.w<- hclust(distance, method = "ward.D")
clusterCut_14<-cutree(hc.w,2)
clusterCut_15<-cutree(hc.w,3)
clusterCut_16<-cutree(hc.w,4)
clusterCut_17<-cutree(hc.w,5)

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

# Your existing Cluster and DBI_score columns
cluster_column <- rep(c("Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"), length.out = length(method_column))

# Define the number of rows you need
avg_widths <- data.frame(
  Method = c(complete_method, kmeans_method, average_method, wards_method),
  # Your existing Cluster and DBI_score columns
  Cluster = rep(c("Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"), length.out = length(method_column)),
  Sil_score = c(
    sil_widths_sc2, sil_widths_sc3, sil_widths_sc4, sil_widths_sc5,
    sil_widths_sk2, sil_widths_sk3, sil_widths_sk4, sil_widths_sk5,
    sil_widths_sa2, sil_widths_sa3, sil_widths_sa4, sil_widths_sa5,
    sil_widths_sw2, sil_widths_sw3, sil_widths_sw4, sil_widths_sw5
  )
)

# Saving the dataframe into a CSV file named 'silhouette.csv'
write.csv(avg_widths, file = "silhouette.csv", row.names = FALSE)


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

dataconvert <- data.frame(
  Method = c(complete_method, kmeans_method, average_method, wards_method),
  # Your existing Cluster and DBI_score columns
  Cluster = rep(c("Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"), length.out = length(method_column)),
  Sil_score = c(
    c_ca2, c_ca3, c_ca4, c_ca5,
    k_ca2, k_ca3, k_ca4, k_ca5,
    a_ca2, a_ca3, a_ca4, a_ca5,
    k_ca2, k_ca2, k_ca2, k_ca2
  )
)
# Saving the dataframe into a CSV file named 'calinhara.csv'
write.csv(dataconvert, file = "calinhara.csv", row.names = FALSE)
