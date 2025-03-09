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

## Results and Insights:
- **Sigmoid function** shows the **gradual adoption** of universal healthcare starting in 2024.
- **OLS regression** reveals that the **policy change** significantly increases **public coverage** and decreases **private coverage**.
- **Visualization** highlights the inverse relationship between public and private insurance coverage.

### Key Findings:
- The **policy change** leads to a steady increase in **public healthcare coverage**, reducing **private insurance** coverage.
- The **sigmoid function** captures the phased policy adoption effectively.

## Next Steps:
- **Model refinement**: Test with real-world data for validation.
- **Add more factors**: Incorporate **economic** and **demographic variables**.
- **Alternative simulations**: Explore different adoption rates and policy scenarios.

## Full Code for the Project:
[Universal Healthcare Policy Simulation Python Script](../python_scripts/health_policy_simulation.py)

You can view the code and run it to replicate the analysis on your local machine or explore further.

---

## Conclusion:
This project demonstrates the potential effects of a **gradual universal healthcare policy** on **coverage rates**. By modeling the policy’s implementation and using **OLS regression**, the simulation provides insights into the relationship between policy adoption and healthcare coverage.

For further questions or comments, please reach out to me at:  
Email: **liammdav@icloud.com**
