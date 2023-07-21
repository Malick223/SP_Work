# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:18:09 2023

@author: malick_ndir
"""

import pandas as pd

# Loads movie data frame
movies = pd.read_csv("tmdb_5000_movies.csv")
seriesEx =movies.iloc[:,0]

# Shows five first lines of data file
head = movies.head()

# Shows five last lines of data files
tails = movies.tail()


describe = movies.describe()

#Shows all the columns in movie dataframe in a list
movies.columns
columns = movies.columns.tolist()

# Information about type of data in each variable of dataframe
dt = movies.dtypes

# Identifying nan(not a number) in our dataset
movies.isnull().sum()

# Remmoves some nan values
movies2 = movies.dropna()

# replaces nans with 0
moviesCleaned = movies.fillna(0)

moviesCleaned.isnull().sum()