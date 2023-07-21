# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 18:46:38 2023

@author: malick_ndir
"""

import pandas as pd
import seaborn as sns

# Read in data
films = pd.read_csv("Films.csv")

# Looking for missing data

for col in films.columns:
    np.mean(df[col].isnull())