# coding=utf-8

'''
Author:lchj
Date:
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_page_content(request_url):

    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

    html=requests.get(request_url,headers=headers,timeout=10)
    content=html.text
    soup=BeautifulSoup(content,'html.parser',from_encoding='utf-8')

    return soup


def analysis(soup):
    temp=soup.find('div',class_='search-result-list')
    # print(temp)
    df=pd.DataFrame(columns=['name','lowest price','highest price','image source'])

    item_list=temp.find_all('div',class_='search-result-list-item')
    # print(item_list)
    # print(len(item_list))
    tmp = {}
    for item in item_list:
        # print(item)
        a=item.find('a')
        name,price,image=a.find('p',class_='cx-name text-hover').text,a.find('p',class_='cx-price').text,a.find('img').attrs.get('src')
        if '-' in price:
            l_price,h_price=price.split('-')
        else:
            l_price,h_price=price
        tmp['name'],tmp['lowest price'],tmp['highest price'],tmp['image source']=name,l_price,h_price,image
        # print(tmp)
        df=df.append(tmp,ignore_index=True)
    return df


url='http://car.bitauto.com/xuanchegongju/?l=8&mid=8'
soup=get_page_content(url)
df=analysis(soup)
print(df)

df.to_csv('./cars1.csv',index=None)




