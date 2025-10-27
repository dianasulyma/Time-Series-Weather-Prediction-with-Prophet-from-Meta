## 🌦️ Time Series Prediction of Weather Patterns in Vancouver, BC

This project implements **time-series analysis and forecasting** using **Meta's Prophet** model on historical weather data from Vancouver, BC.


### 📊 Data

The dataset originates from the [**Government of Canada's Historical Climate Data**](https://climate.weather.gc.ca) portal.  
It encompases **1970–2020** and includes daily records of key weather variables such as:

- Maximum and minimum temperature  
- Snowfall  
- Precipitation
- Rain
- Other daily meteorological measurements  

A total of **50 yearly files** were downloaded for the Vancouver Harbour weather station (one per year from 1970–2020).  
These were combined into a **single dataset** for analysis and model training.


### 🧠 Prediction Model

**Prophet** is an open-source forecasting library developed by **Meta**.  
It is based on a *Generalized Additive Model (GAM)* and is particularly effective for capturing complex **seasonality** patterns—daily, weekly, monthly, and yearly trends (Kwarteng & Andreevich, 2024).

Prophet requires minimal preprocessing and generates forecasts with **prediction intervals**, providing estimates of uncertainty around future values (Kwarteng & Andreevich, 2024).
