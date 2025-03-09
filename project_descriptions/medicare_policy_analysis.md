# Medicare Policy Impact Analysis

## Project Overview
The **Medicare Policy Impact Analysis** project simulates the effect of policy changes on healthcare costs, focusing specifically on **Medicare** expenditures in the United States. This analysis examines data over a period from **2010 to 2024**, analyzing how a simulated **policy change** starting in **2020** impacts total healthcare costs.

In this project, we simulate data for **five U.S. states**: **California (CA)**, **Texas (TX)**, **New York (NY)**, **Florida (FL)**, and **Illinois (IL)**. The simulation introduces a policy change in **2020**, which is hypothesized to increase the **cost per enrollee** for Medicare recipients.

## Key Steps in the Analysis:
1. **Data Generation**: Simulated data is generated for 500 data points, with yearly records spanning from **2010 to 2024**. The data includes information such as the number of **Medicare enrollees**, **cost per enrollee**, and whether there was a **policy change** in that year.
   
2. **Policy Change Simulation**: A simulated policy change occurs starting in **2020**, which results in an increase in the **cost per enrollee**. This increase is intended to reflect the effects of policy decisions on Medicare costs.

3. **Econometric Analysis**: Using **Python** and the **Statsmodels** library, the data undergoes **OLS regression analysis** to assess the impact of policy changes on the **total Medicare costs** over time.

4. **Data Visualization**: A line plot is generated to visualize the trend in **total Medicare costs** over the years, with a marked line indicating when the policy change took place in **2020**. This helps to illustrate how the policy shift influences Medicare expenditures.

## Key Technologies Used:
- **Python 3** for data analysis and programming
- **Pandas** for data manipulation and cleaning
- **NumPy** for generating random numbers and numerical operations
- **Statsmodels** for econometric modeling (Ordinary Least Squares regression)
- **Matplotlib** and **Seaborn** for data visualization and generating the trend plot

## Results and Insights:
- The **OLS regression model** estimates the relationship between **policy changes** and the **total Medicare costs**. It highlights whether and how the policy change in 2020 influenced the total costs.
- The data visualization shows the trend in **Medicare costs over time**, particularly the increase in costs following the simulated policy change in 2020.
  
### Key Findings:
- There was a noticeable **increase in total Medicare costs** after 2020, reflecting the impact of the simulated policy change.
- The model suggests that policy changes such as increased **cost per enrollee** can lead to substantial changes in the **overall healthcare expenditure** over time.

## Next Steps:
- **Refining the model**: Future work could involve testing the model with **real-world datasets** to improve the accuracy of the policy impact analysis.
- **Advanced econometric techniques**: Implementing advanced regression models (such as **fixed effects** or **time series analysis**) to better account for temporal effects and potential confounders.
- **Sensitivity analysis**: Conducting **sensitivity analysis** to assess how different assumptions about policy change (e.g., varying the magnitude of cost increases) affect the results.

## Full Code for the Project:
[Medicare Policy Impact Analysis Python Script](../python_scripts/medicare_policy_analysis.py)

You can view the code and run it to replicate the analysis on your local machine or explore further.

---

## Conclusion:
This project demonstrates the use of **Python** for health policy analysis, employing data simulation, econometric modeling, and visualization techniques. It showcases how **policy changes** can impact key metrics such as **Medicare spending**, and how such analyses can guide decision-making in the healthcare sector.

For further questions or comments, please feel free to reach out to me at:  
Email: **liammdav@icloud.com**