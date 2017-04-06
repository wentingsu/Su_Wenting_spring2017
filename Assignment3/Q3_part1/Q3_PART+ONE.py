
# coding: utf-8

# ## CRICKET MATCHES ANALYSIS
# ### Q3_PART ONE
# * Use ‘cricket_matches’ data set.
# * Calculate the average score for each team which host the game and win the game.
# * Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition.
# * Display a few rows of the output use df.head()
# * Generate a csv output

# In[39]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv


# In[2]:

cricket = pd.read_csv('Data/cricket_matches.csv')


# In[3]:

cricket.head()


# In[15]:

# find the df that the host is winner
cricket1 = cricket[cricket['home']== cricket['winner']]


# In[72]:

# find the df that the host is winned runs1
cricketinning1 = cricket1[cricket1['home']==cricket1['innings1']]


# In[85]:

# get the df that contains the scores and home name
inning1score = cricketinning1[['home','innings1_runs']]


# In[86]:

inning1score.head()


# In[87]:

# change the column name to score to make the calculation easy
inning1score=inning1score.rename(columns = {'innings1_runs':'score'})


# In[89]:

inning1score.head()


# In[17]:

# find the df that the host is winned runs2
cricketinning2 = cricket1[cricket1['home']==cricket1['innings2']]


# In[21]:

# find the df that the host is winned runs1
inning2score = cricketinning2[['home','innings2_runs']]


# In[90]:

# change the column name to score to make the calculation easy
inning2score=inning2score.rename(columns = {'innings2_runs':'score'})


# In[92]:

inning2score.head()


# In[104]:

# get the df that contains the score for each team
frame = pd.concat([inning1score, inning2score], axis=0)


# In[106]:

frame.head()


# In[111]:

# calculate the average score according to the 
calAve = frame.groupby('home')['score'].mean()


# In[115]:

s1 = DataFrame(calAve.index)
s2 = DataFrame(calAve.values, columns=['Score'])


# In[116]:

output = pd.concat([s1, s2], axis=1)


# In[118]:

# Write DataFrame to CSV 
output.to_csv('Q3_PART ONE.csv')


# In[119]:

output = pd.read_csv('Q3_PART ONE.csv')


# In[120]:

output.head()

