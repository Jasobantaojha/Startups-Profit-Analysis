import pandas as pd
from pathlib import Path

# ==========================================
# PRDA-01: STARTUP PROFIT ANALYSIS
# DATA LOADING AND DATA CLEANING
# ==========================================

# Get project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load dataset
file_path = BASE_DIR / "Dataset" / "50_Startups.csv"

df = pd.read_csv(file_path)

print("\n========== DATASET LOADED ==========")

print("Dataset loaded successfully!")

# ==========================================
# 1. DISPLAY FIRST FIVE RECORDS
# ==========================================

print("\n========== FIRST FIVE RECORDS ==========")

print(df.head())

# ==========================================
# 2. DATASET INFORMATION
# ==========================================

print("\n========== DATASET INFORMATION ==========")

print(df.info())

# ==========================================
# 3. CHECK DATASET SHAPE
# ==========================================

print("\n========== DATASET SHAPE ==========")

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

# ==========================================
# 4. CHECK COLUMN NAMES
# ==========================================

print("\n========== COLUMN NAMES ==========")

print(df.columns.tolist())

# ==========================================
# 5. CHECK MISSING VALUES
# ==========================================

print("\n========== MISSING VALUES ==========")

print(df.isnull().sum())

# ==========================================
# 6. CHECK DUPLICATE RECORDS
# ==========================================

print("\n========== DUPLICATE RECORDS ==========")

print("Duplicate Records:", df.duplicated().sum())

# ==========================================
# 7. HANDLE MISSING VALUES
# ==========================================

# Fill missing numerical values with median
numeric_columns = df.select_dtypes(
    include=["number"]
).columns

for column in numeric_columns:
    df[column] = df[column].fillna(
        df[column].median()
    )

# Fill missing State values with mode
if df["State"].isnull().any():
    df["State"] = df["State"].fillna(
        df["State"].mode()[0]
    )

# ==========================================
# 8. REMOVE DUPLICATES
# ==========================================

df = df.drop_duplicates()

# ==========================================
# 9. VERIFY CLEANED DATASET
# ==========================================

print("\n========== CLEANED DATASET ==========")

print("Remaining Missing Values:")
print(df.isnull().sum())

print("\nRemaining Duplicate Records:")
print(df.duplicated().sum())

print("\nFinal Dataset Shape:")
print(df.shape)

# ==========================================
# 10. SAVE CLEANED DATASET
# ==========================================

output_path = BASE_DIR / "Dataset" / "cleaned_startups.csv"

df.to_csv(output_path, index=False)

print("\n========== PROJECT COMPLETED ==========")

print("Cleaned dataset saved successfully!")

print("File Location:", output_path)