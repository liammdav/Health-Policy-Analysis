import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import os

# Ensure the necessary folder exists
os.makedirs('results/medicare_policy_analysis_results', exist_ok=True)

np.random.seed(42)
n = 500

years = np.arange(2010, 2025)
states = ['CA', 'TX', 'NY', 'FL', 'IL']

years_expanded = np.tile(years, int(np.ceil(n / len(years))))[:n]
states_expanded = np.random.choice(states, size=n)

# Simulated Medicare Data
data = pd.DataFrame({
    'year': years_expanded,  
    'state': states_expanded, 
    'enrollees': np.random.randint(50000, 200000, size=n),  
    'cost_per_enrollee': np.random.uniform(8000, 15000, size=n), 
})

# Simulated policy change in 2020
data['policy_change'] = (data['year'] >= 2020).astype(int)  # 1 after 2020, 0 before 2020

# Simulated effect of policy change: cost increase after 2020
data['cost_per_enrollee'] += data['policy_change'] * np.random.uniform(500, 1000, size=n)

# Calculate total cost
data['total_cost'] = data['enrollees'] * data['cost_per_enrollee']

# Aggregate data by year
agg_data = data.groupby('year').agg({
    'total_cost': 'sum',
    'enrollees': 'sum'
}).reset_index()

# Add interaction term between year and policy change
agg_data['year_policy'] = agg_data['year'] * agg_data['year'].apply(lambda x: 1 if x >= 2020 else 0)

# Econometric Modeling -- Regression analysis (OLS)
X = agg_data[['year', 'year_policy']]  # Include interaction term
X = sm.add_constant(X)  # Add intercept
y = agg_data['total_cost']

# Fit OLS model
model = sm.OLS(y, X).fit()

# Save model summary to text file
with open('results/medicare_policy_analysis_results/model_summary.txt', 'w') as f:
    f.write(model.summary().as_text())

# Visualization of Medicare Costs (Aggregated by Year)
plt.figure(figsize=(10, 6))
sns.lineplot(data=agg_data, x='year', y='total_cost', marker="o", label="Total Cost")
plt.axvline(x=2020, color='r', linestyle='--', label='Policy Change (2020)')
plt.title("Total Medicare Cost Trends (Aggregated by Year)")
plt.xlabel("Year")
plt.ylabel("Total Medicare Cost")
plt.legend()

# Save the plot to the results folder
plt.savefig('results/medicare_policy_analysis_results/medicare_cost_trends.png')
plt.close()  # Close the plot to prevent it from displaying in interactive mode

# Optionally, save the aggregated data to a CSV file
agg_data.to_csv('results/medicare_policy_analysis_results/medicare_aggregated_data.csv', index=False)

print("Medicare Policy Analysis Complete")