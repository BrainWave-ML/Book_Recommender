import pandas as pd
import numpy as np
import re


dataset=pd.read_csv("flipkart.csv")
dataset = dataset.drop('assure_alt',axis=1)
dataset = dataset.dropna()

price=[float(i[1:]) for i in list(dataset.Price)]

image_url = list(dataset.Image)
title=list( i.upper() for i in dataset.Title)
reviews=list(dataset.Reviews)
reviews=[int(i[1:len(i)-1].replace(",",'')) for i in reviews]

rating=[float(re.sub('[^1-9.]','',i)) for i in dataset.Rating]

author = [ i.split(', ')[2] for i in dataset.Author]
url = list(dataset.Title_link)