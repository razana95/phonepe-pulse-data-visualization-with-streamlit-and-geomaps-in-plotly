import pandas as pd
import os
import json
import streamlit as st
import warnings
import pymysql
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import plotly.express as px
import plotly.io as pio
warnings.filterwarnings("ignore")
st.set_page_config(layout="wide")
#pio.renderers.default = 'browser'

#DICTIONARY CREATED TO MAP STATE NAMES IN MY DATA AND IN THE GEOJSON DATA
state_dict = {
    'andaman-&-nicobar-islands': 'Andaman and Nicobar',
    'tamil-nadu': 'Tamil Nadu',
    'lakshadweep': 'Lakshadweep',
    'telangana': 'Andhra Pradesh',
    'manipur': 'Manipur',
    'haryana': 'Haryana',
    'gujarat': 'Gujarat',
    'sikkim': 'Sikkim',
    'delhi': 'Delhi',
    'west-bengal': 'West Bengal',
    'uttar-pradesh': 'Uttar Pradesh',
    'goa': 'Goa',
    'punjab': 'Punjab',
    'arunachal-pradesh': 'Arunachal Pradesh',
    'karnataka': 'Karnataka',
    'jammu-&-kashmir': 'Jammu and Kashmir',
    'maharashtra': 'Maharashtra',
    'odisha': 'Orissa',
    'madhya-pradesh': 'Madhya Pradesh',
    'rajasthan': 'Rajasthan',
    'andhra-pradesh': 'Andhra Pradesh',
    'chandigarh': 'Chandigarh',
    'kerala': 'Kerala',
    'chhattisgarh': 'Chhattisgarh',
    'tripura': 'Tripura',
    'mizoram': 'Mizoram',
    'himachal-pradesh': 'Himachal Pradesh',
    "dadra-&-nagar-haveli-&-daman-&-diu": "Dadra and Nagar Haveli",
    'ladakh': 'Jammu and Kashmir',
    'assam': 'Assam',
    'meghalaya': 'Meghalaya',
    'uttarakhand': 'Uttaranchal',
    'puducherry': 'Puducherry',
    'bihar': 'Bihar',
    'jharkhand': 'Jharkhand',
    'nagaland': 'Nagaland'
}

##CREATING DATAFRAME FROM FOLDER AGGREGATION->TRANSACTION
path="/Users/fasilck/Downloads/clone/pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list=os.listdir(path)
col1={'State':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Total_Transaction':[], 'Transaction_amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              col1['Transaction_type'].append(Name)
              col1['Total_Transaction'].append(count)
              col1['Transaction_amount'].append(amount)
              col1['State'].append(i)
              col1['Year'].append(j)
              col1['Quater'].append(int(k.strip('.json')))
Agg_Trans=pd.DataFrame(col1)
Agg_Trans["state_name"]=Agg_Trans["State"].map(state_dict)
Agg_Trans=Agg_Trans.drop("State",axis=1)

####CREATING DATAFRAME FROM FOLDER AGGREGATION->MAP
path="/Users/fasilck/Downloads/clone/pulse/data/aggregated/user/country/india/state/"
Agg_user_list=os.listdir(path)
clm={'State':[], 'Year':[],'Quater':[],'brand':[], 'user_count':[], 'percentage_share':[]}
for i in Agg_user_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            try:
               for z in D['data']['usersByDevice']:
                  Name=z['brand']
                  count=z['count']
                  amount=z['percentage']
                  clm['brand'].append(Name)
                  clm['user_count'].append(count)
                  clm['percentage_share'].append(amount)
                  clm['State'].append(i)
                  clm['Year'].append(j)
                  clm["Quater"].append(int(k.strip(".json")))
            except:
              pass

####CREATING ANOTHER DATAFRAME FROM FOLDER AGGREGATION->USERS       
Agg_users=pd.DataFrame(clm)
Agg_users["state_name"]=Agg_users["State"].map(state_dict)
Agg_users=Agg_users.drop("State",axis=1)

path="/Users/fasilck/Downloads/clone/pulse/data/aggregated/user/country/india/state/"
Agg_user_list=os.listdir(path)
clm={'State':[], 'Year':[],'Quater':[],'registeredUsers':[], 'appOpenings':[]}
for i in Agg_user_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            try:
               z= D['data']['aggregated']["registeredUsers"]
               y=D['data']['aggregated']["appOpens"]
                  #name=z
                  #count=['appOpens']
                  #amount=z['percentage']
               clm['registeredUsers'].append(z)
               clm['appOpenings'].append(y)
               clm['State'].append(i)
               clm['Year'].append(j)
               clm["Quater"].append(int(k.strip(".json")))
            except:
              pass
Agg_users_reg=pd.DataFrame(clm)
Agg_users_reg["state_name"]=Agg_users_reg["State"].map(state_dict)
Agg_users_reg=Agg_users_reg.drop("State",axis=1)
#Agg_users_reg


####CREATING DATAFRAME FROM FOLDER MAP->TRANSACTION
path="/Users/fasilck/Downloads/clone/pulse/data/map/transaction/hover/country/india/state/"
map_trans=os.listdir(path)

clm={'state':[],'year':[],'quarter':[],'district_name':[],'transaction_count':[],'transacted_amount':[]}
for i in map_trans:
  p_i=path+i+"/"
  map_state=os.listdir(p_i)
  for j in map_state:
    p_j=p_i+j+"/"
    map_year=os.listdir(p_j)
    for k in map_year:
      p_k=p_j+k
      if k.endswith(".json"):
        Data=open(p_k,"r")
        D=json.load(Data)
        for z in D['data']['hoverDataList']:
          name=z["name"]
          count=z["metric"][0]["count"]
          amount=z["metric"][0]["amount"]
          clm['district_name'].append(name)
          clm['transaction_count'].append(count)
          clm['transacted_amount'].append(amount)
          clm['state'].append(i)
          clm['year'].append(j)
          clm['quarter'].append(int(k.strip('.json')))

map_trans=pd.DataFrame(clm)
map_trans["state_name"]=map_trans["state"].map(state_dict)
map_trans=map_trans.drop("state",axis=1)



####CREATING DATAFRAME FROM FOLDER MAP->USERS
path="/Users/fasilck/Downloads/clone/pulse/data/map/user/hover/country/india/state/"
map_user=os.listdir(path)

clm={'state':[],'year':[],'quarter':[],'district_name':[],'registeredUsers':[],'appOpening':[]}
for i in map_user:
  p_i=path+i+"/"
  map_state=os.listdir(p_i)
  for j in map_state:
    p_j=p_i+j+"/"
    map_year=os.listdir(p_j)
    for k in map_year:
      p_k=p_j+k
      if k.endswith(".json"):
        Data=open(p_k,"r")
        D=json.load(Data)
        for z in D['data']["hoverData"].items():
          name=z[0]
          count=z[1]["registeredUsers"]       
          amount=z[1]["appOpens"]
          clm['district_name'].append(name)
          clm['registeredUsers'].append(count)
          clm['appOpening'].append(amount)
          clm['state'].append(i)
          clm['year'].append(j)
          clm['quarter'].append(int(k.strip('.json')))
#Succesfully created a dataframe
map_users=pd.DataFrame(clm)
map_users["state_name"]=map_users["state"].map(state_dict)
map_users=map_users.drop("state",axis=1)
#map_users

#CREATING DATAFRAME FROM TOP->TRANSACTION
path="/Users/fasilck/Downloads/pulse-master/data/top/transaction/country/india/state/"
top_trans=os.listdir(path)
#top_user
clm={'state':[],'year':[],'quarter':[],'district_name':[],'count':[],'amount':[]}
for i in top_trans:
  p_i=path+i+"/"
  top_state=os.listdir(p_i)
  for j in top_state:
    p_j=p_i+j+"/"
    top_year=os.listdir(p_j)
    for k in top_year:
      p_k=p_j+k
      if k.endswith(".json"):
        Data=open(p_k,"r")
        D=json.load(Data)
        for z in D['data']["districts"]:
          name=z["entityName"]
          count=z["metric"]["count"]       
          amount=z["metric"]["amount"]
          clm['district_name'].append(name)
          clm['count'].append(count)
          clm['amount'].append(amount)
          clm['state'].append(i)
          clm['year'].append(j)
          clm['quarter'].append(int(k.strip('.json')))
#Succesfully created a dataframe
top_transac=pd.DataFrame(clm)


##CREATING DATAFRAME FROM TOP->USERS
path="/Users/fasilck/Downloads/pulse-master/data/top/user/country/india/state/"
top_users=os.listdir(path)
#top_users
clm={'state':[],'year':[],'quarter':[],'district_name':[],'registered_users':[],'pincode':[],"pin_reg_user":[]}
for i in top_users:
  p_i=path+i+"/"
  top_state=os.listdir(p_i)
  for j in top_state:
    p_j=p_i+j+"/"
    top_year=os.listdir(p_j)
    for k in top_year:
      p_k=p_j+k
      if k.endswith(".json"):
        Data=open(p_k,"r")
        D=json.load(Data)
        for z in D['data']["districts"]:
          name=z["name"]
          count=z["registeredUsers"]
          for y in D["data"]["pincodes"]:       
            amount=y["name"]
            count1=y["registeredUsers"]
            clm['district_name'].append(name)
            clm['registered_users'].append(count)
            clm['pincode'].append(amount)
            #clm["registered_users"].append(count1)
            clm["pin_reg_user"].append(count1)
            clm['state'].append(i)
            clm['year'].append(j)
            clm['quarter'].append(int(k.strip('.json')))
#Succesfully created a dataframe
top_users=pd.DataFrame(clm)



##NEW MERGED DATAFRAME FOR MY PLOTS
u=Agg_Trans["state_name"].drop_duplicates().sort_values()
k=pd.DataFrame(u)
a=Agg_Trans.groupby("state_name",sort=True).sum()
merged=pd.merge(k,a,on="state_name")
total=pd.merge(Agg_users_reg,merged,on="state_name").drop("Quater_y",axis=1)

##################################UPLOADING MY DATAFRAMES INTO SQL DATABASE [COMMENTED IT OUT SO THAT I CAN RUN MY PROGRAM QUICKLY]#######################
         
#from sqlalchemy import create_engine
#import mysql.connector as sq
#import pymysql
#engine=create_engine("mysql+pymysql://root:ayzu2020@127.0.0.1:3306/my_phonepe")
#conn=engine.connect()

#Agg_Trans.to_sql(name="aggregated_transaction",con=conn,if_exists="replace",index=False)
#Agg_users.to_sql(name="aggregated_user",con=conn,if_exists="replace",index=False)
#Agg_users_reg.to_sql(name="aggregated_user_reg",con=conn,if_exists="replace",index=False)
#map_trans.to_sql(name="map_transaction",con=conn,if_exists="replace",index=False)
#map_users.to_sql(name="map_user",con=conn,if_exists="replace",index=False)
#top_transac.to_sql(name="top_transaction",con=conn,if_exists="replace",index=False)
#top_users.to_sql(name="top_user",con=conn,if_exists="replace",index=False)


#mydb=pymysql.connect(host="localhost",user="root",passwd="ayzu2020",database="my_phonepe")
#mycursor=mydb.cursor()


##LOADING MYSQL TABLES IN PANDAS DSATAFRAME
#df_agg_trans=pd.read_sql_table("aggregated_transaction",conn)
#df_agg_user=pd.read_sql_table("aggregated_user",conn)
#df_agg_reg=pd.read_sql_table("aggregated_user_reg",conn)
#df_map_trans=pd.read_sql_table("map_transaction",conn)
#df_map_users=pd.read_sql_table("map_user",conn)


india=json.load(open("/Users/fasilck/Downloads/india_state_geo.json","r"))##GEOJSON FILE FOR STATES


import streamlit as st
#set.set_page_config(layout="wide")
st.title(":green[PHONE_PE DATA ANALYSIS]")
col1,col2=st.columns(2)
with col1:
    st.write(":blue[overall transaction]")
    year=st.selectbox("Please select the year",('2018','2019','2020','2021','2022'),key="k1")
    
#year=int(year)
#df_agg_trans_sum=df_agg_trans[df_agg_trans["Year"]==year]
u=Agg_Trans["state_name"].drop_duplicates().sort_values()
k=pd.DataFrame(u)
a=Agg_Trans.groupby("state_name",sort=True).sum()
merged=pd.merge(k,a,on="state_name")
total=pd.merge(Agg_users_reg,merged,on="state_name").drop("Quater_y",axis=1)
         #total.groupby("state_name")
total_df=total[(total["Year"]==year)]
#total_df



fig = px.choropleth(
    total_df,
    geojson=india,
    featureidkey='properties.NAME_1',
    locations='state_name',
    color='Total_Transaction',
    color_continuous_scale='Viridis',
    #hover_name='state_name',py
    hover_data=["Total_Transaction","Transaction_amount","registeredUsers","appOpenings"],
    title="Aggregated Transaction",
    )

fig.update_geos(fitbounds="locations", visible=False)

#fig.show()
with col2:
    st.write(":blue[map showing all district values in each state]")
    df=pd.read_csv("/Users/fasilck/district.csv")#geojson for districts
    df.rename(columns={"District":"district_name"},inplace=True)
    dist_lat_lon=pd.merge(df,map_trans,on="district_name")

fig_scatt = px.scatter_geo(
    dist_lat_lon,
    lon=dist_lat_lon['Longitude'],
    lat=dist_lat_lon['Latitude'],
    color=dist_lat_lon['transacted_amount'],
    size=dist_lat_lon['transaction_count'],
    hover_name="district_name",
    hover_data=["state_name", 'transacted_amount',
                'transaction_count', 'year', 'quarter'],
    title='District',
    scope="asia",
    #projection="stereographic",
    size_max=22,
)


with col1:
    st.plotly_chart(fig,user_container_width=True)
    
with col2:
    st.plotly_chart(fig_scatt,user_container_width=True)
    st.write("Details of map:  the size of the circle represents total transaction district_wise. Higher the circle higher is the transaction")
              
    

st.write(":blue[line chart to show overall growth of phonepe in last 5 years]")
    
#agg_trans_line=Agg_Trans.groupby("Year").sum()
s=Agg_Trans.groupby("Year").sum()
w=Agg_Trans["Year"].drop_duplicates().sort_values()
year_only=pd.DataFrame(w)
combine=pd.merge(year_only,s,on="Year")

fig1 = px.line(
    combine,
    x="Year",
    y="Total_Transaction"
)

fig1.update_layout(
    title='Total Transactions by Year',
    xaxis_title='Year',
    yaxis_title='Total Transactions'
)

fig1.update_traces(
    line=dict(color='blue', width=2),
    mode='lines+markers',
    marker=dict(size=5, color='red', symbol='circle'),
    fill='tozeroy',
    fillcolor='rgba(0,176,246,0.2)'
)
st.plotly_chart(fig1,use_container_width=True)
    
    ################################ HIDDEN BAR GRAPH #########################################
    

merged_by_tcount=merged.sort_values(by=["Total_Transaction"])
#fig_bar=px.bar(merged_by_tcount,x="state_name",y="Total_Transaction")
fig_bar = px.bar(merged_by_tcount, x="state_name", y="Total_Transaction", 
                color="state_name", color_discrete_sequence=px.colors.qualitative.Pastel,
                title="Total Transactions by State")
fig_bar.update_layout(xaxis_title="State", yaxis_title="Total Transactions", 
                     font=dict(family="Arial", size=14))
with st.expander("see bar graph for the same data"):
    st.plotly_chart(fig_bar,use_container_width=True)
    st.info(":blue[the above bar graph shows the transaction done in each states in increasing order. Here you can observe the top states having higher transaction]")
    
    
    
################################### TRANSACTION ANALYSIS #############################################
st.write(":green[TRANSACTION ANALYSIS]")
tab1,tab2,tab3=st.tabs(["STATE ANALYSIS","DISTRICT ANALYSIS","YEAR ANALYSIS"])
with tab1:
         Agg_Trans=Agg_Trans.copy()
         
         c1,c2=st.columns(2)
         with c1:
            year=st.selectbox("select year",("2018","2019","2020","2021","2022"),key="k2")
         with c2:
            quart=st.selectbox("select quarter",("1","2","3","4"),key="q1")
         #year=int(year)
         total_df_qrtr=total[(total["Year"]==year)& (total["Quater_x"]== int(quart) )]

         # total_df
         fig_choro=px.choropleth(total_df_qrtr,
            locations="state_name",
            geojson=india,
            featureidkey="properties.NAME_1",
            color="Transaction_amount",
            hover_data=["registeredUsers","Total_Transaction","appOpenings"],
            hover_name="state_name",
            )
         
         
#fig2.update_traces(marker=dict(color="#D5FFCC", size=0.3))
         fig.update_geos(fitbounds="locations", visible=False)
         col1,col2=st.columns([7,3])
         with col1:
             st.plotly_chart(fig_choro,use_container_width=True)
         with col2:
             st.info("""Details of the Map:
             Here details are segmented into four quarters of the year. 
             User can observe all transaction details and user details for all the states in each quarter""")
                        
  
with tab2:
         #st.write(:)
         c1,c2,c3=st.columns(3)
         with c1:
            s1=st.selectbox("select state",('Andaman and Nicobar', 'Tamil Nadu', 'Lakshadweep',
                                           'Andhra Pradesh', 'Manipur', 'Haryana', 'Gujarat', 'Sikkim',
                                           'Delhi', 'West Bengal', 'Uttar Pradesh', 'Goa', 'Punjab',
                                           'Arunachal Pradesh', 'Karnataka', 'Jammu and Kashmir',
                                           'Maharashtra', 'Orissa', 'Madhya Pradesh', 'Rajasthan',
                                           'Chandigarh', 'Kerala', 'Chhattisgarh', 'Tripura', 'Mizoram',
                                           'Himachal Pradesh', 'Dadra and Nagar Haveli', 'Assam', 'Meghalaya',
                                           'Uttaranchal', 'Puducherry', 'Bihar', 'Jharkhand', 'Nagaland'),key="s00")
         
         with c2:
            y1=st.selectbox("select year",("2018","2019","2020","2021","2022"),key="s01")
         with c3:
            q=int(st.selectbox("select quarter",("1","2","3","4"),key="s02"))
         #k=int(q)
         
         map_tran=map_trans.copy()
         map_trans_c = map_tran[(map_tran["year"]==y1) & (map_tran["quarter"]==q)& (map_tran["state_name"]==s1)]
         
         fig2 = go.Figure(data=[
            go.Bar(x=map_trans_c["district_name"], y=np.log10(map_trans_c["transaction_count"]), name="transaction_count", marker={"color":"pink"},
                   hovertemplate="Transaction Count: %{y:.0f}<br>Actual Transaction Count: %{customdata:.0f}<extra></extra>",
                   customdata=map_trans_c["transaction_count"]),
            go.Bar(x=map_trans_c["district_name"], y=np.log10(map_trans_c["transacted_amount"]), name="transacted_amount", marker={"color":"orange"},
                   hovertemplate="Transacted Amount: ₹%{y:.2f}K<br>Actual Transacted Amount: ₹%{customdata:.2f}K<extra></extra>",
                   customdata=map_trans_c["transacted_amount"]/1000)      
        ])
         
         fig2.update_layout(barmode="group")
         fig2.update_yaxes(type="log")
         
         st.plotly_chart(fig2,use_container_width=True) 
         st.info("""Observation:
                    User can observe transaction details for each districts in all the states""")

         
with tab3:
         
        c1,c2=st.columns([6,4])
        with c1:
           co1,co2=st.columns(2)
           with co1:
              year2=st.selectbox("select year",("2018","2019","2020","2021","2022"),key="k4")
           with co2:
              mode=st.selectbox("select payment mode",('Peer-to-peer payments', 'Merchant payments',
                         'Recharge & bill payments', 'Financial Services', 'Others'),key="m1")
         
        df_user=Agg_Trans[(Agg_Trans["Transaction_type"]==mode) & (Agg_Trans["Year"]== year2)]
        #fig3=px.choropleth(df_user,
         #              locations="state_name",
          #            geojson=india,
           #           featureidkey="properties.NAME_1",
            #          color="Transaction_amount",
             #         hover_data=["Total_Transaction","Transaction_amount"]
              #        )
        fig3 = px.choropleth(df_user,
                     locations="state_name",
                     geojson=india,
                     featureidkey="properties.NAME_1",
                     color="Transaction_amount",
                     hover_data=["Total_Transaction","Transaction_amount"],
                     #projection="mercator",  # Use Mercator projection for better display
                     scope="asia",
                     color_continuous_scale=px.colors.sequential.Plasma,  # Use a custom color scale
                     range_color=(0, df_user["Transaction_amount"].max()),  # Set color scale range based on data
                     labels={"Transaction_amount": "Transaction Amount (INR)", "state_name": "State"},  # Set axis labels
                     title="Total Transaction Amount by State",  # Set chart title
                     )
        fig3.update_layout(geo=dict(bgcolor="#F0F0F0",  # Set background color
                             lakecolor="#FFFFFF",  # Set lake color
                             showcoastlines=True,  # Show coastlines
                             coastlinecolor="#FFFFFF",  # Set coastline color
                             projection=dict(scale=1.2)),  # Set map scale
                   margin=dict(l=0, r=0, t=50, b=0),  # Set margin for better display
                   coloraxis_colorbar=dict(title="Transaction Amount (INR)"),  # Set colorbar title
                   )       
        fig.update_geos(fitbounds="locations", visible=False)   

        with c1:
             st.plotly_chart(fig3,use_container_width=True)
        
             st.info("""Observation:
                        User can observe transaction details for all modes of payment""")

        with c2:
             table=Agg_Trans.groupby('Transaction_type').sum().drop("Quater",axis=1)
             st.table(table) 
             st.info("""The above table shows the overall details for each payment mode""")
 
    
         ###################### user analysis ###################################################
st.write(":green[USER ANALYSIS]")
tab1,tab2=st.tabs(["DISTRICT ANALYSIS-QUARTER WISE","DISTRICT ANALYSIS-YEAR WISE "])
with tab1:
        c1,c2,c3=st.columns(3)
        with c1:
            stt=st.selectbox("select state",('Andaman and Nicobar', 'Tamil Nadu', 'Lakshadweep',
                                 'Andhra Pradesh', 'Manipur', 'Haryana', 'Gujarat', 'Sikkim',
                               'Delhi', 'West Bengal', 'Uttar Pradesh', 'Goa', 'Punjab',
                                'Arunachal Pradesh', 'Karnataka', 'Jammu and Kashmir',
                                  'Maharashtra', 'Orissa', 'Madhya Pradesh', 'Rajasthan',
                                   'Chandigarh', 'Kerala', 'Chhattisgarh', 'Tripura', 'Mizoram',
                               'Himachal Pradesh', 'Dadra and Nagar Haveli', 'Assam', 'Meghalaya',
                             'Uttaranchal', 'Puducherry', 'Bihar', 'Jharkhand', 'Nagaland'),key="s2")
         
        with c2:
            #y=st.selectbox("select year",("2018","2019","2020","2021","2022"))
            y3=st.selectbox("select year",("2018","2019","2020","2021","2022"),key="k5")
        with c3:
            q3=st.selectbox("select quarter",("1","2","3","4"),key="q4")
         
        d=map_users[(map_users["state_name"]==stt)&(map_users["year"]==y3)&(map_users["quarter"]==int(q3))]


        fig5=go.Figure(data=[
            go.Bar(x=d["district_name"],y=d["appOpening"],name="appOpenings",marker={"color":"pink"}),
            go.Bar(x=d["district_name"],y=d["registeredUsers"],name="registeredUsers",marker={"color":"orange"})      
             ])
         
        fig5.update_layout(bar_mode="group")
        #fig5.update_traces(hovertemplate='<b>%{x}</b><br>%{y:.2e}')

        st.plotly_chart(fig5,use_container_width=True)
        st.info("""Observation:
                   User can observe how many users registered and how many apps opened in all the districts in each quarter""") 
with tab2:
    c1,c2=st.columns(2)
    with c1:
        st2=st.selectbox("select state",('Andaman and Nicobar', 'Tamil Nadu', 'Lakshadweep',
                                         'Andhra Pradesh', 'Manipur', 'Haryana', 'Gujarat', 'Sikkim',
                                          'Delhi', 'West Bengal', 'Uttar Pradesh', 'Goa', 'Punjab',
                                            'Arunachal Pradesh', 'Karnataka', 'Jammu and Kashmir',
                                          'Maharashtra', 'Orissa', 'Madhya Pradesh', 'Rajasthan',
                                        'Chandigarh', 'Kerala', 'Chhattisgarh', 'Tripura', 'Mizoram',
                                         'Himachal Pradesh', 'Dadra and Nagar Haveli', 'Assam', 'Meghalaya',
                                           'Uttaranchal', 'Puducherry', 'Bihar', 'Jharkhand', 'Nagaland'),key="s3")
         
    with c2:
            y4=st.selectbox("select year",("2018","2019","2020","2021","2022"),key="k6")
    da=map_users[(map_users["state_name"]==st2)&(map_users["year"]==y4)]


    fig6=go.Figure(data=[
            go.Bar(x=da["district_name"],y=da["appOpening"],name="appOpenings",marker={"color":"pink"}),
            go.Bar(x=da["district_name"],y=da["registeredUsers"],name="registered _users",marker={"color":"orange"})      
             ])
         
    fig.update_layout(barmode="group")
         
    st.plotly_chart(fig6,use_container_width=True)
    st.info("""Observation:
               This plot shows user details in all the district in each year""")
        
        
        ############################# BRAND ANALYSIS ######################################
st.write(":green[BRAND ANALYSIS]")
tab1,tab2=st.tabs(["YEAR WISE ANALYSIS","OVERALL BRAND ANALYSIS"])
with tab1:
    c1,c2=st.columns(2)
    with c1:
        brnd=st.selectbox("select brand",('Vivo', 'Xiaomi', 'Samsung', 'Realme', 'Oppo', 'OnePlus', 'Tecno',
       'Apple', 'Huawei', 'Motorola', 'Others', 'Lenovo', 'Gionee',
       'COOLPAD', 'HMD Global', 'Lyf', 'Micromax', 'Asus', 'Infinix',
       'Lava'))
         
    with c2:
        y5=st.selectbox("select year",("2018","2019","2020","2021","2022"),key="k7")

    brand_user=Agg_users[(Agg_users["brand"]==brnd)&(Agg_users["Year"]==y5)]
    
    fig7=px.choropleth_mapbox(
    brand_user,
    geojson=india,
    locations="state_name",
    color="percentage_share",
    featureidkey="properties.NAME_1",
    mapbox_style="carto-positron",
    center={"lat": 24, "lon": 78},
    zoom=3,
    opacity=0.5,
    hover_data=["percentage_share", "user_count"],
)

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
             
    #fig.update_geos(fitbounds="locations", visible=False)   
    st.plotly_chart(fig7,use_container_width=True)

    st.info("""Observation:
               The above map shows the contribution of all mobile brands in all the states""")

with tab2:
    #fig8=px.line(Agg_users,x="brand",y="percentage_share",title="percentage share of all mobile brands")
    #st.plotly_chart(fig8,use_container_width=False)

    fig8 = px.pie(Agg_users, values="percentage_share", names="brand", title="Percentage Share of All Mobile Brands")
    fig8.update_traces(textposition='inside', textinfo='percent+label')
    fig8.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)',
    'font_color': '#333',
    'hoverlabel': {
        'font': {'color': '#fff'},
        'bgcolor': 'royalblue'
        }
    })
    st.plotly_chart(fig8, use_container_width=True)
    st.info(""" Observation:
            User can observe percentage share of each brand for phonepe transaction""")
