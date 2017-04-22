# Final Exam - Spring 2017

## Topic: The World Happiness Report Data Analysis

---

## General Dataset Description


| File Name        | Content           | 
| -------------- |:-------------| 
| 2015.csv        | happiness scores and ranking in 2015 | 
| 2016.csv     | happiness scores and ranking in 2016    |   
| Sentiment.csv      | Twitter Sentiment Analysis Dataset |   


- The happiness scores and rankings use data from the Gallup World Poll. The reports review the state of happiness in the world today and show how the new science of happiness explains personal and national variations in happiness. 

- They reflect a new worldwide demand for more attention to happiness as a criteria for government policy.

- The columns following the happiness score estimate the extent to which each of six factors: economic production, social support, life expectancy, freedom, absence of corruption, and generosity 

– contribute to making life evaluations higher in each country than they are in Dystopia, a hypothetical country that has values equal to the world’s lowest national averages for each of the six factors.

- They have no impact on the total score reported for each country, but they do explain why some countries rank higher than others.

---

## Overall Dataset Analysis

> **Overall Analysis**.

| Analysis No.        | Content           | 
| ------------- |:-------------:| 
|Analysis 1       | **Explore the Overall Happiness Rank and Distribution**  | 
| Analysis 2      | **scores change between the 2015 and 2016 reports **    | 
| Analysis 3  | **Explore scores change between the 2015 and 2016**  |
| Analysis 4      | ** Explorescores change between the 2015 and 2016 reports** |  
| Analysis 5     | **Explore**  | 

- What countries or regions rank the highest in overall happiness and each of the six factors contibuting to happiness? 
- How did country ranks or scores change between the 2015 and 2016 reports? 
- Did any country experience a significant increase or decrease in happiness?

> **Overall Libraries Used**.

| Library No.        | Library Name           | 
| -------------- |:-------------| 
| 1        | Numpy | 
| 2     | Panda   |   
| 3     | seaborn |  
| 4     | matplotlib |  
| 5     | seaborn |  

---

### Analysis 1

> 1. There are six numerical factors of happyniess. Calculate the total happiness score of each country and showed in a new column.

##### add picture 1-1
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img_A1/1-1.png)

> 2. Sort the data by the total score, and add a new column named Rank to show the happiness rank for each country.

##### add picture 1-2
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img_A1/1-2.png)
> ** examining univariate and bivariate distributions **

 
> 3. ** Visualizing the distribution of overall dataset.**  And analysis according to the plots. 

### add picture 1-5
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img_A1/1-5.png)
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

### add picture 1-3
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img_A1/1-3.png)
### add picture 1-4
![alt tag](https://github.com/wentingsu/Su_Wenting_spring2017/blob/master/Final/img_A1/1-4.png)

- It can also be useful to visualize a bivariate distribution of two variables. 

- after we get the sorted data by ** total score ** and get the rank for each country,now let's look at the variables between rank and total score distribution.

- we apply the ** jointplot() function ** in seaborn to creates a multi-panel figure that shows both the bivariate (or joint) relationship between two variables along with the univariate (or marginal) distribution of each on separate axes.
 
- The most familiar way to visualize a bivariate distribution is a ** scatterplot ** , where each observation is shown with point at the x and y values. This is analgous to a rug plot on two dimensions. You can draw a scatterplot with the matplotlib plt.scatter function, and it is also the default kind of plot shown by the jointplot() function:

- t is also posible to use the ** kernel density estimation ** procedure described above to visualize a bivariate distribution. In seaborn, this kind of plot is shown with a contour plot and is available as a style in jointplot():

##### Summarize:
- from both above plot we can get the point that according the asending rank, the score is mostly concentrate on the 4 to 6 scores, which is the same as the distribution plots.
 
 
- in the first analysis, we mainly observe the overall dataset between 2015 and 2016 years. in next analysis we will use the categorical plots to find out how the scores distributed in different region.

