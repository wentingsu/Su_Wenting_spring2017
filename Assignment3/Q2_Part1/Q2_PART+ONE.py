
# coding: utf-8

# ## EMPLOYEE COMPENSATION ANALYSIS
# ### Q2_PART ONE
# * Use 'employee_compensation' data set.
# * Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.
# * Output should contain the organization group and the departments in each organization group with the total compensation from highest to lowest value.
# * Display a few rows of the output use df.head().
# * Generate a csv output.

# In[242]:

from pandas import Series, DataFrame
import pandas as pd
import csv


# In[243]:

employee = pd.read_csv('Data/employee_compensation.csv')


# In[244]:

employee.head()


# In[371]:

groupName = employee['Organization Group'].unique()


# In[372]:

# check the unique group name
groupName 


# In[373]:

# define the function to get the mean of each department for each group
def getDepMean(groupName):
    # pass the groupName and get df of each group
    group = employee[employee['Organization Group']==groupName] 
    # calculate each group's mean with each department
    calMean = group.groupby('Department')['Total Compensation'].mean()
    # extract the value and department name in the df
    s1 = DataFrame(calMean.index)
    s2 = DataFrame(calMean.values, columns=['Means'])
    # combine the df and sort by the mean value and add the orfamization name column
    frame = pd.concat([s1, s2], axis=1)
    frame['Organization'] = groupName
    frame.sort_values(by='Means',ascending=False)
    # switch the clolumn to organize, group and means.
    output = frame[['Organization','Department','Means']]
    # return the output.
    return output


# In[375]:

group1 = getDepMean(groupName[0])
group2 = getDepMean(groupName[1])
group3 = getDepMean(groupName[2])
group4 = getDepMean(groupName[3])
group5 = getDepMean(groupName[4])
group6 = getDepMean(groupName[5])
group7 = getDepMean(groupName[6])


# In[394]:

output = pd.concat([group1, group2,group3,group4,group5,group6], axis=0)


# In[396]:

# Write DataFrame to CSV 
output.to_csv('Q2_PART ONE.csv')


# In[397]:

output.head()


# In[ ]:



