
# coding: utf-8

# ## Analysis 2
# 
# 1. After talking about the overall datasets, now let's look at the happiness scores distribution of each region.
# 
# 2. Visualizing Distributions of observations within region categories.
# 
# 3. according to the swarmplot, we can divided the score into four groups:#2-4,4-6,6-8; and we can give the lable of the three groups: 

# In[2]:

import pandas as pd
# from pythainlp.segment import segment
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats, integrate
get_ipython().magic('matplotlib inline')


# In[5]:

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


# In[10]:

#define the function to sort based on total score and add a new column named rank
def getRank(data):
    # sort the data by the total score with descending order.
    newData = data.sort_values(by='total score',ascending=False)
    # reindex the new data.
    newData['Rank'] = range(1,len(data) + 1)
    newData.index = range(0,len(data))
    return newData


# In[16]:

data2015=getTotalScore('data/2015.csv')
data2016=getTotalScore('data/2016.csv')


# In[17]:

data1 = getRank(data2015)
data2 = getRank(data2016)


# In[21]:

data1['Region'].value_counts()


# In[77]:

#Distributions of observations within categories
# Boxplots
# swarmplot
# to compare the distribution of a variable across levels of other variables.
sns.set()
ax = sns.boxplot(x="Region", y="total score", data=data1,linewidth=1.0)
ax = sns.swarmplot(x="Region", y="total score", data=data1, color=".5")
plt.xticks(rotation=45)
# plt.savefig('2-1.png')


# In[39]:

group = data1.groupby('Region')['total score'].mean()


# In[50]:

data3 = pd.concat([pd.DataFrame(group.index), pd.DataFrame(group.values)], axis=1)


# In[53]:

data3.columns=['Region', 'MeanScore']


# In[72]:

data4 = data3.sort_values(by='MeanScore',ascending=False)


# In[74]:

data4


# In[78]:

# Statistical estimation within categories
# bar plots
sns.set()
sns.barplot(x='Region', y='MeanScore',data=data4, color="salmon",palette="Blues_d");
plt.xticks(rotation=45)
plt.savefig('2-2.png')


# In[ ]:

# according to the swarmplot, we can divided the score into four groups:
#2-4,4-6,6-8; and we can give the lable of the three groups: 


# In[31]:

bins = [2,4,6,8]
group_names = ['low','Okay','Good']
categories = pd.cut(data1['total score'], bins, labels=group_names)
data1['categories'] = pd.cut(data1['total score'], bins, labels=group_names)


# In[32]:

pd.value_counts(data1['categories'])


# In[122]:

group2 = data1.groupby('Region')['categories'].value_counts()


# In[109]:

group3 = pd.DataFrame(group2)


# In[137]:

group3.head()


# In[99]:

#Plotting with categorical data
sns.countplot(y="Region", hue = "categories", data = data1, palette="Greens_d")
plt.savefig('2-3.png')


# In[145]:

sns.violinplot(x="Region", y="total score", hue="categories", data=data1,
                inner="stick", palette="Set1");
plt.xticks(rotation=45)
plt.savefig('2-5.png')


# In[97]:

sns.barplot(x="Region", y="total score", hue="categories", data=data1);
plt.xticks(rotation=45)
plt.savefig('2-6.png')


# In[146]:

# Point Plot
sns.pointplot(x="Region", y="total score", hue="categories", data=data1);
plt.xticks(rotation=45)
plt.savefig('2-7.png')


# In[ ]:




# In[ ]:




# In[ ]:




# In[34]:

sns.violinplot(x="total score", y="Region", hue="categories", data=data1);


# In[ ]:

data_low = data1[data1.categories=='low']
data_okay = data1[data1.categories=='Okay']
data_good = data1[data1.categories=='Good']


# In[ ]:




# In[28]:

# sns.set_style("whitegrid")
sns.set()
sns.swarmplot(x="Region", y="total score",  data=getRank(getTotalScore("data/2015.csv")))
plt.xticks(rotation=45)


# In[ ]:




# In[288]:

data2 = getTotalScore("data/2015.csv")
data2['y'] = (range(1, 10))


# In[295]:

# Scatterplots
sns.lmplot('y', 'total score', data=data2, fit_reg=False)


# In[ ]:

car['VEHICLE 2 Count']= car[['VEHICLE 2 TYPE']].apply(lambda x: 1 if(np.all(pd.notnull(x))) else 0, axis = 1)


# In[ ]:



