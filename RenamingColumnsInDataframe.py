# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 19:40:49 2023

@author: malick_ndir
"""

import pandas as pd
movies = pd.read_csv("tmdb_5000_movies.csv")

# create a dictionary that replaces names
change = {'revenue' : 'revenue_in_milions', 'budget' : 'budget_in_millions'}

movies.rename(index=str, columns=change, inplace=True)