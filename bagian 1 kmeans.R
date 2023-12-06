library(readxl)
library(cluster)
library(factoextra)
library(fpc)
library(knitr)

# Load the openxlsx package
library(openxlsx)
# Read the data file
df <- read_excel("datatest.xlsx")

# Create a summary of the data
summary_data <- summary(df)

# Store the summary output as a character vector
summary_output <- capture.output(summary_data)

# Print the summary output as a table
kable(summary_output, format = "html")
