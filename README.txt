# Streamlit Data Dashboard

## Overview
This Streamlit web application allows users to upload CSV files, analyze data, handle missing values, apply filters, group data, visualize charts, and download cleaned datasets.

## Features
- Upload CSV files for analysis
- Data preview and summary (describe statistics)
- Null value handling (fill with median for numerical and mode for categorical data)
- Filter data based on column values
- Group-by operations (sum, average, count)
- Interactive visualizations (Bar and Line Charts)
- Download cleaned dataset

## Key Features
1. Data Upload & Preprocessing
CSV & Excel Upload: Users can upload CSV and Excel files to the dashboard for analysis.
Null Value Handling: The app automatically identifies and displays missing values in the dataset. Users can choose to fill missing values using the median (for numeric columns) and mode (for categorical columns).
Data Cleaning: Provides an option to fill or update missing data within the dataset for accurate analysis.
2. Data Preview & Summary
Preview Data: Users can preview the first few rows of the dataset to verify the data they are working with.
Statistical Summary: The app shows basic summary statistics, such as mean, median, min, max, and standard deviation for numeric columns.
3. Data Filtering
Dynamic Filtering: Users can select any column and filter the dataset based on specific values. The filtered data is then displayed for further analysis.
4. Group-by and Aggregation
Group Data: Users can perform grouping on categorical columns and calculate aggregations like sum, average, and count of numerical values.
Interactive Analysis: Visualizes aggregated data to gain insights into different categories and their corresponding values.
5. Data Visualization
Bar Chart and Line Chart: Users can generate dynamic bar and line charts for visual data analysis. Customization options allow for selecting columns for the x-axis and y-axis.
Visualization Updates: Instantly updates visualizations based on user input, allowing for quick insights into trends or anomalies.
6. Download Cleaned Data
Cleaned Data Export: Once null values are handled, users can download the cleaned version of the dataset as a CSV file for further use.
7. User Contact Form
Contact Us: A form where users can submit their name, email, and message to get in touch for inquiries, feedback, or support.
Data Storage: Submitted messages are stored in a Google Sheet for easy management and response.

