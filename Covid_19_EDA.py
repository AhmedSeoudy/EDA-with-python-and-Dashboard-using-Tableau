#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[2]:


covid_df = pd.read_csv("/Users/ahmedseoudy/Desktop/covid_19_india.csv")


# In[3]:


covid_df.head(5)


# In[4]:


covid_df.info()


# In[5]:


covid_df.describe()


# In[6]:


vaccine_df = pd.read_csv("/Users/ahmedseoudy/Desktop/covid_vaccine_statewise.csv")


# In[7]:


vaccine_df.head(5)


# In[8]:


vaccine_df.info()


# In[9]:


vaccine_df.describe()


# In[10]:


covid_df.drop(["Sno","Time","ConfirmedIndianNational","ConfirmedForeignNational"],inplace = True, axis = 1)
covid_df.head()


# In[11]:


covid_df["Date"] = pd.to_datetime(covid_df["Date"],format = "%Y-%m-%d")


# # Active Cases

# In[12]:


covid_df["Active"] = covid_df["Confirmed"] - (covid_df["Cured"] + covid_df["Deaths"])
covid_df.tail(5)


# In[13]:


statewise = pd.pivot_table(covid_df , values = ["Cured","Deaths","Confirmed","Active"]
                           ,index = "State/UnionTerritory",aggfunc = sum)


# In[14]:


statewise["Recovery_rate"]= (statewise["Cured"] * 100 )/ statewise["Confirmed"]
statewise["Mortality_rate"] =  (statewise["Deaths"] * 100 )/ statewise["Confirmed"]
statewise.head(10)


# In[15]:


statewise = statewise.sort_values(by = "Confirmed",ascending = False)
statewise.style.background_gradient(cmap = "cubehelix")


# # Top 10 Active cases states

# In[16]:


top_active_cases = covid_df.groupby(covid_df["State/UnionTerritory"]).max()[["Active","Date"]].sort_values(by = "Active",ascending = False).reset_index() 


# In[17]:


fig = plt.figure(figsize = (16,9))
plt.title("Top 10 Citites with Active Cases",size=20)
ax = sns.barplot(data = top_active_cases.iloc[:10], y= "Active" , x = "State/UnionTerritory",linewidth = 2)


# Top 10 states with highest Death cases 

# In[18]:


top_death_states = covid_df.groupby(by = "State/UnionTerritory").sum()
top_death_states = top_death_states.sort_values("Deaths",ascending = False).reset_index()
top_death_states.head()


# In[19]:


fig = plt.figure(figsize = (16,9))
plt.title("Top 10 States with highest Deaths")
ax = sns.barplot(data = top_death_states[:10] , y= "Deaths",x= "State/UnionTerritory",linewidth = 2)


# Growth trend

# In[20]:


fig = plt.figure(figsize = (16,9))
plt.title("Top 5 affected states in india")
sns.lineplot(data=covid_df[covid_df["State/UnionTerritory"].isin(["Maharashtra","Karnataka","kerala","Tamil Nadu","Uttar Pradesh"])]
            ,y="Active",x="Date",hue = "State/UnionTerritory")


# In[21]:


vaccine_df.head()


# In[22]:


vaccine_df.isnull().sum()


# In[23]:


vaccine_df.drop(["Sputnik V (Doses Administered)","AEFI","18-44 Years (Doses Administered)","45-60 Years (Doses Administered)","60+ Years (Doses Administered)"],axis =1,inplace =True)


# In[24]:


vaccine_df.drop(["18-44 Years(Individuals Vaccinated)","45-60 Years(Individuals Vaccinated)","60+ Years(Individuals Vaccinated)"],axis =1 ,inplace =True)


# In[25]:


vaccine_df.rename({"Updated On":"Vaccine_Date"},inplace = True,axis='columns')


# #Male vs Female Vaccination

# In[26]:


male = vaccine_df["Male(Individuals Vaccinated)"].sum()
female = vaccine_df["Female(Individuals Vaccinated)"].sum()    
px.pie(names=["Male","Female"], values = [male,female],title="Male vs female Vaccination")


# In[27]:


vaccine = vaccine_df[vaccine_df.State != "India"]


# In[28]:


vaccine.rename({"Total Individuals Vaccinated":"Total"},inplace = True,axis = 'columns')


# In[29]:


vaccine.reset_index().head()


# #States with most vaccinated Individuals

# In[30]:


most_vaccinated = vaccine.groupby(by="State").sum().sort_values(by="Total",ascending=False).reset_index()


# In[31]:


least_vaccinated = vaccine.groupby(by="State").sum().sort_values(by="Total",ascending=True).reset_index()


# In[32]:


fig = plt.figure(figsize = (16,9))
plt.title("States with most vaccinated individuals")
ax = sns.barplot(data =most_vaccinated[:10], x= "State",y="Total")


# In[33]:


fig = plt.figure(figsize = (25,9))
plt.title("States with least vaccinated individuals")
ax = sns.barplot(data =least_vaccinated[:10], x= "State",y="Total")


# In[ ]:





# In[ ]:




