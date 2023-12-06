library(readxl)
library(cluster)
library(factoextra)
library(fpc)

# Load the openxlsx package
library(openxlsx)
# Read the data file
df <- read_excel("datatest.xlsx")

# Create a summary of the data
summary_data <- summary(df)
summary_data
