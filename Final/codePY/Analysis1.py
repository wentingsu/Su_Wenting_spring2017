
# coding: utf-8

# ## Analysis 1
# 
# 1. There are six numerical factors of happyniess. Calculate the total happiness score of each country and showed in a new column.
# 
# 2. Sort the data by the total score, and add a new column named Rank to show the happiness rank for each country.
# 
# 3. Visualizing the distribution of a dataset. And analysis according to the plots. 
# 
# 4. Generate the plots to show the overall datasets: Distribute Plot. 
# 
# 3. merge the 2015 and 2016 rank country table and create a new column to show the change of the rank for each contry and out put to a new csv. 

# In[382]:

import pandas as pd
# from pythainlp.segment import segment
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats, integrate
get_ipython().magic('matplotlib inline')


# In[275]:

# define the function to calculate and create the total score of happiness.
def getTotalScore(str):
    # load the data
    data = pd.read_csv(str)
    # get all the columns that to be added together
    colums = data.ix[:,2:]
    # add the new column named 'total score'
    # data['total score'] = colums.sum(axis = 1).head()
    data['total score'] = np.sum(colums,axis = 1)
    # return the data frame
    return data


# In[296]:

data2015=getTotalScore('data/2015.csv')
data2016=getTotalScore('data/2016.csv')


# In[297]:

data2015.head()


# In[319]:

#define the function to sort based on total score and add a new column named rank
def getRank(data):
    # sort the data by the total score with descending order.
    newData = data.sort_values(by='total score',ascending=False)
    # reindex the new data.
    newData['Rank'] = range(1,len(data) + 1)
    newData.index = range(0,len(data))
    return newData


# In[320]:

data1 = getRank(data2015)
data2 = getRank(data2016)


# In[321]:

data1.head()


# In[322]:

x1 = data1['total score']
x2 = data2['total score']


# In[385]:

sns.jointplot('Rank', 'total score', data=data1,color='g')
plt.savefig('1-3.png')


# In[386]:

sns.jointplot('Rank', 'total score', data=data1,kind="kde")
plt.savefig('1-4.png')


# In[387]:

# generate th distribution plot for 2015 and 2016 year to 
# reserve and compare the trend of the score
f, axes = plt.subplots(3, 2, figsize=(16, 16), sharex=True)
axes = axes.flatten()

sns.distplot(x1, kde=False, rug=True, ax=axes[0])
sns.distplot(x2, kde=False, rug=True, ax=axes[1],color='g')

sns.kdeplot(x1, shade=True, ax=axes[2]);
sns.kdeplot(x2, shade=True, ax=axes[3], color = 'g');

sns.distplot(x1, ax=axes[4])
sns.distplot(x2, ax=axes[5],color='g')

plt.subplots_adjust(wspace=0)

plt.savefig('1-5.png')

