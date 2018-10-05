import pandas as pd
import numpy as np
import re
import csv

dataset=pd.read_csv("flipkart.csv")
dataset = dataset.drop('assure_alt',axis=1)
dataset = dataset.dropna()
df = pd.read_csv("listdes1.csv")
description = list(df.Description)
# print(description)
new_list = dataset.index.tolist()

# index_list = [ int(x)+1 for x in new_list]
# print(index_list)
# csv.register_dialect('myDialect',
# quoting=csv.QUOTE_ALL,
# skipinitialspace=True)

# with open('flip1.csv', 'w') as f:
#     writer = csv.writer(f)
#     for row in dataset:
#         writer.writerow(row)

# f.close()

price=[float(i[1:]) for i in list(dataset.Price)]

image_url = list(dataset.Image)
title=list( i.upper() for i in dataset.Title)
reviews=list(dataset.Reviews)
reviews=[int(i[1:len(i)-1].replace(",",'')) for i in reviews]

rating=[float(re.sub('[^1-9.]','',i)) for i in dataset.Rating]

author = [ i.split(', ')[2] for i in dataset.Author]
url = list(dataset.Title_link)