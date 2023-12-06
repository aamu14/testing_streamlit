library(readxl)
library(cluster)
library(factoextra)
library(fpc)
library(knitr)

# Load the openxlsx package
library(openxlsx)
# Read the data file
df <- read_excel("datatest.xlsx")
df <- df[,-1]
