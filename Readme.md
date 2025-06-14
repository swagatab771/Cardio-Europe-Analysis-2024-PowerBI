
# 📊 Mortality Patterns of Heart Attacks

This Power BI dashboard explores and visualizes temporal and geographical trends in heart attack-related mortality, offering critical insights for healthcare analysis, policy planning, and predictive modeling. This project helped me demonstrate analytical, forecasting, and data storytelling skills during my interview at Eurac Research.

![image](https://github.com/user-attachments/assets/0c1a9444-6d9a-4711-8a75-0c945f6bf1dc)


## 🩺 Objective
To analyze heart attack mortality patterns across time, identify anomalies, forecast future trends (2023–2025), and provide insights into the effect of medical interventions and demographic dynamics.

### 📅 Are 2023 Data Available?
As of the time of this project:

No, actual data for 2024–2025 was not yet released.

I implemented forecasting models to estimate future mortality trends from 2024 to 2025, based on historical patterns.

#### 🔮 How Forecasting Was Done (2023–2025)
Forecasting Model Used

* I utilized Power BI's built-in exponential smoothing forecast (ETS) available under the Analytics pane in line charts.

* Additionally, I used a Python-based approach combining Facebook Prophet and pmdarima for more robust forecasting and model comparison.


This provided a sufficient time window to detect long-term trends and cyclical behavior.

Power BI automatically detected yearly seasonality patterns.

In Python, *Prophet* was configured to account for yearly seasonality, and *pmdarima* auto-ARIMA helped choose optimal seasonal and non-seasonal parameters.

A 95% confidence interval was applied in both Power BI and Python models to reflect prediction uncertainty and offer decision boundaries.

#### Custom Forecast Script

You can find the Python script in the file:
*find_mortality_trend_by_year.py*

This script allows you to:

* Input an existing CSV dataset
* Define the number of future years for forecasting
* Compare visual and statistical accuracy across both Prophet and ARIMA models

📌 Note: This explanation is data-driven but relies on assumptions from historical trends in the absence of actual 2023+ data.

### Data Source
Public health databases like WHO, Eurostat, and OECD.
