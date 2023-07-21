# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 18:03:54 2023

@author: malick_ndir
"""

import pandas as pd

movies = pd.read_csv('tmdb_5000_movies.csv')

# to_csv will write the entire content of a dataframe to a csv file
movies.to_csv('movies.csv', na_rep='', index=False, header=False)

# to_pkl will create a pickle file
# which is a compressed format 
# that makes it easy to store large data files
movies.topkl('movies.pkl')