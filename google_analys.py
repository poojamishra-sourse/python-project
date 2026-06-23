import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from pytrends.request import TrendReq
#set up pytrend library and define keywords
pytrends=TrendReq(hl='en-us',tz=360)
keyword="cloud computing"
#data request
pytrends.build_payload([keyword],cat=0,timeframe='today 12-m',geo='',gprop='')
#counrty wise interest
region_data=pytrends.interest_by_region()
region_data=region_data.sort_values(by=keyword,ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=region_data[keyword],y=region_data.index,palette="Blues_d")
plt.title(f"Top 10 Countries interested in {keyword}")
plt.xlabel("Interest ")
plt.ylabel("Country")
plt.show()
#world map visualization
region_data=region_data.reset_index()
fig=px.choropleth(region_data, locations='geoName', locationmode='country names', color=keyword,  color_continuous_scale='Blues', title=f"search intrest for ' {keyword}'by country")
fig.show()
#time series analysis
time_df=pytrends.interest_over_time()
plt.figure(figsize=(12,6))
plt.plot(time_df.index,time_df[keyword],marker='o')
plt.title(f"search intrest for '{keyword}' over time",color='purple')
plt.xlabel("Date")
plt.ylabel("Interest")
plt.grid(True)
plt.show()
#multikeyword comparison
keywords=["cloud computing","artificial intelligence","data science"]
pytrends.build_payload(keywords,cat=0,timeframe='today 12-m',geo='',gprop='')
campare_df=pytrends.interest_over_time()
plt.figure(figsize=(12,6))
for kw in keywords:
    plt.plot(campare_df.index,campare_df[kw],marker='o',label=kw)
plt.title("keyword comparison",color='green')
plt.xlabel("Date")
plt.ylabel("Interest")  
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()    