# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 19:32:03 2023

@author: malick_ndir
"""

import pandas as pd
movies = pd.read_csv("tmdb_5000_movies.csv")

# Turn a column from a dataframe into an index
movies = movies.set_index('id')

# moves index back to column that it came from
movies = movies.reset_index()

# Will allow original dataframe to be modified and
# not return a copy after reseting
movies.reset_index(inplace = True)

