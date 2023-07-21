# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 10:11:02 2023

@author: malick_ndir
"""

import pandas as pd
credit = pd.read_csv(r'tmdb_5000_credits.csv')
movies = pd.read_csv("tmdb_5000_movies.csv")

# Merges both credit id and movie_id by using left_on
# and right_on because name of columns aren't the same
movies_with_credit = pd.merge(movies, credit, how='inner',
                              left_on='id', right_on='movie_id')

# Makes id and movie_id the index
movies.setindex('id', inplace=True)
credit.set_index('movie_id', inplace=True)

movies_joined_credits = movies.join(credit, rsuffix='_c')

# Resets columns back to normal
movies.reset_index(inplace=True)
credit.reset_index(inplace=True)