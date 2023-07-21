# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 21:08:21 2023

@author: malick_ndir
"""

import pandas as pd
credit = pd.read_csv("tmdb_5000_credits.csv")

# These two are the same
movie_id = credit.movie_id
movie_id = credit["movie_id"]

title = credit.title

# concatinates columns into two separate rows
newDF = pd.concat([movie_id, title], axis = 1)

# concatinate movie_id and title columns into one
# Single row
neDF_2 = pd.concat([movie_id, title], axis=0)
