# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 18:11:05 2023

@author: malick_ndir
"""

import numpy as np
import pandas as pd

credit = pd.read_csv(r"tmdb_5000_credits.csv")

movie_id = credit.movie_id
movie_id = credit["movie_id"]

title = credit.title

newDF = pd.concat([movie_id, title], axis = 1)

newDF_2 = pd.concat([movie_id, title], axis = 0)

# Values of integer arrays
movie_id_array = movie_id.values
# Values of object arrays
title_id_array = title.values

newNewDF = pd.DataFrame(movie_id_array, columns = ["id"])