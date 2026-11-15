import pandas as pd

# Load dataset
df = pd.read_csv("Dataset/50_Startups.csv")

# Display first five records
print("FIRST FIVE RECORDS:")
print(df.head())

# Display dataset information
print("\nDATASET INFORMATION:")
print(df.info())

# Display number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# Display column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())