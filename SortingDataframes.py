# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 20:47:58 2023

@author: malick_ndir
"""

import pandas as pd
movies = pd.read_csv("tmdb_5000_movies.csv")

# calculates profit
movies['profit'] = movies['revenue'] - movies['budget']

# re-orders value
movies.sort_values(by='profit', ascending=False)[['title','profit']].head(20)