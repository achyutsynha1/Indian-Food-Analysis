#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import codecs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler


# In[2]:


os.listdir()


# In[3]:


df=pd.read_csv("C:\\Users\\loket\\Downloads\\5-indian_food.csv")


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.shape


# In[7]:


df.info()


# In[8]:


df.dtypes


# In[9]:


df.isnull().sum()


# In[10]:


df.columns


# In[38]:


df.columns = df.columns.str.lstrip()


# In[12]:


df.columns


# In[13]:


df.describe()


# In[14]:


df.head()


# In[15]:


df.dropna(inplace = True)


# In[16]:


df.shape


# In[17]:


type('ingredients')


# In[18]:


df.dtypes


# In[39]:


df.flavor_profile.unique()


# In[40]:


df["flavor_profile"]= df["flavor_profile"].replace("-1","umami")


# In[21]:


df["cook_time"]= df["cook_time"].replace(-1,0)


# In[42]:


df["prep_time"]= df["prep_time"].replace(-1,0)


# In[22]:


df[['cook_time','name']].sort_values('cook_time')


# In[23]:


df["prep_time"]= df["prep_time"].replace(-1,0)


# In[24]:


df[['prep_time','name']].sort_values('prep_time')


# In[25]:


df.prep_time.mean()


# In[26]:


df.cook_time.mean()


# In[27]:


df.diet.value_counts()


# In[47]:


df["state"]= df["state"].replace("-1","others")


# In[46]:


df.state.value_counts()


# In[29]:


df.flavor_profile.value_counts()


# In[37]:


sns.displot(df["prep_time"], bins = 200)


# In[51]:


sns.displot(df["cook_time"], bins = 20)


# In[55]:


ax=sns.jointplot(x = 'prep_time', y ='cook_time', data = df, xlim = (0,200), ylim = (0,120))


# In[56]:


sns.countplot(x = 'flavor_profile', data = df)


# In[58]:


df["region"]= df["region"].replace("-1","others")


# In[59]:


sns.countplot(x = 'region', data = df)


# In[67]:


sns.boxplot(x = 'flavor_profile', y = 'prep_time', data = df)


# In[61]:


sns.stripplot(x = 'flavor_profile', y = 'prep_time', data = df)


# In[62]:


sns.countplot(x = 'course', data = df)


# In[64]:


sns.countplot(x = 'diet', data = df)


# In[68]:


sns.pairplot(df)


# In[69]:


mx=df.corr()


# In[73]:


plt.figure(figsize=(50,50))
sns.boxplot(x='prep_time',y='cook_time',data = df)


# In[75]:


df['total_time']=df['prep_time']+df['cook_time']
df.head()


# In[80]:


plt.figure(figsize=(10,10))
sns.boxplot(x='region',y='total_time',data=df) 


# In[81]:


df1=df.corr()
df1


# In[82]:


plt.figure(figsize=(7,7))
sns.heatmap(df1,annot=True,linecolor='White',linewidth=1)


# In[83]:


sns.relplot(x='total_time',y='course',hue='diet',kind='scatter',cmap='winter',data=df)


# In[84]:


sns.pairplot(df,vars=('prep_time','cook_time'),hue='total_time')


# In[87]:



sns.displot(df["total_time"], bins = 20)


# In[ ]:





# In[ ]:




