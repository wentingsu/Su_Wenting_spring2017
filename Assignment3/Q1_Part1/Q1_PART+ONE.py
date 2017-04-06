
# coding: utf-8

# ## NYC VEHICLE COLLISION ANALYSIS
# 
# ### Q1_PART ONE
# * Use ‘vehicle_collisions’ data set.
# * For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City.
# * Display a few rows of the output use df.head().
# * Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)

# ### ? does the nan conted in the accident? 

# In[133]:

from pandas import Series, DataFrame
import pandas as pd


# In[161]:

import csv


# In[135]:

car = pd.read_csv('Data/vehicle_collisions.csv')


# In[136]:

car.head()


# In[138]:

# get the year from all data
car['Year'] = pd.to_datetime(car['DATE']).dt.year


# In[139]:

# get the month from all data
car['Month'] = pd.to_datetime(car['DATE']).dt.month


# In[145]:

# get the 2016 year's data
YearIn = car[car['Year']==2016]


# In[166]:

MCountList=[]
MList=[]
PList=[]
NYCList =[]

for m in range(1, 13):
    MonthIn = YearIn[YearIn['Month']==m]
    TotalCount = YearIn[YearIn['Month']==m].count().Month
    Mcount = MonthIn[MonthIn['BOROUGH']=='MANHATTAN'].count().BOROUGH
    Percent = Mcount/TotalCount
    
    MList.append(m)
    MCountList.append(Mcount)
    NYCList.append(TotalCount)   
    PList.append(Percent)
    
# MCountList
# MList
# PList
# NYCList


# In[167]:

data = {'MONTH':MList,'MANHATTAN':MCountList,'NYC':NYCList,'PERCENTAGE':PList}
frame = DataFrame(data)
frame.head()


# In[170]:

# Write DataFrame to CSV 
frame.to_csv('Q1_PART ONE.csv')


# In[171]:

output = pd.read_csv('Q1_PART ONE.csv')


# In[172]:

output

