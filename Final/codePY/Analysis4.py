
# coding: utf-8

# # Analysis 4
# 
# * analyse the variable
# * from previous analyses we can find out that the happiness scores difference between Western Europe and  Central and Eastern Europe is large. In this analysis, let's find out each how variables influence the outcomes.

# In[3]:

import pandas as pd
# from pythainlp.segment import segment
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
get_ipython().magic('matplotlib inline')


# In[4]:

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


# In[5]:

data2015=getTotalScore('data/2015.csv')
data2016=getTotalScore('data/2016.csv')


# In[6]:

#define the function to sort based on total score and add a new column named rank
def getRank(data):
    newData = data.sort_values(by='total score',ascending=False)
    newData['Rank'] = range(1,len(data) + 1)
    newData.index = range(0,len(data))
    return newData


# In[7]:

data1 = getRank(data2015)
data2 = getRank(data2016)


# In[9]:

data1.columns


# In[ ]:

# apply the PCA 


# In[13]:

from sklearn.preprocessing import StandardScaler


# In[12]:

df = data2015.ix[:,2:-1]


# In[33]:

df.head()


# In[17]:

# standardize the data prior to a PCA,to make sure it was measured on the same scales. 
X_std = StandardScaler().fit_transform(df)


# In[29]:

pd.DataFrame(X_std).head()


# In[30]:

mean_vec = np.mean(X_std, axis=0)
cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1)


# In[25]:

cov_mat = np.cov(X_std.T)
eig_vals, eig_vecs = np.linalg.eig(cov_mat)


# In[34]:

#correlation matrix
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(cov_mat, vmax=.8, square=True,linewidths=.5);
plt.savefig('4-2.png')


# In[100]:

# eig_pairs1


# In[40]:

tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)


# In[46]:

with plt.style.context('seaborn-whitegrid'):
    plt.figure(figsize=(6, 3))

    plt.bar(range(7), var_exp, alpha=0.5, align='center',
            label='individual explained variance')
    plt.step(range(7), cum_var_exp, where='mid',
             label='cumulative explained variance')
    plt.ylabel('Explained variance ratio')
    plt.xlabel('Principal components')
    plt.legend(loc='best')
    plt.tight_layout()
#     plt.show()
    plt.savefig('4-3.png')


# In[48]:

tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in eig_vals]
cum_var_exp = np.cumsum(var_exp)


# In[49]:

with plt.style.context('seaborn-whitegrid'):
    plt.figure(figsize=(6, 3))

    plt.bar(range(7), var_exp, alpha=0.5, align='center',
            label='individual explained variance')
    plt.step(range(7), cum_var_exp, where='mid',
             label='cumulative explained variance')
    plt.ylabel('Explained variance ratio')
    plt.xlabel('Principal components')
    plt.legend(loc='best')
    plt.tight_layout()
#     plt.show()
    plt.savefig('4-4.png')


# In[50]:

from sklearn.decomposition import PCA


# In[51]:

X = np.array(X_std)


# In[52]:

pca=PCA(n_components=6)


# In[53]:

pca.fit(X)


# In[54]:

Y = pd.DataFrame(pca.transform(X))


# In[59]:

Y.columns = ['Economy (GDP per Capita)','Family','Health (Life Expectancy)','Trust (Government Corruption)','Generosity','Dystopia Residual']


# In[60]:

Y.head()


# In[89]:

pca.explained_variance_ratio_


# In[ ]:



