# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 14:52:25 2023

@author: malick_ndir
"""


import pandas as pd
movies = pd.read_csv("tmdb_5000_movies.csv")

# define function you want to apply
def str_lower(s):
    return s.lower()

# apply function
movies['title'] = movies['title'].apply(str_lower)

movies['title'] = movies['title'].apply(lambda x: x.lower())

# A JSON is a way to structure text so you can store complex date
# tables in one line or field
# JSON: Java Script Opject Notation

# converting JSON to a pipe delimainated list

def json_extract(json, field):
    j = pd.read_json(json)
    if field in j.columns:
        genre = j[field]
        genre = genre.tolist()
        ret = '|'.join(genre)
    else:
        return None
    
movies['genres'] = movies['genres'].apply(json_extract, args = ('name',))

# Finding length of longest title in dataframe

movies['title_len'] = movies['title'].apply(len)

m = movies.sort_values(by='title_len', ascending=False)
m[['title_len']].head(1)

# What is the runtime of the movie with the highest
# vote average that contains the word you in the title

def contains_you(s):
    words = s.lower().split()
    if 'you' in words:
        return True
    else:
        return False
    
    movies['contains_you'] = movies['title'].apply(contains_you)
    
    m = movies[movies['contains_you']]
    m = m.sort_values(by='vote_average', ascending = False)
    
    m[['runtime']].head(1)