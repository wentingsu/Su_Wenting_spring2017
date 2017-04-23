# Final Exam - Spring 2017

# Topic: The World Happiness Report Data Analysis

---

## Part1 : General Dataset Description


| File Name        | Content           | 
| -------------- |:-------------| 
| 2015.csv        | happiness scores and ranking in 2015 | 
| 2016.csv     | happiness scores and ranking in 2016    |   

- The happiness scores and rankings use data from the Gallup World Poll. The reports review the state of happiness in the world today and show how the new science of happiness explains personal and national variations in happiness. 

- The columns following the happiness score estimate the extent to which each of seven factors: 'Economy (GDP per Capita), 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual'.

- They have no impact on the total score reported for each country, but they do explain why some countries rank higher than others.

---

## Part2: Overall Dataset Analysis

> **Analysis Summarize**.

| Analysis No.        | Content           | 
| ------------- |:-------------:| 
|Analysis 1       | Explore the Overall Happiness Scores and Distribution  | 
| Analysis 2      | Explore the Total Scores under different Regions    | 
| Analysis 3  | Explore Scores and Rank change between the 2015 and 2016  |
| Analysis 3  | Explore the variables and factors in Datasets Using PCA  |
| Analysis 5     | Explore Specific Regions and related Factors  | 


> **Overall Libraries Used**.

| Library No.        | Library Name           | 
| -------------- |:-------------| 
| 1        | Numpy | 
| 2     | Panda   |   
| 3     | seaborn |  
| 4     | matplotlib |  
| 5     | PCA |  

---

## Part3:   Analysis

## Analysis 1

> **Analyse the overall Datasets Distribution**

- There are seven numerical factors of happyniess. Calculate the total happiness score of each country and showed in a new column. The outcome is shown below.

#### Plot 1-1
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A1/1-1.png)

- Sort the data by the total score, and add a new column named Rank to show the happiness rank for each country.The outcome is shown below.

#### Plot 1-2
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A1/1-2.png)

> **Visualizing the distribution of overall dataset.**

- when dealing with a set of data, the first thing we'll do is get a sense for how the variables are distributed. The most convenient way to take a quick look at this univariate distribution in seaborn is the distplot() function which is shown below.

##### Plot 1-5
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A1/1-5.png)

- The first subplot are **histogram plot** which represents the distribution of data by forming bins along the range of the **total score** from 1 to 9,  and then drawing bars to show the number of observations that fall in each bin.

- The second subplot are **The kernel density estimate** which can be a useful tool for plotting the shape of a distribution. Like the histogram, the KDE plots encodes the density of observations on one axis with height along the other axis:

- The last subplot are the default distplot which represents both the histogram and kernel density estimate. 

>
> **Plotting bivariate distributions.**

- It can also be useful to visualize a bivariate distribution of two variables. 

- after we get the sorted data by **total score** and get the rank for each country,now let's look at the variables between rank and total score distribution, which are shown as plot 1-3 and 1-4.

##### Plot 1-3
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A1/1-3.png)

- we apply the **jointplot() function** in seaborn to creates a multi-panel figure that shows both the bivariate (or joint) relationship between two variables along with the totalscore and rank distribution of each on separate axes.
 
- The most familiar way to visualize a bivariate distribution is a **scatterplot** , where each observation is shown with point at the x and y values. This is analgous to a rug plot on two dimensions. You can draw a scatterplot with the matplotlib plt.scatter function, and it is also the default kind of plot shown by the jointplot() function:


In **Plot1-4**, it is also use the **kernel density estimation** to visualize a bivariate distribution.

##### Plot 1-4
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A1/1-4.png)


####  Analysis 2 Summarize:

1. In year 2016, the maximum totoal score is smaller than 2015.

2. From these univariate distribution plots we can find out that the total score mainly focus on the 4 to 6 in both 2015 and 2016 year.

3. The overall trend is the same. However, in year 2016 the slope is more flatterbe than 2015, which indicates that the overall score is better than 2015.

4. From plot 1-3 and 1-4,  we can find out that according to the asending rank, the total score is mostly focus on the 4 to 6 scores, which is the same as the distribution plots in plot 1-5.
 
5. in the first analysis, we mainly observe the overall dataset between 2015 and 2016 years. in next analysis we will use the categorical plots to find out how the scores distributed in different region.

---

## Analysis 2

> **Distributions of observations within categories**

- After talking about the overall datasets, now let's look at the happiness scores distribution of each **region**.

- The categorical scatterplot approach can provide about the distribution of values within each category. 

- There are several ways to summarize this information in ways that facilitate easy comparisons across the category levels. These generalize some of the approaches we discussed in the chapter to the case where we want to quickly compare across several distributions.

- The **Boxplots** below shows the three quartile values of the distribution along with extreme values. 

- The “whiskers” extend to points that lie within 1.5 IQRs of the lower and upper quartile, and then observations that fall outside this range are displayed independently. 

- Importantly, this means that each value in the boxplot corresponds to an actual observation in the totcal score under different Regions:

##### Plot 2-1
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-1.png)

> **Statistical estimation within categories**

- Often, rather than showing the distribution within each category, you might want to show the central tendency of the values. 

- The following bar plots shoes the mean value of happiness score for each **Range**. 

- This plot demonstrate that there are 10 unique region, and the highest mean total score is in **Australia and New Zealand** and **North America** and the lowest mean score is in **Sub-Saharan Africa**.

##### Plot 2-2
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-2.png)


> **Explore more on the score within seperately region** 

- according to the swarmplot, we can divided the score into three groups: 2-4,4-6,6-8; and we can give the lable of the three groups: low, okay and good. 
- Firstly, we use panda to generate the dataframe the numbers for each categories under different Region. the head of the output is like:

##### Plot 2-4
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-4.png)

- Now let's plot the new grouped data in bar plots.

##### Plot 2-3
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-3.png)

- A special case for the bar plot is when you want to show the number of observations in each category rather than computing a statistic for a second variable. This is similar to a histogram over a categorical, rather than quantitative, variable. In seaborn, it’s easy to do so with the countplot() function.

- Above plot shows the counts of each categories for every regine. We can clearly find out there is now low group in Western Europe,North America, Latin Ametica, Central and Eastern Europe, and Eastern Asia.

- A different approach is a violinplot(), which combines a boxplot with the kernel density estimation procedure. Shown as plot 2-5

##### Plot 2-5
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-5.png)

- This approach uses the kernel density estimate to provide a better description of the distribution of values. 

- Additionally, the quartile and whikser values from the boxplot are shown inside the violin. 


In plot 2-6, there are multiple observations in each category. we use the bar plot to compute a confidence interval around the estimate and plots. 

##### Plot 2-6
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-6.png)

- The following pointplot visualizing the change of the mean under each group and region.

- Additionally, pointplot connects points from the same hue category. This makes it easy to see how the main relationship is changing as a function of a second variable based on differences of slopes.

##### Plot 2-7
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-7.png)


####  Analysis 2 Summarize:

1. From Plot 2-1 we can find out some of the Regins like **Middle East and Northern Africa**, the range of the scores are high.

2. Although from plot 2-1 and 2-2 we can find out that in year 2015, the highest mean score is in **Australia and New Zealand**  and the lowest mean score is in **Sub-Saharan Africa**. However, there only two country in the highest Region.

3. Plot 2-3 clearly demonstrate the counts for each group and each Region. Plot 2-5 give the mean value of total score and also the the violin inside. From which we can find out that the happiness scores of Europe, america, and Asia, is higher than the Africa. 

---

## Analysis 3
>Compare the rank change for each Region in different year. 

- 1. Merge the 2015 and 2016 rank country table and create a new column to show the change of the rank for each contry and out put to a new csv.


##### Plot 3-1
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A3/3-1.png)
- This table shows the new table with adding the column named change which shows the rank change from year 2015 to year 2016.


##### Plot 3-2
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A3/3-2.png)
- the swarmplot shows the rank change under each region.
- from this plot we can see the largest increase is above 30, and the most decrease is also -30. 

##### Plot 3-3
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A3/3-3.png)
- above pointplot to compare the rank and mean of total score change from year 2015 to 2016
- from this plot we can not see too much change from theses two years. However from last plot we can see the maximum change can be -30 to 30. we have to deep look about the change of the rank.

##### Plot 3-4
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A3/3-4.png)
- firstly we divided the change into three group : increase that the rank change large than 0, and neutral group that the rank change is 0 and the decrease group that the rank change is small than 0.

- and then we add the group to a new column named **Trend**. 
- from the scatter plots we can see that the amongt of increase and decrease is almost the same

##### Plot 3-5
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A3/3-5.png)

- Plotting “wide-form” data
- While using “long-form” or “tidy” data is preferred, these functions can also by applied to “wide-form” data in a variety of formats, including pandas DataFrames or two-dimensional numpy arrays. These objects should be passed directly to the data parameter:
-from this violinplot we can also find out that the increase and the decrease is almost the same. But how did it change in different regions?

##### Plot 3-6
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A3/3-6.png)
- using factorplot to find out the rank change for each region. 

####  Analysis 3 Summarize:

---

## Analysis 4

> 1. in this Analysis, we will find out the factors that influence the outcomes of the total score.

> 2. I will use Principal Component Analysis (PCA) to analyse the seven factors of each column that  'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual' which one is the most important we will use PCA to Dimensionality Reduction.

> Principal Component Analysis (PCA) is a simple yet popular and useful linear transformation technique that is used in numerous applications, such as stock market predictions, the analysis of gene expression data, and many more. 



##### Plot 4-1
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A4/4-1.png)
- standardize the data prior to a PCA,to make sure it was measured on the same scales. 
- from 0-6, the columns stands for **Economy (GDP per Capita), 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', Dystopia Residual**

##### Plot 4-2
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A4/4-2.png)
- step1: Computing Eigenvectors and Eigenvalues:
- The eigenvectors and eigenvalues of a covariance (or correlation) matrix represent the "core" of a PCA: The eigenvectors (principal components) determine the directions of the new feature space, and the eigenvalues determine their magnitude. In other words, the eigenvalues explain the variance of the data along the new feature axes.
- the plot shows the correlation matrix of the dataset.


 - step2: Sorting Eigenpairs; The typical goal of a PCA is to reduce the dimensionality of the original feature space by projecting it onto a smaller subspace, where the eigenvectors will form the axes. However, the eigenvectors only define the directions of the new axis, since they have all the same unit length 1, which can confirmed by the following two lines of code:

##### Plot 4-3
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A4/4-3.png)
##### Plot 4-4
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A4/4-4.png)

- step3: Get Explained Variance

####  Analysis 4 Summarize:
---


## Analysis 5

> 1. from previous analyses we can find out that the happiness scores difference between Western Europe and Central and Eastern Europe is large. In this analysis, let's find out each how variables influence the outcomes.

##### add picture 5-1
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A5/5-1.png)
> **Visualizing pairwise relationships in a dataset**

- To plot multiple pairwise bivariate distributions in a dataset, you can use the pairplot() function. This creates a matrix of axes and shows the relationship for each pair of columns in a DataFrame. by default, it also draws the univariate distribution of each variable on the diagonal Axes:

##### add picture 5-2
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A5/5-2.png)

> based on analysis 4, we generate the two variables lmplot for Europe Regions to compare for the factors. 

- 1. Economy (GDP per Capita)','Family','Health (Life Expectancy)','Freedom'.


##### add picture 5-3
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A5/5-3.png)

##### add picture 5-4
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A5/5-4.png)

##### add picture 5-5
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A5/5-5.png)

##### add picture 5-6
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A5/5-6.png)

##### add picture 5-7
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A5/5-7.png)


####  Analysis 5 Summarize:





