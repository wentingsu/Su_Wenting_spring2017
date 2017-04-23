
# coding: utf-8

# # Analysis 5
# 
# * analyse the variable
# * from previous analyses we can find out that the happiness scores difference between Western Europe and  Central and Eastern Europe is large. In this analysis, let's find out each how variables influence the outcomes.

# In[2]:

import pandas as pd
# from pythainlp.segment import segment
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
get_ipython().magic('matplotlib inline')


# In[3]:

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


# In[4]:

data2015=getTotalScore('data/2015.csv')
data2016=getTotalScore('data/2016.csv')


# In[5]:

#define the function to sort based on total score and add a new column named rank
def getRank(data):
    newData = data.sort_values(by='total score',ascending=False)
    newData['Rank'] = range(1,len(data) + 1)
    newData.index = range(0,len(data))
    return newData


# In[6]:

data1 = getRank(data2015)
data2 = getRank(data2016)


# In[7]:

data1['Region'].value_counts()


# In[8]:

w_europe = data1[data1.Region=='Western Europe']
ec_europe = data1[data1.Region=='Central and Eastern Europe']
europe = pd.concat([w_europe,ec_europe],axis=0)
europe.head()


# In[11]:

# Visualizing pairwise relationships in a dataset
selectCols=  ['total score','Economy (GDP per Capita)','Family','Health (Life Expectancy)','Freedom','Trust (Government Corruption)','Region']
sns.pairplot(europe[selectCols], hue='Region',size=2.8)
plt.savefig('5-1.png')


# In[30]:

selectCols= ['Economy (GDP per Capita)','Family','Health (Life Expectancy)','Freedom','Trust (Government Corruption)']
for one in selectCols:
    sns.lmplot(data=europe, x = one, y='total score', hue='Region',size=4.5)
    plt.savefig('5'+one +'.png')


# In[17]:

# get the DataFrame of all aisa contries
se_Asia = data1[data1.Region=='Southeastern Asia']
s_Asia = data1[data1.Region=='Southern Asia']
e_Asia = data1[data1.Region=='Eastern Asia']

asia = pd.concat([se_Asia,s_Asia,e_Asia],axis=0)
asia.head()


# In[18]:

sns.lmplot(data=asia,x='Health (Life Expectancy)',y='total score',hue="Region")


# In[31]:

sns.lmplot(data=asia, x = 'Freedom', y='total score', hue='Region',size=4.5)
plt.savefig('5-6.png')


# In[ ]:

se_Asia = data1[data1.Region=='Southeastern Asia']
s_Asia = data1[data1.Region=='Southern Asia']
e_Asia = data1[data1.Region=='Eastern Asia']



# In[32]:

f, axes = plt.subplots(2, 2, figsize=(16, 16))
axes = axes.flatten()
compareCols = ['Economy (GDP per Capita)','Family','Health (Life Expectancy)','Trust (Government Corruption)']
for i in range(len(compareCols)):
    col = compareCols[i]
    axi = axes[i]
    sns.distplot(se_Asia[col],color='blue' , label='Southeastern Asia', ax=axi)
    sns.distplot(s_Asia[col],color='r', label='Southern Asia',ax=axi)
    sns.distplot(e_Asia[col],color='green', label='Eastern Asia',ax=axi)
    axi.legend()
plt.savefig('5-7.png')

