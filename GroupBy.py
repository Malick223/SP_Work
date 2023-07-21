# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 17:46:23 2023

@author: malick_ndir
"""

import pandas as pd

movies = pd.read_csv('tmdb_5000_movies.csv')

# Groups by orginal_languae/ .mean() gets average
# .sum() gets average

avg_per_country = movies.groupby('original_language').mean()