### Time series prediction of weather patterns in Vancouver, BC. 

This project implements time-series analysis and prediction using Meta's Prophet model on weather data in Vancouver, BC. 

#### Data 

The data for this project comes from **Historical Climate Data**, accessible via https://climate.weather.gc.ca/. The data we will use spans 1970-2020 and includes fields for various daily weather and temperature measurements (snow, precipitation, max/min temperature, wind speed, etc.).  

We downloaded 50 files from the Government of Canada Historical Climate Data webpage, one file per year from 1970 to 2020. We combined this dataset into a single file for easier analysis and modelling. 


<img width="442" height="331" alt="combined_files" src="https://github.com/user-attachments/assets/5487b566-f948-42c7-9084-e229b15cf8e0" />

#### Prediction Model
Prophet is an open-source forecasting tool developed by Meta. It is based on GAM (Generalized Additive Model). It is capable of handling seasonal changes granularly, meaning it can detect seasonality at the day, week, month, and year levels (Kwarteng & Andreevich, 2024). Prophet requires minimal data preprocessing and provides uncertainty estimates via prediction intervals (Kwarteng & Andreevich, 2024).