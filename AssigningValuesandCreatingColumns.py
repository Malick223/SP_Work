# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 13:46:44 2023

@author: malick_ndir
"""

import pandas as pd
movies = pd.read_csv("tmdb_5000_movies.csv")

# dividing the revenue and budget series by one million
# so it can be easier to read
movies['revenue'] = movies['revenue']/1000000
movies['budget'] = movies['budget']/1000000

# Setting a series to a single value
# here we get the budget series and identify
# each value under budget that is less than or
# equal to 0 and set it to None
movies['budget'][movies['budget'] <= 0] = None

# Adding a profit column by subtracting
# the values in the revenue from the budget

movies['profit'] = movies['revenue'] - movies['budget']

# What is the budget(in millions) per minute of runtime for avatar
movies['budget_per_minute'] = movies['budget']/(1000000*movies['runtime'])
