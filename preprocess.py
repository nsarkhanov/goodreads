
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("testing.csv")
df.columns
df = df.drop(['Unnamed: 0', 'place', 'url'], axis=1)
df = df.dropna()
df['num_pages'] = pd.to_numeric(df['num_pages'], downcast='integer')
df.head()

# Step 1: find min(avg_rating)
minValue = df['avg_rating'].min()
print('Minimum rating: ', minValue)

# Step2: find max(avg_rating)
maxValue = df['avg_rating'].max()
print('Maximum rating: ', maxValue)

# Step3 min max norm for average rating


def minmax_norm(data_column_name):
    x = data_column_name
    mean_norm_ratings = 1+((x-x.min())/(x.max()-x.min()))*9
    return mean_norm_ratings


df['minmax_norm_ratings'] = minmax_norm(
    df['avg_rating']).round(decimals=2)  # little problem

df.head()

# # Mean normalization
#Step1 : average (avg_rating)
df_mean = df[["avg_rating"]].mean()
df_mean


def mean_norm(data_column_name):
    x = data_column_name
    mean_norm_ratings = 1+((x-x.mean())/(x.max()-x.min()))*9
    return mean_norm_ratings


a = mean_norm(df["avg_rating"])
a.to_frame()

df['mean_norm_ratings'] = mean_norm(df['avg_rating']).round(decimals=2)
df.head()
cols = df.columns.tolist()
cols = cols[:8]+cols[-2:]+cols[8:-2]
df = df[cols]
df

df.to_csv('preprocess_data.csv')

# #                                                                            Analyse

anay_goup = df.groupby("original_publish_year")[
    'minmax_norm_ratings'].mean().round(decimals=2)


# In[63]:


anay_goup.to_frame()


# In[61]:


anay_goup.to_frame()


# #                                         The Best Book Author

def get_book_author(name, df):
    f = df[df.loc[:, 'author'] == name]
    m = f['minmax_norm_ratings'].max()
    return m


get_book_author('Cassandra Clare', df)
