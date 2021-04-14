#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


# In[3]:


df = pd.read_csv("testing.csv")
df.columns


# In[6]:


df=df.drop(['Unnamed: 0','place', 'url'],axis = 1)


# In[11]:


df=df.dropna()


# In[19]:


df['num_pages']=pd.to_numeric(df['num_pages'],downcast='integer')


# In[21]:


df.head()


# # 1. Min-Max normalization

# In[23]:


#Step 1: find min(avg_rating)
minValue = df['avg_rating'].min()
print('Minimum rating: ', minValue)

#Step2: find max(avg_rating)
maxValue = df['avg_rating'].max()
print('Maximum rating: ', maxValue)


# In[24]:


#Step3 min max norm for average rating 
def minmax_norm(data_column_name):
    x = data_column_name
    mean_norm_ratings=1+((x-x.min())/(x.max()-x.min()))*9
    return mean_norm_ratings


# In[37]:


df['minmax_norm_ratings']=minmax_norm(df['avg_rating']).round(decimals=2)  # little problem


# In[38]:


df.head()


# # Mean normalization

# In[13]:


#Step1 : average (avg_rating)
df_mean = df[["avg_rating"]].mean()
df_mean


# In[39]:


def mean_norm(data_column_name):
    x = data_column_name
    mean_norm_ratings=1+((x-x.mean())/(x.max()-x.min()))*9
    return mean_norm_ratings


# In[41]:


#print(type(mean_norm(cleaned["avg_rating"])))
a = mean_norm(df["avg_rating"])
a.to_frame()


# Adding Minmax_norm and mean_norm to the csv

# In[43]:


df['mean_norm_ratings']=mean_norm(df['avg_rating']).round(decimals=2)


# In[102]:


df.head()


# In[50]:


cols = df.columns.tolist()
cols=cols[:8]+cols[-2:]+cols[8:-2]
df = df[cols]


# In[92]:


df


# In[72]:


# dt = df.loc[(df["num_pages"] != 0 )& (df['original_publish_year'] != 0 )]
# dt


# In[ ]:


df.to_csv('preprocess_data.csv')


# #                                                                            Analyse

# In[62]:


anay_goup = df.groupby("original_publish_year")['minmax_norm_ratings'].mean().round(decimals=2)


# In[63]:


anay_goup.to_frame()


# In[61]:


anay_goup.to_frame()


# #                                         The Best Book Author

# In[99]:


def  get_book_author(name,df):
    f=df[df.loc[:,'author'] == name]
    m=f['minmax_norm_ratings'].max()
    return m



# In[100]:


get_book_author('Cassandra Clare',df)


# <a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=8aa7b630-9ed2-4356-9070-0a10a3a5f060' target="_blank">
# <img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>
# Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>
