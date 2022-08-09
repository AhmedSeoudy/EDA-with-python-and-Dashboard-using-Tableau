#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from pandas.api.types import CategoricalDtype

get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns


# In[2]:


airbnb_nyc = pd.read_csv('/Users/ahmedseoudy/Desktop/AB_NYC_2019.csv')


# In[3]:


airbnb_nyc.head()


# In[4]:


airbnb_nyc.shape


# In[5]:


airbnb_nyc.info()


# In[6]:


# How many room types are available for rental?
airbnb_nyc.room_type.unique()


# In[7]:


# How many neighborhood groups are there?
airbnb_nyc.neighbourhood_group.unique()


# In[8]:


# How many neighborhoods are there?
airbnb_nyc.neighbourhood.nunique()


# In[9]:


# How many hosts are there?
airbnb_nyc.host_id.nunique()


# In[10]:


# How many listings are there?
airbnb_nyc.id.nunique()


# In[11]:


airbnb_nyc.isnull().sum()


# In[12]:


airbnb_nyc.drop(['name', 'host_name', 'last_review'], axis=1, inplace=True)


# In[13]:


# Checking the changes
airbnb_nyc.head()


# In[14]:


airbnb_nyc.fillna({'reviews_per_month': 0}, inplace=True)
airbnb_nyc.isnull().sum()


# In[15]:


airbnb_nyc.duplicated().sum()


# In[16]:


airbnb_nyc.rename(columns={'neighbourhood_group': 'borough', 'neighbourhood': 'neighborhood'}, inplace=True)


# In[17]:


airbnb_nyc.head()


# In[18]:


airbnb_nyc.describe()


# In[19]:


airbnb_nyc.agg(
    {'price': ['mean', 'median', 'min', 'max', 'count']})


# In[21]:


plt.figure(figsize=(10,5))
ax = sns.boxplot(y='price', data=airbnb_nyc).set_title('Price Distribution by Borough')
plt.xlabel('Borough')
plt.ylabel('Price')
plt.show()


# In[22]:


airbnb_pivot = pd.pivot_table(airbnb_nyc, index=['borough'], values='id', aggfunc=['count'], 
                              margins=True, margins_name='Total Count')
airbnb_pivot


# In[26]:


df2 = airbnb_nyc.groupby(['borough'])['id'].count()
df2.plot.pie( title='Total Listings by Borough', autopct='%1.0f%%', fontsize='11', colors=['#a6d854', '#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3'],startangle=0, figsize=(10,8))
plt.show()


# In[28]:


# creating palette
my_pal = {'Brooklyn': '#66c2a5', 'Manhattan': '#fc8d62', 'Queens': '#8da0cb', 'Staten Island': '#e78ac3', 'Bronx': '#a6d854'}
df = airbnb_nyc[['borough', 'price']]
df = airbnb_nyc.groupby(['borough'], as_index=False)[['price']].mean()

plt.figure(figsize=(12, 6))
df = sns.barplot(x="borough", y="price", data=df, palette=my_pal)
for p in df.patches:
    df.annotate(format(p.get_height(), '.2f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', size = 12, 
                   xytext = (0, -12), textcoords = 'offset points')
    
plt.xlabel('Borough')
plt.ylabel('Average Price')
plt.title('Average Price by Borough')
plt.show()


# In[30]:


my_pal2 = {'Entire home/apt': '#377eb8', 'Private room': '#ff7f00', 'Shared room': '#4daf4a'}
df = airbnb_nyc[['borough', 'room_type', 'price']]
df = df.groupby(['borough', 'room_type'], as_index=False)[['price']].mean()

plt.figure(figsize=(12, 6))
df = sns.barplot(x="borough", y="price", data=df, hue='room_type', palette=my_pal2)
for p in df.patches:
    df.annotate(format(p.get_height(), '.2f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', size = 11, 
                   xytext = (0, -12), textcoords = 'offset points')
    
plt.xlabel('Borough')
plt.ylabel('Average Price')
plt.title('Average Price by Room Type')
plt.show()


# In[31]:


import warnings
warnings.filterwarnings('ignore')
plt.figure(figsize=(12,6))
sns.scatterplot(airbnb_nyc.longitude, airbnb_nyc.latitude, 
                hue=airbnb_nyc.room_type, palette=my_pal2).set_title('Visualizing Listings by Room Type')
plt.ioff()


# In[33]:


airbnb_nyc.groupby(['borough'])['availability_365'].mean()
plt.figure(figsize=(10,5))
ax = sns.boxplot(data=airbnb_nyc, x='borough', y='availability_365', palette=my_pal).set_title('Room Availability by Borough')
plt.xlabel('Borough')
plt.ylabel('Availability per Year')
plt.show()


# In[34]:


plt.figure(figsize=(12,6))
sns.scatterplot(airbnb_nyc.longitude, airbnb_nyc.latitude, 
                hue=airbnb_nyc.availability_365).set_title('Visualizing Availability by Borough')
plt.ioff()


# In[35]:


df = airbnb_nyc.groupby(['neighborhood'])['id'].count().nlargest(10)


# In[36]:


plt.figure(figsize=(12,6))
x = list(df.index)
y = list(df.values)
x.reverse()
y.reverse()

plt.title("Top 10 Neighborhoods with the Most Listings")
plt.ylabel("Neighborhood")
plt.xlabel("Total Listings")

plt.barh(x, y)
plt.show()


# In[37]:


plt.figure(figsize=(12, 6))
ax = sns.barplot(x="borough", y="minimum_nights", data=airbnb_nyc, palette=my_pal, ci=None)
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', size = 11, 
                   xytext = (0, -12), textcoords = 'offset points')
plt.xlabel('Borough')
plt.ylabel('Average Minimum Nights')
plt.title('Average Minimum Nights by Borough')
plt.show()


# In[ ]:




