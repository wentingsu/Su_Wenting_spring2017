
# coding: utf-8

# # Analysis 3 : analyse the variable

# * merge the 2015 and 2016 rank country table and create a new column to show the change of the rank for each contry and out put to a new csv. 

# In[1]:

import pandas as pd
# from pythainlp.segment import segment
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
get_ipython().magic('matplotlib inline')


# In[2]:

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


# In[3]:

data2015=getTotalScore('data/2015.csv')
data2016=getTotalScore('data/2016.csv')


# In[4]:

#define the function to sort based on total score and add a new column named rank
def getRank(data):
    newData = data.sort_values(by='total score',ascending=False)
    newData['Rank'] = range(1,len(data) + 1)
    newData.index = range(0,len(data))
    return newData


# In[5]:

data1 = getRank(data2015)
data2 = getRank(data2016)


# In[6]:

data2.head()


# In[13]:

# extract the region, country and rank in year 2015
data3 = pd.concat([data1['Country'],data1['Region'],data1['Rank'],data1['total score']],axis=1)
# extract the region, country and rank in year 2016
data4 = pd.concat([data2['Country'],data2['Rank'],data2['total score']],axis=1)
# merge the data in year 2015 and 2016
data5 = data3.merge(data4, on = 'Country', how = 'inner')
# get the new column named 'change' means the change of the rank from year 2015 to year 2016
data5['change'] = data5['Rank_y'] - data5['Rank_x']


# In[14]:

data5.head(6)


# In[18]:

# sort the change according to the change of scores.
data6 = data5.sort_values(by='change',ascending=False)


# In[19]:

data6.head()


# In[20]:

data6['change'].value_counts().head()


# In[24]:

sns.set()
sns.swarmplot(x="Region", y="change",  data=data5)
plt.xticks(rotation=45)
plt.savefig('3-2.png')


# In[27]:

# pointplot to compare the rank and total score change from year 2015 to 2016
f, axes = plt.subplots(2, 1, figsize=(16, 16), sharex=True)
axes = axes.flatten()
# The change of the mean
sns.pointplot(x="Region", y="total score_x", data=data5, color='r', ax = axes[0])
sns.pointplot(x="Region", y="total score_y", data=data5, color='g',ax = axes[0])

sns.pointplot(x="Region", y="Rank_x", data=data5, color='r',ax = axes[1])
sns.pointplot(x="Region", y="Rank_y", data=data5, color='g',ax = axes[1])
plt.xticks(rotation=45)

plt.savefig('3-3.png')


# In[15]:

increase = data5[data5.change>0]
neutral = data5[data5.change==0]
decrese = data5[data5.change<0]

increase['Trend'] = 'increase'
neutral['Trend'] = 'neutral'
decrese['Trend'] = 'decrese'

data7 = pd.concat([increase,neutral,decrese],axis=0)
# data7


# In[16]:

data7.head()


# In[192]:

data7['Trend'].value_counts()


# In[28]:

# Scatterplots
sns.lmplot('Rank_x', 'change', data=data6, fit_reg=False)
plt.savefig('3-4.png')


# In[29]:

# Additionally, these functions accept vectors of Pandas or numpy objects rather than variables in a
sns.violinplot(x=data7.Trend, y=data7.change);
plt.savefig('3-5.png')


# In[31]:

# using factorplot to find out the rank change for each region. 
g = sns.factorplot("Trend", col="Region", col_wrap=3,
                 data=data7[data7.Region.notnull()],
                 kind="count", size=3.5, aspect=.8, palette="Set2")
plt.savefig('3-6.png')


# In[ ]:

# Analyse the value-counts of the change from 2015-2016


# In[69]:

y = pd.DataFrame(data5['change'].value_counts().index)


# In[70]:

x = pd.DataFrame(data5['change'].value_counts().values)


# In[71]:

changevalue = pd.concat([y,x],axis=1)


# In[74]:

changevalue.columns = ['change', 'values']

