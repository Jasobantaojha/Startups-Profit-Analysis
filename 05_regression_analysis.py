import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Load dataset
df = pd.read_csv("Dataset/cleaned_startups.csv")

# Select input and output features
X = df[['R&D Spend', 'Administration', 'Marketing Spend']]
y = df['Profit']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)

print("\nREGRESSION ANALYSIS RESULTS")
print("---------------------------")
print("R2 Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred) ** 0.5)

print("\nRegression Coefficients:")
for name, value in zip(X.columns, model.coef_):
    print(name, ":", value)

# Train final model using all available data
final_model = LinearRegression()
final_model.fit(X, y)

# Assignment prediction inputs
new_data = pd.DataFrame([
    [21892.92, 81910.77, 164270.7],
    [23940.93, 96489.63, 137001.1]
], columns=X.columns)

predictions = final_model.predict(new_data)

print("\nPROFIT PREDICTIONS")
for i, value in enumerate(predictions, start=1):
    print(f"Company {i} Predicted Profit: {value:.2f}")