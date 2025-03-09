import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import os

os.makedirs('results/health_policy_simulation_results', exist_ok=True)

np.random.seed(42)
years = np.arange(2015, 2035)  

# Policy change using a sigmoid function
def sigmoid_policy(year, midpoint=2024, k=1):
    return 1 / (1 + np.exp(-k * (year - midpoint)))

policy_change = np.array([sigmoid_policy(y, 2024, 1.2) for y in years])

# Simulating public healthcare coverage (% population covered)
base_public_coverage = 30 + 0.5 * (years - 2015)  
policy_effect = 10 * policy_change  
public_coverage = base_public_coverage + policy_effect + np.random.normal(0, 2, len(years))

# Simulating private insurance coverage (inverse of public coverage)
private_coverage = 100 - public_coverage + np.random.normal(0, 2, len(years))

# DataFrame
df = pd.DataFrame({'Year': years, 'Public Coverage': public_coverage, 
                   'Private Coverage': private_coverage, 'Policy Change': policy_change})

# OLS Regression
X = sm.add_constant(df[['Year', 'Policy Change']])  
y = df['Public Coverage']
model = sm.OLS(y, X).fit()

# Visualization for policy change intensity
plt.figure(figsize=(12, 5))
sns.lineplot(x=df['Year'], y=df['Policy Change'], label="Policy Change Intensity", color="red")
plt.xlabel("Year")
plt.ylabel("Policy Change Factor (0 to 1)")
plt.title("Gradual Implementation of Universal Healthcare")
plt.grid()
plt.savefig('results/health_policy_simulation_results/policy_change_intensity.png')
plt.close()

# Visualization for coverage rates
plt.figure(figsize=(12, 6))
sns.lineplot(x=df['Year'], y=df['Public Coverage'], label="Public Coverage (%)", color="blue")
sns.lineplot(x=df['Year'], y=df['Private Coverage'], label="Private Coverage (%)", color="green")
plt.axvline(x=2024, linestyle="--", color="red", label="Policy Implemented")
plt.xlabel("Year")
plt.ylabel("Coverage (%)")
plt.title("Impact of Universal Healthcare on Coverage Rates")
plt.legend()
plt.grid()
plt.savefig('results/health_policy_simulation_results/coverage_rates.png')
plt.close()

with open('results/health_policy_simulation_results/ols_summary.txt', 'w') as f:
    f.write(model.summary().as_text())