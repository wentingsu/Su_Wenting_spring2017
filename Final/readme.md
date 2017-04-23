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

> **Analysis Topics**.

| Analysis No.        | Content           | 
| ------------- |:-------------:| 
|Analysis 1       | **Explore the Overall Happiness Scores and Distribution**  | 
| Analysis 2      | **Explore the Total Scores under different Regions**    | 
| Analysis 3  | **Explore Scores and Rank change between the 2015 and 2016**  |
| Analysis 3  | **Explore the variables and factors in Datasets Using PCA**  |
| Analysis 5     | **Explore Specific Regions and related Factors**  | 


> **Overall Libraries Used**.

| Library No.        | Library Name           | 
| -------------- |:-------------| 
| 1        | Numpy | 
| 2     | Panda   |   
| 3     | seaborn |  
| 4     | matplotlib |  
| 5     | PCA |  

---

## Analysis 1

> 1. There are six numerical factors of happyniess. Calculate the total happiness score of each country and showed in a new column.

##### add picture 1-1
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A1/1-1.png)

> 2. Sort the data by the total score, and add a new column named Rank to show the happiness rank for each country.

##### add picture 1-2
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A1/1-2.png)
> **examining univariate and bivariate distributions**

 
> 3. ** Visualizing the distribution of overall dataset.**  And analysis according to the plots. 

#####  add picture 1-5
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A1/1-5.png)
- when dealing with a set of data, the first thing we'll do is get a sense for how the variables are distributed. The most convenient way to take a quick look at this univariate distribution in seaborn is the distplot() function. 

- from the plot shown as following. 

- The first line are ** histogram plot ** which represents the distribution of data by forming bins along the range of the ** total score ** from 1 to 9,  and then drawing bars to show the number of observations that fall in each bin.

- The second line are ** The kernel density estimate** which can be a useful tool for plotting the shape of a distribution. Like the histogram, the KDE plots encodes the density of observations on one axis with height along the other axis:

- The last line are the default distplot which represents both the histogram and kernel density estimate. 

##### Summarize:

- 1. the most highest score is less than 2015.
- 2. from these univariate distributions plots we can get the point that both in 2015 and 2016 year, the total score mainly concentrated on the 4.5 to 5.5.
- 3. the overall trend is the same, but in year 2015 ir sill be more flat than the 2015, which indicates that the overall score is higher than 2015.


> 4. ** Visualizing the distribution of overall dataset.**  Plotting bivariate distributions

##### add picture 1-3
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A1/1-3.png)
##### add picture 1-4
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A1/1-4.png)

- It can also be useful to visualize a bivariate distribution of two variables. 

- after we get the sorted data by **total score** and get the rank for each country,now let's look at the variables between rank and total score distribution.

- we apply the **jointplot() function** in seaborn to creates a multi-panel figure that shows both the bivariate (or joint) relationship between two variables along with the univariate (or marginal) distribution of each on separate axes.
 
- The most familiar way to visualize a bivariate distribution is a **scatterplot** , where each observation is shown with point at the x and y values. This is analgous to a rug plot on two dimensions. You can draw a scatterplot with the matplotlib plt.scatter function, and it is also the default kind of plot shown by the jointplot() function:

- It is also posible to use the **kernel density estimation** procedure described above to visualize a bivariate distribution. In seaborn, this kind of plot is shown with a contour plot and is available as a style in jointplot():

##### Summarize:
- from both above plot we can get the point that according the asending rank, the score is mostly concentrate on the 4 to 6 scores, which is the same as the distribution plots.
 
 
- in the first analysis, we mainly observe the overall dataset between 2015 and 2016 years. in next analysis we will use the categorical plots to find out how the scores distributed in different region.

---

## Analysis 2

> 1. After talking about the overall datasets, now let's look at the happiness scores distribution of each **region**.

> **Distributions of observations within categories**

- At a certain point, the categorical scatterplot approach becomes limited in the information it can provide about the distribution of values within each category. There are several ways to summarize this information in ways that facilitate easy comparisons across the category levels. These generalize some of the approaches we discussed in the chapter to the case where we want to quickly compare across several distributions.


##### add picture 2-1
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-1.png)
- Above **Boxplots** shows the three quartile values of the distribution along with extreme values. 

- The “whiskers” extend to points that lie within 1.5 IQRs of the lower and upper quartile, and then observations that fall outside this range are displayed independently. 

- Importantly, this means that each value in the boxplot corresponds to an actual observation in the data:


> 2. **Statistical estimation within categories**

##### add picture 2-2
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-2.png)
- Often, rather than showing the distribution within each category, you might want to show the central tendency of the values. 
-Seaborn has two main ways to show this information, but importantly, the basic API for these functions is identical to that for the ones discussed above.

- this bar plots shoes the mean value of happiness score for each **Range**. 

- summarize: this plot demonstrate that there are 10 unique region, and the most 
from this plot we can clearly find out that the highest mean score is in **Australia and New Zealand** and **North America** and the lowest mean score is in **Sub-Saharan Africa**.

> 3. Explore more on the score within seperately **region** according to the swarmplot, we can divided the score into three groups:#2-4,4-6,6-8; and we can give the lable of the three groups: low, okay and good. Firstly, we use panda to generate the dataframe the numbers for each categories under different Region.

##### add picture 2-4
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-4.png)
- Now let's plot the new data in bar plots.

##### add picture 2-3
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-3.png)
- A special case for the bar plot is when you want to show the number of observations in each category rather than computing a statistic for a second variable. This is similar to a histogram over a categorical, rather than quantitative, variable. In seaborn, it’s easy to do so with the countplot() function:

##### add picture 2-5
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-5.png)
- A different approach is a violinplot(), which combines a boxplot with the kernel density estimation procedure described in the distributions tutorial:

- This approach uses the kernel density estimate to provide a better description of the distribution of values. Additionally, the quartile and whikser values from the boxplot are shown inside the violin. Because the violinplot uses a KDE, there are some other parameters that may need tweaking, adding some complexity relative to the straightforward boxplot:

- It can also be useful to combine swarmplot() or swarmplot() with violinplot() or boxplot() to show each observation along with a summary of the distribution:

##### add picture 2-6
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-6.png)
 - A familiar style of plot that accomplishes this goal is a bar plot. In seaborn, the barplot() function operates on a full dataset and shows an arbitrary estimate, using the mean by default. 
 - When there are multiple observations in each category, it also uses bootstrapping to compute a confidence interval around the estimate and plots that using error bars.
 
##### add picture 2-7
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A2/2-7.png)
- An alternative style for visualizing the same information is offered by the pointplot() function. 
- This function also encodes the value of the estimate with height on the other axis, but rather than show a full bar it just plots the point estimate and confidence interval. 
- Additionally, pointplot connects points from the same hue category. This makes it easy to see how the main relationship is changing as a function of a second variable, because your eyes are quite good at picking up on differences of slopes:


- summarize:
1.
2.
3.

---
## Analysis 3
> 1. Merge the 2015 and 2016 rank country table and create a new column to show the change of the rank for each contry and out put to a new csv.

> 2. compare the change for each Region in different year. 

##### add picture 3-1
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A3/3-1.png)
- This table shows the new table with adding the column named change which shows the rank change from year 2015 to year 2016.


##### add picture 3-2
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A3/3-2.png)
- the swarmplot shows the rank change under each region.
- from this plot we can see the largest increase is above 30, and the most decrease is also -30. 

##### add picture 3-3
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A3/3-3.png)
- above pointplot to compare the rank and mean of total score change from year 2015 to 2016
- from this plot we can not see too much change from theses two years. However from last plot we can see the maximum change can be -30 to 30. we have to deep look about the change of the rank.

##### add picture 3-4
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A3/3-4.png)
- firstly we divided the change into three group : increase that the rank change large than 0, and neutral group that the rank change is 0 and the decrease group that the rank change is small than 0.

- and then we add the group to a new column named **Trend**. 
- from the scatter plots we can see that the amongt of increase and decrease is almost the same

##### add picture 3-5
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A3/3-5.png)

- Plotting “wide-form” data
- While using “long-form” or “tidy” data is preferred, these functions can also by applied to “wide-form” data in a variety of formats, including pandas DataFrames or two-dimensional numpy arrays. These objects should be passed directly to the data parameter:
-from this violinplot we can also find out that the increase and the decrease is almost the same. But how did it change in different regions?

##### add picture 3-6
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A3/3-6.png)
- using factorplot to find out the rank change for each region. 

---

## Analysis 4
> 1. in this Analysis, we will find out the factors that influence the outcomes of the total score.

> 2. I will use Principal Component Analysis (PCA) to analyse the seven factors of each column that  'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual' which one is the most important we will use PCA to Dimensionality Reduction.

> Principal Component Analysis (PCA) is a simple yet popular and useful linear transformation technique that is used in numerous applications, such as stock market predictions, the analysis of gene expression data, and many more. 



##### add picture 4-1
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A4/4-1.png)
- standardize the data prior to a PCA,to make sure it was measured on the same scales. 
- from 0-6, the columns stands for **Economy (GDP per Capita), 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', Dystopia Residual**

##### add picture 4-2
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A4/4-2.png)
- step1: Computing Eigenvectors and Eigenvalues:
- The eigenvectors and eigenvalues of a covariance (or correlation) matrix represent the "core" of a PCA: The eigenvectors (principal components) determine the directions of the new feature space, and the eigenvalues determine their magnitude. In other words, the eigenvalues explain the variance of the data along the new feature axes.
- the plot shows the correlation matrix of the dataset.


 - step2: Sorting Eigenpairs; The typical goal of a PCA is to reduce the dimensionality of the original feature space by projecting it onto a smaller subspace, where the eigenvectors will form the axes. However, the eigenvectors only define the directions of the new axis, since they have all the same unit length 1, which can confirmed by the following two lines of code:

##### add picture 4-3
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A4/4-3.png)
##### add picture 4-4
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img/img_A4/4-4.png)

- step3: Get Explained Variance

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








