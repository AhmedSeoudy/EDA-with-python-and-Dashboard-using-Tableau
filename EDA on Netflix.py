#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt


# In[2]:


netflix_df = pd.read_csv("/Users/ahmedseoudy/Desktop/netflix_titles.csv")


# In[3]:


netflix_df.info()


# In[4]:


netflix_df["director"] = netflix_df["director"].fillna("No Available Data")
netflix_df["cast"] = netflix_df["cast"].fillna("No Available Data")
netflix_df["date_added"] = netflix_df["date_added"].fillna(netflix_df["date_added"].mode())
netflix_df["country"] = netflix_df["country"].fillna(netflix_df["country"].mode())
netflix_df["rating"] = netflix_df["rating"].fillna(netflix_df["rating"].mode())
netflix_df.head(10)


# In[5]:


netflix_df.isnull().sum()


# In[6]:


netflix_df.duplicated().sum()


# In[7]:


netflix_df['year'] = pd.DatetimeIndex(netflix_df['date_added']).year
netflix_df['month'] = pd.DatetimeIndex(netflix_df['date_added']).month


# In[8]:


netflix_df.head()


# In[9]:


ratings_ages = {
    'TV-PG': 'Older Kids',
    'TV-MA': 'Adults',
    'TV-Y7-FV': 'Older Kids',
    'TV-Y7': 'Older Kids',
    'TV-14': 'Teens',
    'R': 'Adults',
    'TV-Y': 'Kids',
    'NR': 'Adults',
    'PG-13': 'Teens',
    'TV-G': 'Kids',
    'PG': 'Older Kids',
    'G': 'Kids',
    'UR': 'Adults',
    'NC-17': 'Adults'
}
netflix_df["ratings_ages"]=netflix_df["rating"].replace(ratings_ages)


# Content Distribution

# In[10]:


count_types = netflix_df["type"].value_counts().reset_index()
count_types


# In[11]:


px.pie(count_types,values = "type", names="index",title='Content Distribution')


# Countries with highest number of movies and TV shows

# In[12]:


countries_data = netflix_df.groupby(by = "country").count()["show_id"].sort_values(ascending=False).reset_index()


# In[13]:


countries_data = countries_data[:10]
fig = plt.figure(figsize=(12,6))
plt.title("Countries with highest number of movies and Tv shows")
ax = sns.barplot(x=countries_data["country"],y=countries_data["show_id"])
for i in ax.patches:
    ax.text(i.get_x()+.25,i.get_height()+2.3,str(int((i.get_height()))),
            rotation=0,fontsize=15,color='black')


# Top ten countries with highest number of movies

# In[14]:


movies_df = netflix_df[netflix_df["type"] == "Movie"]
movies_df = movies_df.groupby(by = "country")["show_id"].count().sort_values(ascending = False).reset_index()
movies_df


# In[15]:


movies_df = movies_df[:10]
fig = plt.figure(figsize=(12,6))
plt.title("Countries with highest number of movies ")
ax = sns.barplot(x=movies_df["country"],y=movies_df["show_id"])
for i in ax.patches:
    ax.text(i.get_x()+.25,i.get_height()+2.3,str(int((i.get_height()))),
            rotation=0,fontsize=15,color='black')


# In[16]:


shows_df = netflix_df[netflix_df["type"] == "TV Show"]
shows_df = shows_df.groupby(by = "country")["show_id"].count().sort_values(ascending = False).reset_index()
shows_df = shows_df[:10]
fig = plt.figure(figsize=(12,6))
plt.title("Countries with highest number of TV shows ")
ax = sns.barplot(x=shows_df["country"],y=shows_df["show_id"])
for i in ax.patches:
    ax.text(i.get_x()+.25,i.get_height()+2.3,str(int((i.get_height()))),
            rotation=0,fontsize=15,color='black')


# Content Added over the years

# In[17]:


year_data = netflix_df.groupby(by = "year")["show_id"].agg({'count':'count'}).sort_values(by = "year",ascending = True).reset_index()
year_data


# In[18]:


fig = plt.figure(figsize=(12,6))
plt.title("Content added over the years ")
ax = sns.barplot(x=year_data["year"],y=year_data["count"])
for i in ax.patches:
    ax.text(i.get_x()+.25,i.get_height()+2.3,str(int((i.get_height()))),
            rotation=0,fontsize=15,color='black')


# Genres

# In[19]:


px.pie(netflix_df,names="ratings_ages",values=netflix_df.index)


# In[20]:


type_year_mov = netflix_df[netflix_df["type"] == "Movie"]
type_year_mov = type_year_mov.groupby(by=["year"])["show_id"].agg({'count':'count'})
type_year_series = netflix_df[netflix_df["type"] == "TV Show"]
type_year_series = type_year_series.groupby(by=["year"])["show_id"].agg({'count':'count'})


# In[21]:


type_year_mov.columns = ['movie count']
type_year_series.columns = ['TV shows count']


# In[22]:


fig = plt.figure(figsize=(16,9))


# In[23]:


ax = type_year_mov.plot() 
type_year_series.plot(ax=ax, title='Types added over the years')


# In[ ]:




