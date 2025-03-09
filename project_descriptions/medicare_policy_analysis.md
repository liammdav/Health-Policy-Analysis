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

## Results:
- The **OLS regression model** showed a statistically significant relationship between the **policy change** in **2020** and an increase in **Medicare expenditures**. The coefficient for `year_policy` (the policy change variable) was found to be **4.01 million**, suggesting a notable increase in **Medicare costs** as a result of the policy shift.
  
- The model also highlighted that the **cost per enrollee** had a positive impact on the total Medicare expenditure, with the policy change in 2020 resulting in higher costs across the years following its implementation.

- The **R-squared value** of **0.424** indicates that approximately **42.4%** of the variation in **total Medicare costs** can be explained by the model, including the policy change effect and other factors such as the time (year).

- The data visualization produced from this analysis clearly demonstrates a noticeable increase in **Medicare costs** post-2020, with a marked change coinciding with the simulated policy change. This reinforces the model's findings and visually highlights the influence of policy on healthcare spending.

### Key Findings:
1. **Policy Change Impact**: The regression analysis found that the **simulated policy change** in **2020** led to a **significant increase in Medicare costs**. The **coefficient for the year_policy variable** was **4.01 million**, indicating a substantial rise in **Medicare expenditure** following the policy shift.

2. **Correlation with Cost Per Enrollee**: The increase in **cost per enrollee** was a key driver of the rise in **total Medicare costs**. This suggests that even minor changes in per-enrollee costs can have a large impact on overall expenditure.

3. **R-Squared Value**: The **R-squared value** of **0.424** indicates that the model explains **42.4%** of the variation in **total Medicare costs**. While this is a moderate fit, the model still highlights the significant impact of the policy change on Medicare expenditures.

4. **Visual Evidence of Policy Change**: The data visualization showed a clear **increase in Medicare costs after 2020**, aligning with the regression results. This visual representation reinforced the significant role of the policy change in altering **Medicare expenditure** over time.

## Next Steps:
- **Refining the model**: Future work could involve testing the model with **real-world datasets** to improve the accuracy of the policy impact analysis.
- **Advanced econometric techniques**: Implementing advanced regression models (such as **fixed effects** or **time series analysis**) to better account for temporal effects and potential confounders.
- **Sensitivity analysis**: Conducting **sensitivity analysis** to assess how different assumptions about policy change (e.g., varying the magnitude of cost increases) affect the results.

## Full Code for the Project:
[Medicare Policy Impact Analysis Python Script](../python_scripts/medicare_policy_analysis.py)

You can view the code and run it to replicate the analysis on your local machine or explore further.

---

## Conclusion:
This project leverages **Python** to simulate and analyze the impact of a **policy change** on **Medicare expenditures**, employing **econometric modeling** and data visualization techniques to assess the relationship between policy adjustments and healthcare costs.

The analysis revealed a **significant increase in total Medicare costs** following the **policy change in 2020**, as reflected in the regression results and supported by the visual trends in the data. The model demonstrates that small shifts in policy, such as adjustments to the **cost per enrollee**, can lead to substantial increases in **overall healthcare spending**.

These insights are crucial for understanding how future **policy decisions** could shape the trajectory of **Medicare costs** and help inform strategies aimed at controlling expenditures while maintaining coverage. For future work, I plan to expand the analysis by incorporating **real-world datasets** and employing more advanced econometric techniques, such as **fixed effects models** and **time series analysis**, to refine the results and provide deeper insights into policy impacts.

For further questions or comments, please feel free to reach out to me at:  
Email: **liammdav@icloud.com**