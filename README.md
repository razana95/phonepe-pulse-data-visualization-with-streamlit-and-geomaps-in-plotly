# PhonePe Pulse Data Visualization with Streamlit and Geomaps in Plotly

This project aims to visualize the data from the PhonePe Pulse GitHub repository (https://github.com/PhonePe/pulse) using Streamlit and Plotly in Python. The goal is to extract real data from the PhonePe Pulse GitHub page, process the data, and generate valuable insights through interactive visualizations.

## Project Overview

The project involves the following processes:

Extracting dataframes from the PhonePe Pulse GitHub repository using the pandas dataframe.
Uploading the extracted dataframes into SQL Workbench using SQLalchemy and pymysql.
Loading the dataframes from the SQL tables back into pandas.
Visualizing the data using geomaps functions in Plotly.
The main component of the project is a dashboard created with Streamlit, which showcases the visualizations and insights derived from the PhonePe Pulse data.

## Dashboard Components

The dashboard consists of the following main components:

**Geo Visualization**: This section includes 
a)choropleth maps of Indian states to display overall transaction details for each year. 
b)It also features scattergeo maps of all districts within each state, showing transaction details at the district level. 
c)Additionally, there is a line map illustrating the overall growth of PhonePe over the years, and
d)A hidden bar graph highlighting the top states with higher transactions.

**Transaction Analysis**: This section is further divided into three categories:
a) State Analysis: Analyzes transaction details at the state level.
b) District Analysis: Provides insights into transaction details at the district level.
c) Year Analysis: Focuses on transaction analysis over different years.

**User Analysis**: This section is divided into two categories:
a) District Analysis - Quarter-wise: Analyzes user data at the district level, categorized by quarters.
b) District Analysis - Year-wise: Analyzes user data at the district level, categorized by years.

**Brand Analysis**: This section is divided into two categories:
a) Year Analysis: Analyzes brand performance over different years.
b) Overall Brand Analysis: Provides an overview of the performance of various brands.

## Getting Started

To get started with this project, follow these steps:

Clone or download the repository from [repository link].
Install the required dependencies and libraries.
Extract the necessary dataframes from the PhonePe Pulse GitHub repository using the provided code.
Upload the extracted dataframes into SQL Workbench using SQLalchemy and pymysql.
Load the dataframes from the SQL tables back into pandas.
Run the Streamlit application to launch the dashboard and visualize the data and insights.

## Conclusion

The PhonePe Pulse Data Visualization project offers a comprehensive and interactive dashboard to explore and analyze the data from the PhonePe Pulse GitHub repository. By utilizing Streamlit and Plotly, the project provides valuable insights into transaction details, user analysis, and brand performance. The visualizations and analysis presented in the dashboard can be useful for decision-making and gaining insights into the performance of PhonePe in different regions and over different time periods.

For more details, please refer to the code and documentation provided in this repository.

*Note: The dataset used in this project is sourced from the PhonePe Pulse GitHub repository (https://github.com/PhonePe/pulse), and credit should be given to PhonePe for providing the data.



