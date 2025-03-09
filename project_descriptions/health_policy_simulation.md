# Universal Healthcare Policy Simulation

## Project Overview
The **Universal Healthcare Policy Simulation** models the gradual implementation of a universal healthcare policy and its impact on **public** and **private healthcare coverage rates**. Using econometric modeling, the project examines how policy changes influence coverage distribution over time, with the adoption of the policy modeled via a **sigmoid function**.

## Key Steps in the Simulation:
1. **Data Generation**: Simulated data for **2015–2035** includes **public coverage**, **private coverage**, and **policy change intensity**, modeled with a **sigmoid function**.
2. **Policy Change Simulation**: A **sigmoid function** models the **gradual implementation** of universal healthcare, peaking in **2024**.
3. **Econometric Analysis**: **OLS regression analysis** explores the relationship between **policy change** and **public healthcare coverage**.
4. **Data Visualization**: **Line plots** visualize **policy change intensity** and the **impact on public and private coverage**.

## Key Technologies Used:
- **Python 3** for data analysis
- **NumPy**, **Pandas** for data manipulation
- **Statsmodels** for regression analysis
- **Matplotlib**, **Seaborn** for data visualization

## Results:
The econometric analysis and simulation yield the following key insights:

- **OLS Regression Results**:  
  The **R-squared** value of **0.950** indicates that the model explains **95% of the variation** in public healthcare coverage. The policy change has a statistically significant and positive effect on public coverage, with a **coefficient** of **7.17**, indicating that each unit increase in the policy change intensity results in an increase in public coverage by **7.17 units**.

- **Inverse Relationship**:  
  As public coverage rises due to the policy change, private insurance coverage declines. The **sigmoid function** successfully captures this gradual and inverse shift in coverage over time, reflecting the typical outcomes of universal healthcare policies.

- **Significance of Results**:  
  The **F-statistic** of **161.4** and the **p-values** for the policy change and year variables (**p < 0.05**) indicate that the findings are statistically significant and that the policy change is a critical factor driving the increase in public coverage.

### Key Findings:
1. **Gradual Increase in Public Coverage**:  
   The simulation shows that the implementation of the universal healthcare policy leads to a steady increase in **public healthcare coverage**. As the policy is phased in, starting from 2024, the public coverage rate rises consistently, reflecting the effects of the policy change.

2. **Decline in Private Insurance Coverage**:  
   The implementation of the policy results in a corresponding decrease in **private insurance coverage**, as more individuals switch to public coverage. The inverse relationship between public and private coverage is clearly observed, with private insurance rates decreasing as public coverage increases.

3. **Sigmoid Function**:  
   The **sigmoid function** accurately captures the gradual adoption of the policy over time, with a peak in **2024**. This function effectively models the real-world scenario of a phased implementation, where the policy change gains momentum before stabilizing.

4. **Policy Change Impact**:  
   The **OLS regression analysis** reveals that the policy change is statistically significant in both its impact on public coverage (with a coefficient of **7.17**) and the increase in public healthcare coverage over time. The regression results indicate a strong and positive relationship between the **policy change** and **public coverage**.

## Next Steps:
- **Model refinement**: Test with real-world data for validation.
- **Add more factors**: Incorporate **economic** and **demographic variables**.
- **Alternative simulations**: Explore different adoption rates and policy scenarios.

## Full Code for the Project:
[Universal Healthcare Policy Simulation Python Script](../python_scripts/health_policy_simulation.py)

You can view the code and run it to replicate the analysis on your local machine or explore further.

---

## Conclusion:
The **Universal Healthcare Policy Simulation** provides a comprehensive analysis of the potential effects of a **gradual universal healthcare policy** on **coverage rates**. Through the application of a **sigmoid function** to model policy adoption and **OLS regression** to analyze the impact on public coverage, the simulation shows that the policy change significantly increases public coverage while decreasing private insurance coverage.

The results suggest that a gradual shift towards universal healthcare, starting from 2024, could substantially increase public healthcare coverage, highlighting the effectiveness of the policy in achieving broader coverage. The inverse relationship with private insurance coverage emphasizes the trade-off between public and private funding mechanisms in the healthcare system.

These findings offer valuable insights for policymakers considering the phased implementation of universal healthcare. Future work could focus on refining the model with real-world data, incorporating additional variables such as **economic conditions** and **demographic factors**, and testing alternative policy scenarios to better understand the long-term implications of universal healthcare adoption.

For further questions or comments, please reach out to me at:  
Email: **liammdav@icloud.com**
