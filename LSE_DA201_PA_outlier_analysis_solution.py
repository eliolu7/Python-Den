#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics Using Python

# ## Practical activity: Outlier analysis

# **This is the solution to the activity.**
# 
# Canopy is a new boutique streaming company that is looking to create an app that provides recommendations based on the last movie you watched. As a part of their process, they want to review the data and gather enough information before they start making suggestions and recommendations to their clients. 
# 
# This analysis uses the `movies.csv` and `ott.xlsx` data sets. Based on the available information, in this activity you will:
# 
# - perform an outlier analysis on the data to detect outliers or anomalies and find interesting relationships among the variables
# - understand what the data says by visualising it on a boxplot.

# ## 1. Import the libraries

# In[26]:


# Import necessary libraries.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


# ## Import Excel file

# In[2]:


# Load the Excel data using pd.read_excel.
ott = pd.read_excel('ott.xlsx')

# View the columns.
print(ott.columns)


# ## Import CSV file

# In[3]:


# Load the CSV data using pd.read_csv.
movies = pd.read_csv('movies.csv')

print(movies.columns)


# ## Validate the DataFrames

# In[9]:


# Data imported correctly?


print(movies.shape)
print(movies.dtypes)
movies.head()


# In[10]:


# Data imported correctly?
print(ott.dtypes)
print(ott.shape)
ott.head()


# ## Combine the two DataFrames

# In[6]:


# Merge the two DataFrames.
mov_ott = pd.merge(movies, ott, how='left', on = 'ID')

# View the DataFrame.
print(mov_ott.shape)
mov_ott.head()


# ## 2. Create a boxplot

# In[12]:


# Create boxplot with two variables (Age and IMDb).
sns.boxplot(x='Age', y='IMDb', data=mov_ott)


# In[25]:


# Filter the data for movies released from 2010 to 2020
mov_ott_2010 = mov_ott[mov_ott['Year'] >= 2010]

# Calculate the percentage of movies viewed each year
total_movies = len(mov_ott_2010['Year'])
year_counts = mov_ott_2010['Year'].value_counts()
year_percentages = year_counts / total_movies * 100

# Create a bar plot to display the percentage of movies viewed each year
ax = sns.barplot(x=year_percentages.index, y=year_percentages.values)
ax.set(ylabel='Percent')
ax.yaxis.set_major_formatter(mtick.PercentFormatter())

for p in ax.patches:
    percentage = '{:.1f}%'.format(p.get_height())
    x = p.get_x() + p.get_width() / 2
    y = p.get_y() + p.get_height()
    ax.annotate(percentage, (x, y), ha='center')

plt.xticks(rotation=90)
plt.show()

# Create a histogram with a KDE plot to check for normality in the IMDb ratings
plt.figure(figsize=(10, 6))
bin_edges = [x for x in range(1, 11)]  # Define bin edges for IMDb ratings from 1 to 10
hist, bins, _ = plt.hist(mov_ott['IMDb'], bins=bin_edges, density=True, alpha=0.7, color='blue')
sns.kdeplot(mov_ott['IMDb'], color='red', label='KDE')
plt.xlabel('IMDb Ratings')
plt.ylabel('Percent')
plt.title('Distribution of IMDb Ratings with KDE')
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))  # Correct the y-axis tick labels to show percentages
plt.legend()
plt.show()


# In[ ]:




