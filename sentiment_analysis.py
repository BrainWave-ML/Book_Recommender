"""
Created on Mon Jun 25 21:20:24 2018

@author: rushikesh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('chennai_reviews.csv')

#Removing unnecessary features
dataset = dataset.drop(['Unnamed: 8', 'Unnamed: 6', 'Unnamed: 7','Unnamed: 5'], axis=1)

#Removing sentiments having text that is len more than or equal to 2
df = dataset[[(len(str(x))<2) for x in dataset['Sentiment']]]


X = df.iloc[:,[2]]
y = df.iloc[:, 3]

#Buildign a word count vector 
from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer(min_df = 5, ngram_range = (1,3)).fit(X['Review_Text'])
X_train_vectorized = vect.transform(X['Review_Text'])
len(vect.get_feature_names())


#Applying Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=500)
classifier.fit(X_train_vectorized, y)


text = "delivery wasn't so good"
text = [text]
predic = classifier.predict(vect.transform(text))
print(predic)
