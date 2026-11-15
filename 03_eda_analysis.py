import pandas as pd
from pathlib import Path

# ==========================================
# PRDA-01: STARTUP PROFIT ANALYSIS
# EXPLORATORY DATA ANALYSIS
# ==========================================

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load cleaned dataset
file_path = BASE_DIR / "Dataset" / "cleaned_startups.csv"

df = pd.read_csv(file_path)

# ==========================================
# 1. DESCRIPTIVE STATISTICS
# ==========================================

print("\n========== DESCRIPTIVE STATISTICS ==========")

print(df.describe())

# ==========================================
# 2. MEAN
# ==========================================

print("\n========== MEAN VALUES ==========")

print(df.mean(numeric_only=True))

# ==========================================
# 3. MEDIAN
# ==========================================

print("\n========== MEDIAN VALUES ==========")

print(df.median(numeric_only=True))

# ==========================================
# 4. STANDARD DEVIATION
# ==========================================

print("\n========== STANDARD DEVIATION ==========")

print(df.std(numeric_only=True))

# ==========================================
# 5. STATE-WISE STARTUP COUNT
# ==========================================

print("\n========== STATE-WISE STARTUP COUNT ==========")

print(df["State"].value_counts())

# ==========================================
# 6. STATE-WISE AVERAGE PROFIT
# ==========================================

print("\n========== STATE-WISE AVERAGE PROFIT ==========")

state_profit = df.groupby("State")["Profit"].mean()

print(state_profit)

# ==========================================
# 7. STATE-WISE TOTAL PROFIT
# ==========================================

print("\n========== STATE-WISE TOTAL PROFIT ==========")

print(df.groupby("State")["Profit"].sum())

# ==========================================
# 8. CORRELATION ANALYSIS
# ==========================================

print("\n========== CORRELATION MATRIX ==========")

correlation = df.corr(numeric_only=True)

print(correlation)

# ==========================================
# 9. CORRELATION WITH PROFIT
# ==========================================

print("\n========== CORRELATION WITH PROFIT ==========")

profit_correlation = correlation["Profit"].sort_values(
    ascending=False
)

print(profit_correlation)

# ==========================================
# 10. SAVE EDA RESULTS
# ==========================================

reports_folder = BASE_DIR / "Reports"

reports_folder.mkdir(exist_ok=True)

correlation.to_csv(
    reports_folder / "correlation_matrix.csv"
)

state_profit.to_csv(
    reports_folder / "state_wise_average_profit.csv"
)

df.describe().to_csv(
    reports_folder / "descriptive_statistics.csv"
)

print("\n========== EDA COMPLETED ==========")

print("EDA results saved successfully!")