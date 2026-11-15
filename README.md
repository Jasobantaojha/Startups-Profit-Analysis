# Startups-Profit-Analysis

STARTUP PROFIT
ANALYSIS
PRDA–01 Project Analysis Report
Multiple Linear Regression | Profit Prediction | Power BI Visualization
Prepared by: JASOBANTA OJHA
Dataset: 50_Startups.csv
Coverage: 50 startups in New York, California and Florida
Target variable: Profit
Prepared as the detailed analysis report for the PRDA–01 assignment.

 1. Executive Summary
This project studies how expenditure on Research and Development (R&D), Administration and Marketing is related to the profit earned by startups. The supplied 50_Startups.csv dataset contains 50 startup observations from New York, California and Florida. Multiple linear regression was used to estimate the relationship between the three spending variables and Profit, and to predict profit for the two input cases specified in the assignment. The reported Python test-set R² is 0.900065, while the Excel regression using all 50 observations reports an in-sample R² of 0.950746.
2. Problem Statement and Objectives
The assignment asks for an analysis of how money spent on Marketing, R&D and Administration affects company Profit. It also requires profit predictions for two specified sets of spending inputs, visualizations using Tableau or Power BI, and business insights and suggestions.
The main objectives are to:
•	Understand the supplied startup dataset and its variables.
•	Explore the relationship between each spending variable and Profit.
•	Fit a multiple linear regression model using R&D Spend, Administration and Marketing Spend.
•	Evaluate model performance and estimate profit for the two assignment inputs.
•	Present findings through visualizations and practical recommendations.
3. Dataset Description
The analysis uses the supplied CSV file, 50_Startups.csv. The assignment describes the data as covering 50 startups located in New York, California and Florida. The dataset has five fields: R&D Spend, Administration, Marketing Spend, State and Profit. The project overview records 50 rows and no missing values in these five fields.
Attribute	Description	Role in this analysis
R&D Spend	Amount spent on research and development.	Predictor
Administration	Amount spent on administration.	Predictor
Marketing Spend	Amount spent on marketing strategies.	Predictor
State	State in which the startup is located.	Categorical / grouping field
Profit	Profit earned by the startup.	Target variable

For the regression model reported here, Profit is the dependent variable (Y), and R&D Spend, Administration and Marketing Spend are the independent variables (X). State is included in the descriptive and visualization analysis; it is not listed among the three predictors in the reported regression results.
4. Methodology
The analysis follows a sequence of data review, exploratory visualization, regression modelling, model evaluation, prediction and interpretation. Multiple linear regression was selected because the task examines the relationship between one numeric outcome (Profit) and three spending predictors.
Two model evaluation results are reported from the project work. The Excel regression uses all 50 observations and gives an in-sample R² of 0.950746. The Python workflow uses an 80/20 train-test split with random_state = 42 and reports test-set performance. These R² values describe different evaluation setups and should not be treated as directly interchangeable.
5. Regression Results
Evaluation / metric	Reported result
Excel regression R² (all 50 observations; in-sample)	0.950746
Python test-set R² (80/20 split; random_state = 42)	0.900065
Python test-set MAE	6,979.15
Python test-set RMSE	8,995.91

The Excel in-sample R² indicates that the fitted regression accounts for a large proportion of the variation in Profit within the data used to fit that regression. The Python test R² indicates that the model also achieved a strong fit on the held-out test observations in that run. MAE is the mean absolute prediction error, while RMSE gives greater weight to larger errors. These error values are expressed in the same units as Profit.
6. Regression Coefficients and Interpretation
Predictor	Python coefficient	Direction
R&D Spend	0.803779	Positive
Administration	-0.067929	Negative
Marketing Spend	0.031242	Positive

In the fitted Python model, R&D Spend has the largest positive coefficient. Marketing Spend also has a positive coefficient, while Administration has a negative coefficient. These coefficient signs describe the model's estimated relationships when the other predictors are held constant. Coefficient magnitudes should be interpreted carefully because the predictors are measured on different scales. A coefficient by itself does not prove that changing a spending category will cause a particular change in profit.
7. Profit Predictions for the Assignment Inputs
The following predicted profits are the outputs reported by the project's Python regression workflow for the two input combinations specified in the assignment.
Input case	R&D Spend	Administration	Marketing Spend	Predicted Profit
Company 1	21,892.92	81,910.77	164,270.70	70,037.90
Company 2	23,940.93	96,489.63	137,001.10	70,554.57

The model predicts a profit of 70,037.90 for Company 1 and 70,554.57 for Company 2. These are estimates produced by the fitted model, not guaranteed actual profits.
8. Visualization and Descriptive Findings
The project visualization work uses the startup data to examine Profit by State and the relationships between Profit and each spending variable. The dashboard and charts are intended to make comparisons and patterns easier to interpret.
•	State comparison: the project aggregation shows New York with the highest total profit and California with the lowest total profit in this particular sample.
•	Spending relationships: scatter plots are used to inspect how Profit varies with R&D Spend, Administration and Marketing Spend across the 50 startups.
•	Dashboard use: Power BI or Tableau visuals should be included as screenshots in the submission to provide visual evidence of the analysis.
State totals are descriptive results for these 50 observations. They do not establish that a startup's state or location causes it to earn higher or lower profit. Likewise, scatter plots show observed associations and should be interpreted together with the regression results.
9. Key Insights
•	R&D Spend has a positive coefficient and is the strongest positive coefficient in the reported Python model.
•	Marketing Spend has a positive coefficient, suggesting a positive estimated relationship with Profit in this fitted model.
•	Administration has a negative coefficient in the fitted Python model; this is a reason to review administrative cost efficiency, not proof that all administrative spending reduces profit.
•	The model reports a test-set R² of 0.900065, with MAE of 6,979.15 and RMSE of 8,995.91 in the project run.
•	The two assignment cases have predicted profits of 70,037.90 and 70,554.57 respectively.
•	The dataset is limited to 50 startups in three states, so findings should not automatically be generalized to all startups.
10. Recommendations
•	Evaluate R&D projects carefully because R&D Spend has the strongest positive coefficient in the fitted model. Track project outcomes and returns rather than increasing spending without evaluation.
•	Review marketing campaigns by channel and measure the revenue and profit generated by each campaign. Continue or expand activities that demonstrate measurable returns.
•	Review administrative expenses for efficiency and identify avoidable costs while maintaining the staff and systems needed to operate effectively.
•	Use the regression model as a decision-support aid, not as the sole basis for investment or budgeting decisions.
•	Collect more startup observations and, where possible, data from additional periods and locations before relying on the model for broader decisions.
•	Reassess model performance with new data and compare predicted profit with actual profit over time.
11. Limitations
•	The dataset contains only 50 startup observations.
•	The data cover three states and may not represent startups in other regions or industries.
•	The regression coefficients describe estimated associations and do not establish cause and effect.
•	The reported predictions are model estimates and may differ from actual future profit.
•	The coefficient sizes are affected by the different measurement scales of the predictors.
•	The project results should be validated using additional data before major business decisions are made.
12. Conclusion
The PRDA–01 Startup Profit Analysis examined the relationship between R&D Spend, Administration and Marketing Spend and startup Profit using multiple linear regression. The project reports an Excel in-sample R² of 0.950746 and a Python test-set R² of 0.900065. In the Python model, R&D Spend and Marketing Spend have positive coefficients, while Administration has a negative coefficient. The model predicts profits of 70,037.90 and 70,554.57 for the two input cases in the assignment. The visual analysis also compares profit across the three states and explores spending-profit patterns. Overall, the model can support preliminary analysis, but its results should be treated with caution and validated with a larger, more representative dataset.
13. Submission Attachments
Attach the following supporting items separately when submitting this report, as required by the assignment: (1) Dataset Source Confirmation selecting CSV, (2) the project PowerPoint, (3) regression output if available (optional), and (4) screenshots of the Tableau or Power BI dashboard. This report is the detailed analysis report file.
