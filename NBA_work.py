# %% 
# importing packages for lab
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# %%
# Loading Data 
salary_data = pd.read_csv('2025_salaries.csv', header=1, encoding='latin-1')
# header=1 because we want to let pyhton know where the column starts
stats = pd.read_csv('nba_2025.txt', sep="," , encoding='latin-1')
# we want to seperate the data by commas

# %%
salary_data.head()
stats.head()

# %%
# Merging Data
# help(pd.merge)
merged_data = pd.merge(salary_data, stats, on='Player')

# %%
# dealing with duplicates
# putting a brackets around something requires us to call the data set and push the function onto it. We are using a function to index and create a new data frame
duplicates = merged_data[merged_data.duplicated(subset='Player', keep=False)]

# %%
# sklearn for steps
# 1. create an instance of the model. example: mymodel = KMeans(n_clusters=3)
# 2. Fit the model to the data. example: mymodel.fit(x), the x is the training data, assuming you have a clean data set
# ligustic regression - regression that can be done on classified fetaures not numerical
# 3. make predictions using the model: example: predictions = mymodel.predict(x), skipping because we don't need this, using it by visualizing it
# 4. evulate the model's performance: example: score = mymodel.score(x), on the lower left should be?? 
# we know when some data points are unusual because they weren't representing the patterns well
# include all the stats in the cluster to find good players are the players that are not the best or worst
# rebounds, points per game, points per minute, points average per game, subset the actual column to 
# correlation tracks the velocity of data in space, when salary goes up those variables go off 


# for kmeans you don't need to predict, you can just use the labels_ attribute 
# to get the cluster assignmnets for each data point after fitting the model.

# %%
# lambda functions are anonymous functions that can be defined by a single line of code
merged_data['Salary_in_thousands'] = merged_data['Salary'].apply(lambda x: x /1000)
# apply means to do the opperation 
# lambda function calls x and tells it x / 1000, you can include conditional and ... operaters 

# %%
help(KMeans)
# %%
