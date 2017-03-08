# Su_Wenting_spring2017


# Part1 Analysis

Kenneth Lay formed Enron in 1985 by after merging Houston Natural Gas and InterNorth;
Jeffrey Skilling was the former CEO of the Enron Corporation;


## Analyse 1:

1. Under the sent box of Kenneth Lay, open all the emails in it.
2. Find out how many email address that Kenneth Lay is sent.
3. Calculate the frequency of each email address and show the top 10 most frequent email address

##### output: 
##### 1. get the length of the email address that Kenneth Lay is sent.
##### 2. calculate the frequency of each email address 
##### 3. show the top 10 most frequent email address

## Analyse 2:

1. Under the inbox of Kenneth Lay and Jeffrey Skilling, open all the emails in it.
2. Find out how many email address that Kenneth Lay and Jeffrey Skilling have receieved. Take top 10 email address from Kenneth 
Lay and top 10 from Jeffrey Skilling.
3. Find out the top 5 emails address that both Kenneth Lay and Jeffrey Skilling receieved, and top 5 that their different emails.

##### output: 
 1. get the number of the email that both  Lay and  Skilling receieved,
 2. take the top 10 email address of each person
 3. get the top 5 email common email addresses and different

## Analyse 3:

 1. Pick all the files under CEO skilling-j folder and Get all the email Subjects.
 2. Calculate the frequency of each word in all subjects, and save the data as CSV file.(rank, word, frequency)
 3. Generate the Log-Log figure to prove if Zipf's law works in this.

##### output: 
 1. read all the folders and all files under skilling-j
 2. get all the frequency of words from all subjects and write the results to cvs with rank, word, frequency. result file namd: subjectProve.csv.
 3. conclusion: Conclusion: the subjects word frequency meets the Zipf's law. the picture is in the .jupyter named: Midterm_Part1_Analyse.ipynb


# Part2 Analysis

## Collection Data:
#### Archive API;
get the data from year 1851 to year 2016 
Output: in data/Archive files

#### Article Search API;
get the data of the query key equals all the unique presidents' name that I got from NLTP inaugral library.
Output: in data/ArticleSearch

#### Books API;
get the data of the title key equals all the unique presidents' name that I got from NLTP inaugral library.
Output: in data/Books

#### Community API;
get the comment data of the users from 2014 t0 2016 
Output: in data/Community


## Analyse 1:

1. Using the Archive API data, read all json files in year 2016
2. Each json file contain a key called 'keywords' contains the details of each document.
3. Extract each of the 'keywords' data and write it in an excel sheet. also add the related '_id'

##### output: 
 1.get all write the list of 'ID','Name','Rank','is_Major' to the csv file from year 2016-1-1 to 2016-12-31.
 2.the output file named: Archive.csv


## Analyse 2:

1. Using the Article Search API and Books API data, read all json files in 'ArticleSearch' and 'Books'
2. In the Article Search API, each json file contain keys called 'main', for each president, find out the number of the 'main' that contains president's name
3. In the Books API, each json file contain a key 'title', for each president, find out the number of titles that contains his name. and compare with 2.

##### output: 
 1. get the president frequency using Article Search API data
 2. get the president frequency using Books API data
 Conclusion: the number of preseidents' name at book API 'title' key are more than the Article Search API 'main' key.


## Analyse 3:

1. Using the Community API read all json files in 'Community/'
2. In the Community API, each json file contain a key called 'userID', find out the number of unique Users in year 2014, 2015 and 2016; and compare the change trend.
3. In the Community API, each json file contain a key called 'commentType', find out the number of each commentType. compare the three years.

##### output: 
 1. get the unique number of users in year 2014 to 2016
 conclusion: compared with 2014, the user increased by around 600, however in 2016 it is slightly cutdown
 2. get the different comment Types and counts in year 2014 to 2016
 conclusion: from the 2014 to 2016 the amount of comments is also increased, and the user usually used to comment and replay the comment.







