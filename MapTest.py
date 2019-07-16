
# coding: utf-8

# In[87]:


import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import lxml
from geopy.geocoders import Nominatim
from IPython.display import Image 
from IPython.core.display import HTML
from pandas.io.json import json_normalize
import folium


# In[88]:


result = requests.get("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")


# In[89]:


soup = BeautifulSoup(result.content, 'html5lib')


# In[90]:


table = soup.find_all('table')[0] 
table
dfs = pd.read_html(str(table))
df = pd.concat(dfs)
df.columns = ['Postalcode', 'Borough','Neighbourhood']
df = df.iloc[1:]
df=df[df['Neighbourhood']!='Not assigned']
df.head()
dfgrp=df.groupby(['Postalcode','Borough'])['Neighbourhood'].apply(''.join).reset_index()
dfgrp.head(11)


# In[91]:


dfspatial=pd.read_csv("C:\Geospatial_Coordinates.csv")


# In[92]:


dfoutput=dfgrp.merge(dfspatial,on='Postalcode',how='inner')


# In[93]:


dfoutput.head(11)


# In[94]:


dfToronto=dfoutput[dfoutput['Borough'].str.contains("Toronto")]


# In[95]:


dfToronto.head()


# In[96]:


dfToronto.Longitude.dtype


# In[97]:


venues_map = folium.Map(location=[43.676357, -79.293031], zoom_start=10)


# In[98]:


from folium import plugins
from folium.plugins import MarkerCluster
from IPython.display import display
marker_cluster = MarkerCluster().add_to(venues_map)





# In[99]:


for index, row in dfToronto.iterrows():    
    folium.Marker(
    [row['Latitude'], row['Longitude']],
    radius=10,
    color='red',
    popup="M4N",
    fill = True,
    fill_color = 'blue',
    fill_opacity = 0.6).add_to(marker_cluster)
    venues_map.save('venues.html')


# In[100]:


venues_map

