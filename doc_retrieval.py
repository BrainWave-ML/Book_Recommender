#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:51:57 2018

@author: rushikesh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loading the dataset

df = pd.read_csv('listdes.csv')
df = df.replace(np.nan ,'yep', regex=True)



# book = df.iloc[32:33,1:]




X_book = df.iloc[:,1:]



#Tf-idf
from sklearn.feature_extraction.text import TfidfVectorizer

vectb = TfidfVectorizer().fit(X_book['Description'])


# book_vectorized = vectb.transform(book['Description'])


X_book_vectorized = vectb.transform(X_book['Description'])


#Building a knn model

from sklearn.neighbors import NearestNeighbors

#Since the tf-idf already normalizes the vector we can use euclidean distance also
classifier = NearestNeighbors(n_neighbors=5)

classifier.fit(X_book_vectorized)

# ans_books = classifier.kneighbors(book_vectorized[0], n_neighbors=5)

# book_ind = ans_books[1]


#Printing the closest five
# for i in book_ind:
#     print(X_book.iloc[i,0])





