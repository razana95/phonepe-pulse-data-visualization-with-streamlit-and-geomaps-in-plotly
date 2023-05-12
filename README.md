# phonepe-pulse-data-visualization-with-streamlit-and-geomaps-in-plotly

I have created a dashboard to visualize Phonepe pulse Github repository data(https://github.com/PhonePe/pulse) using Streamlit and Plotly in Python



THE MAIN AIM OF THIS PROJECT:
To get realdata from phone pulse github page and processing the data to get valuable insights.

PROCESS INVOLVED :

*Extracting dataframe from the github data using pandas dataframe.
*Uploading those dataframes into sql workbench using sqlalchamey and pymysql.
*Loading pandas dataframe from the sql tables.
*Visualizing the data using geomaps functions in plotly.
* Creating a dashboard with streamlit to show visualizations.


THE MAIN COMPONENTS OF THE DASHBOARD:
1)GEO VISUALIZATION OF OVERALL TRANSACTION DETAILS FOR EACH DISTRICTS AND STATES.
2)TRANSACTION ANALYSIS.
3)USER ANALYSIS.
4)BRAND ANALYSIS.

1)GEO VISUALIZATION:
-created choropleth map of indian states that will show overall transaction details for each year.
-created scattergeo map of all districts in each states that shows all transaction details.
-Line map for overall growth of phonepe over the years.
-Hidden bar graph to show the top states having higher transactions.

2)TRANSACTION ANALYSIS:
-This sub divides into three categories:
a)STATE ANALYSIS
b) DISTRICT ANALYSIS
c) YEAR ANALYSIS
                   
3)USER ANALYSIS:
-This sub divides into two categories:
a)DISTRICT ANALYSIS-QUARTER WISE
b) DISTRICT ANALYSIS-YEAR WISE

4)BRAND ANALYSIS:
-This sub divides into two categories:
a)Year analysis
b)Overall brand analysis
