import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('results/hospital_financing_analysis_results', exist_ok=True)

np.random.seed(42)
n = 500

years = np.arange(2010, 2025)  # Years from 2010 to 2024
states = ['CA', 'TX', 'NY', 'FL', 'IL']
years_expanded = np.tile(years, int(np.ceil(n / len(years))))[:n]
states_expanded = np.random.choice(states, size=n)

# Simulated reimbursement rates and hospital profitability
medicare_reimbursement = np.random.uniform(5000, 10000, size=n)  
private_insurance_reimbursement = np.random.uniform(10000, 20000, size=n)  

# Simulated hospital profitability based on reimbursement rates and patient volume
hospital_profitability_medicare = (medicare_reimbursement * np.random.uniform(0.5, 2, size=n))  
hospital_profitability_private = (private_insurance_reimbursement * np.random.uniform(1, 3, size=n))  

data = pd.DataFrame({
    'year': years_expanded,
    'state': states_expanded,
    'medicare_reimbursement': medicare_reimbursement,
    'private_insurance_reimbursement': private_insurance_reimbursement,
    'hospital_profitability_medicare': hospital_profitability_medicare,
    'hospital_profitability_private': hospital_profitability_private
})

# Visualization of Hospital Profitability vs Reimbursement Rates
plt.figure(figsize=(10, 6))

sns.scatterplot(x=data['medicare_reimbursement'], y=data['hospital_profitability_medicare'], label='Medicare Reimbursement', color='b')
sns.scatterplot(x=data['private_insurance_reimbursement'], y=data['hospital_profitability_private'], label='Private Insurance Reimbursement', color='g')

plt.title('Hospital Profitability vs. Reimbursement Rates')
plt.xlabel('Reimbursement Rate')
plt.ylabel('Hospital Profitability')
plt.legend(title='Reimbursement Type')


plt.savefig('results/hospital_financing_analysis_results/hospital_profitability_vs_reimbursement.png')
plt.close()  # Close the plot to prevent it from displaying in interactive mode
data.to_csv('results/hospital_financing_analysis_results/hospital_financing_data.csv', index=False)
