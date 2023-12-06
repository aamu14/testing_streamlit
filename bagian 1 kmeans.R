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

# Create a summary of the data
# Calculate summary statistics for specific columns
summary_stats <- sapply(df, function(x) {
  c(
    min = min(x, na.rm = TRUE),
    Q1 = quantile(x, 0.25, na.rm = TRUE),
    median = median(x, na.rm = TRUE),
    Q3 = quantile(x, 0.75, na.rm = TRUE),
    mean = mean(x, na.rm = TRUE),
    max = max(x, na.rm = TRUE)
  )
})

# Convert the summary statistics to a data frame and transpose it
summary_table <- as.data.frame(summary_stats)
summary_table <- t(summary_table)

# Assign column names
colnames(summary_table) <- c("Minimum", "Q1", "Median", "Q3", "Rata-rata", "Maksimum")

# Add variable names as row names
rownames(summary_table) <- c(
  "Luas Daerah (km^2)", "Kepadatan Penduduk per km^2", "Tingkat TK/RA", "Tingkat SD/MI",
  "Tingkat SMP/MTs", "Tingkat SMA/MA/SMK", "Murid Tingkat TK/RA", "Murid Tingkat SD/MI",
  "Murid Tingkat SMP/MTs", "Murid Tingkat SMA/MA/SMK", "Guru Tingkat TK/RA", "Guru Tingkat SD/MI",
  "Guru Tingkat SMP/MTs", "Guru Tingkat SMA/MA/SMK"
)

# Display the summary table
summary_table
