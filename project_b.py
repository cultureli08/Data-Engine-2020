# coding=utf-8

'''
Author:lchj
Date:
'''
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

import pandas as pd
pd.options.display.max_columns=100

data=pd.read_csv('./订单表.csv',encoding='gbk')

print(data.shape)

orders_series=data.set_index('客户ID')['产品名称']

print(orders_series)

transactions=[]
temp_index=0
for i,v in orders_series.items():
    if i != temp_index:
        temp_set=set()
        temp_index=i
        temp_set.add(v)
        transactions.append(temp_set)
    else:
        temp_set.add(v)

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
hot_encoded_df = data.groupby(['客户ID', '产品名称'])['产品名称'].count().unstack().reset_index().fillna(0).set_index(
    '客户ID')
hot_encoded_df = hot_encoded_df.applymap(encode_units)
frequent_itemsets = apriori(hot_encoded_df, min_support=0.02, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.5)
print("频繁项集：", frequent_itemsets)
print("关联规则：", rules[(rules['lift'] >= 1) & (rules['confidence'] >= 0.5)])
# print(rules['confidence'])


