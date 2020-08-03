# coding=utf-8

'''
Author:lchj
Date:
'''
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd

pd.options.display.max_columns=100

data=pd.read_csv('./CarPrice_Assignment.csv')
# print(data.describe())

train_x=data[['wheelbase','carlength','carwidth','carheight','curbweight','enginesize',\
              'boreratio','stroke','compressionratio','horsepower','peakrpm','citympg','highwaympg','price']]

min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv',index=False)

kmeans=KMeans(n_clusters=5)
kmeans.fit(train_x)
predict_y=kmeans.predict(train_x)

result=pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)

# print(result)
result.to_csv('car_cluster_result.csv',index=False)


