
# coding: utf-8

# In[27]:


import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import lxml


# In[28]:


result = requests.get("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")


# In[29]:


result


# In[30]:


soup = BeautifulSoup(result.content, 'html5lib')


# In[38]:


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


# In[39]:


df.shape

