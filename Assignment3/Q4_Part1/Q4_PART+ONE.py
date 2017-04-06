
# coding: utf-8

# ## MOVIE AWARDS ANALYSIS
# ### Q4_PART ONE
# * Use ‘movies_awards’ data set.
# * You are supposed to extract data from the awards column in this dataset and split it into several columns. An example is given below.
# * The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
# * You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award.
# * If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated).
# * Create two separate columns for each award category (won and nominated).
# * Write your output to a csv file. (Sample output is given in next page)

# In[1]:

from pandas import Series, DataFrame
import pandas as pd
import csv


# In[2]:

movies = pd.read_csv('Data/movies_awards.csv')


# In[3]:

movies.head()


# In[13]:

df1 = DataFrame(movies['Awards'])


# In[15]:

df = df1.dropna()


# In[20]:

df.head(10)


# In[68]:

df.to_csv('simple.csv')


# In[ ]:

movie.title.apply(lambda x : int(x[-5:-1]) if x[-5:-1].isdigit() else 1990 ).tail()


# In[23]:

df.Awards.apply(lambda x : x[0]).value_counts()


# In[67]:

df.Awards.apply(lambda x : x[0]).head()


# In[ ]:

searchfor = ['og', 'at']
s[s.str.contains('|'.join(searchfor))]


# In[ ]:

searchfor = []


# In[93]:

awards_won= df.Awards.apply(lambda x : x[0] if x[0:5].find('win')!= -1 else 0 )


# In[95]:

awards_nominated= df.Awards.apply(lambda x : x[0] if x[0:5].find('nom')!= -1 else 0 )


# In[ ]:




# In[98]:

N = df.Awards.apply(lambda x : x if x.startswith('N') else 0 )


# In[129]:

# N.head(10)


# In[121]:

N1 = df.Awards.apply(lambda x : x[0:16] if x.startswith('N') else 0)


# In[124]:

# N1


# In[128]:

# awards_won = df.Awards.apply(lambda x : x[0] if x[0:5].find('win')!= -1 else x )


# In[127]:

# df2.head()


# In[126]:

# Awards_Won.head()


# In[125]:

# df.Awards.apply(lambda x : (x[0:5]))


# In[ ]:

df.Awards.apply(lambda x : int(x[-5:-1]) if x[-5:-1].isdigit() else 1990 ).tail()

