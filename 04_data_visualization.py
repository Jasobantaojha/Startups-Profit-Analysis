
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ==========================================
# PRDA-01: STARTUP PROFIT ANALYSIS
# DATA VISUALIZATION
# ==========================================

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load cleaned dataset
file_path = BASE_DIR / "Dataset" / "cleaned_startups.csv"
df = pd.read_csv(file_path)

# Create visualization folder
output_folder = BASE_DIR / "Visualizations"
output_folder.mkdir(exist_ok=True)

# Visualization style
sns.set_theme(style="whitegrid")

print("Starting Data Visualization...")

# ==========================================
# 1. CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(10, 7))

correlation = df.corr(numeric_only=True)

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap - Startup Profit Analysis")
plt.tight_layout()

plt.savefig(output_folder / "01_correlation_heatmap.png", dpi=300)
plt.show()
plt.close()

# ==========================================
# 2. R&D SPEND VS PROFIT
# ==========================================

plt.figure(figsize=(9, 6))

sns.regplot(
    data=df,
    x="R&D Spend",
    y="Profit",
    scatter_kws={"color": "blue"},
    line_kws={"color": "red"}
)

plt.title("R&D Spend vs Profit")
plt.xlabel("R&D Spend")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig(output_folder / "02_rd_spend_vs_profit.png", dpi=300)
plt.show()
plt.close()

# ==========================================
# 3. ADMINISTRATION VS PROFIT
# ==========================================

plt.figure(figsize=(9, 6))

sns.regplot(
    data=df,
    x="Administration",
    y="Profit",
    scatter_kws={"color": "green"},
    line_kws={"color": "red"}
)

plt.title("Administration vs Profit")
plt.xlabel("Administration Spending")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig(output_folder / "03_administration_vs_profit.png", dpi=300)
plt.show()
plt.close()

# ==========================================
# 4. MARKETING SPEND VS PROFIT
# ==========================================

plt.figure(figsize=(9, 6))

sns.regplot(
    data=df,
    x="Marketing Spend",
    y="Profit",
    scatter_kws={"color": "purple"},
    line_kws={"color": "red"}
)

plt.title("Marketing Spend vs Profit")
plt.xlabel("Marketing Spending")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig(output_folder / "04_marketing_spend_vs_profit.png", dpi=300)
plt.show()
plt.close()

# ==========================================
# 5. STATE-WISE AVERAGE PROFIT
# ==========================================

plt.figure(figsize=(9, 6))

state_profit = df.groupby("State")["Profit"].mean().sort_values(
    ascending=False
)

sns.barplot(
    x=state_profit.index,
    y=state_profit.values
)

plt.title("State-wise Average Startup Profit")
plt.xlabel("State")
plt.ylabel("Average Profit")

plt.tight_layout()
plt.savefig(output_folder / "05_state_wise_profit.png", dpi=300)
plt.show()
plt.close()

# ==========================================
# 6. R&D SPENDING DISTRIBUTION
# ==========================================

plt.figure(figsize=(9, 6))

sns.histplot(
    df["R&D Spend"],
    kde=True
)

plt.title("R&D Spending Distribution")
plt.xlabel("R&D Spend")
plt.ylabel("Number of Startups")

plt.tight_layout()
plt.savefig(output_folder / "06_rd_distribution.png", dpi=300)
plt.show()
plt.close()

# ==========================================
# 7. ADMINISTRATION DISTRIBUTION
# ==========================================

plt.figure(figsize=(9, 6))

sns.histplot(
    df["Administration"],
    kde=True
)

plt.title("Administration Spending Distribution")
plt.xlabel("Administration Spending")
plt.ylabel("Number of Startups")

plt.tight_layout()
plt.savefig(output_folder / "07_administration_distribution.png", dpi=300)
plt.show()
plt.close()

# ==========================================
# 8. MARKETING SPENDING DISTRIBUTION
# ==========================================

plt.figure(figsize=(9, 6))

sns.histplot(
    df["Marketing Spend"],
    kde=True
)

plt.title("Marketing Spending Distribution")
plt.xlabel("Marketing Spend")
plt.ylabel("Number of Startups")

plt.tight_layout()
plt.savefig(output_folder / "08_marketing_distribution.png", dpi=300)
plt.show()
plt.close()

# ==========================================
# PROJECT COMPLETED
# ==========================================

print("\n===================================")
print("DATA VISUALIZATION COMPLETED")
print("===================================")

print("All 8 charts saved successfully!")

print("Location:", output_folder)
