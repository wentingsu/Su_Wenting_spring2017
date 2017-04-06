
# coding: utf-8

# ## NYC VEHICLE COLLISION ANALYSIS
# 
# ### Q1_PART TWO
# * Use ‘vehicle_collisions’ data set.
# * For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)
# * Display a few rows of the output use df.head().
# * Generate a csv output with five columns ('borough', 'one-vehicle', 'two- vehicles', 'three-vehicles', 'more-vehicles')

# In[99]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv


# In[149]:

car = pd.read_csv('Data/vehicle_collisions.csv')


# In[150]:

car.head()


# In[270]:

car.BOROUGH.value_counts()


# In[176]:

# calculate the count of Vehicle2
car['VEHICLE 2 Count']= car[['VEHICLE 2 TYPE']].apply(lambda x: 1 if(np.all(pd.notnull(x))) else 0, axis = 1)


# In[178]:

# calculate the count of Vehicle3
car['VEHICLE 3 Count']= car[['VEHICLE 3 TYPE']].apply(lambda x: 1 if(np.all(pd.notnull(x))) else 0, axis = 1)


# In[183]:

# calculate the count of Vehicle4
car['VEHICLE 4 Count']= car[['VEHICLE 4 TYPE']].apply(lambda x: 1 if(np.all(pd.notnull(x))) else 0, axis = 1)


# In[184]:

# calculate the count of Vehicle5
car['VEHICLE 5 Count']= car[['VEHICLE 5 TYPE']].apply(lambda x: 1 if(np.all(pd.notnull(x))) else 0, axis = 1)


# In[185]:

# calculate the count of Vehicle1
car['VEHICLE 6 Count']= car[['VEHICLE 1 TYPE']].apply(lambda x: 1 if(np.all(pd.notnull(x))) else 0, axis = 1)


# In[187]:

# get all the number of count and add a new column named Total count
car['Total Count'] = car['VEHICLE 2 Count']+car['VEHICLE 3 Count']+car['VEHICLE 4 Count']+car['VEHICLE 5 Count']+car['VEHICLE 6 Count']


# In[293]:

#define a function to get the distribution for each area
def getBOROUGH(name):
    # pass the different BOROUGH values 
    one = car[car.BOROUGH==name]
    # Get the total count series of the involved cars
    s = one['Total Count'].value_counts().sort_index()
    # calculate the 'more-vehicles' that more than three
    s[4]= s[4] + s[5]
    newS = s.drop([0,5])
    return newS


# In[294]:

#Concatenating Along an Axis
output = pd.concat([getBOROUGH('BROOKLYN'), getBOROUGH('QUEENS'),getBOROUGH('MANHATTAN'),getBOROUGH('BRONX'),getBOROUGH('STATEN ISLAND')], axis=1).T


# In[295]:

output


# In[296]:

car.BOROUGH.value_counts().index


# In[300]:

# add the index name
output1 = output.set_index(car.BOROUGH.value_counts().index)


# In[307]:

# add the colums name
output1.columns=['ONE_VEHICLE_INVOLVED', 'TWO_VEHICLES_INVOLVED', 'THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED']


# In[318]:

output1.columns.name='BOROUGH'


# In[320]:

# Write DataFrame to CSV 
output1.to_csv('Q1_PART TWO.csv')


# In[321]:

output2 = pd.read_csv('Q1_PART TWO.csv')


# In[323]:

output2

