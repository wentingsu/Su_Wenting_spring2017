
# coding: utf-8

# ## EMPLOYEE COMPENSATION ANALYSIS
# ### Q2_PART TWO
# 
# * Use 'employee_compensation' data set.
# * Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee.
# * Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# * For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value.
# * Display the top 5 Job Families according to this percentage value using df.head().
# * Write the output (jobs and percentage value) to a csv.

# In[1]:

from pandas import Series, DataFrame
import pandas as pd
import csv


# In[2]:

employee = pd.read_csv('Data/employee_compensation.csv')


# In[384]:

employee.head()


# In[60]:

# Filter data by calendar year 
CalendarYear = employee[employee['Year Type']=='Calendar']


# In[ ]:

CalendarYear['Employee Identifier']


# In[354]:

# get the series of JobFamily for each employee
JobFamily = employee.groupby('Employee Identifier')['Job Family'].value_counts()


# In[117]:

# define the function to calculate the mean for each column of each employee.
def allAverage(col):
    ave = employee.groupby('Employee Identifier')[col].mean()
    return ave


# In[118]:

# get all the average for each cokumn 
Salaries = allAverage('Salaries')


# In[83]:

Overtime = allAverage('Overtime')


# In[84]:

OtherS = allAverage('Other Salaries')


# In[85]:

TotalS = allAverage('Total Salary')


# In[86]:

Retirement= allAverage('Retirement')


# In[87]:

Health = allAverage('Health/Dental')


# In[88]:

OtherB = allAverage('Other Benefits')


# In[89]:

TotalB = allAverage('Total Benefits')


# In[90]:

TotalC = allAverage('Total Compensation')


# In[359]:

# combine all the series 
frame = pd.concat([Salaries,Overtime, OtherS, TotalS,Retirement,Health,OtherB,TotalB,TotalC], axis=1)


# In[210]:

frame['5%Salaries']=frame['Salaries'].apply(lambda x : x*0.05)


# In[223]:

# find the people whose over time salary is greater than 5% of salaries
frameObig = frame[frame['Overtime']>frame['5%Salaries']]


# In[361]:

frameObig.head()


# In[281]:

people = DataFrame(frameObig.index)


# In[336]:

peopleList = people['Employee Identifier'].values.tolist()


# In[362]:

# get the series of JobFamily for each employee
JobFamily = DataFrame(employee.groupby('Employee Identifier')['Job Family'].value_counts())


# In[363]:

JobFamily.index.values
# apply(lambda x : x[0][1])


# In[364]:

JobFamilyf = DataFrame(JobFamily.index.values,columns=['Job Family'])


# In[365]:

JobFamilyf['Employee Identifier'] = JobFamilyf['Job Family'].apply(lambda x : x[0])


# In[366]:

JobFamilyf['Job Family'] = JobFamilyf['Job Family'].apply(lambda x : x[1])


# In[367]:

newF = JobFamilyf[['Employee Identifier', 'Job Family']]


# In[368]:

newF.head()


# In[377]:

df = pd.DataFrame(index=peopleList)


# In[379]:

df.index.values


# In[385]:

# newF['Employee Identifier'].apply(lambda x : x)


# In[ ]:




# In[386]:

# employee['Job Family'].value_counts()


# In[128]:

employee['Employee Identifier'].unique()


# In[32]:




# In[ ]:




# In[ ]:



