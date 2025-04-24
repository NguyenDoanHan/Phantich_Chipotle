# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 15:33:53 2025

@author: Administrator
"""
import subprocess

commands = [
    'git init',
    'git add .',
    'git commit -m "First commit from Spyder"',
    'git branch -M main',
    'git remote add origin https://github.com/NguyenDoanHan/Nh-h-ng-Chipotle',
    'git push -u origin main'
]

for cmd in commands:
    subprocess.run(cmd, shell=True)


import pandas as pd
import collections
import matplotlib.pyplot as plt 

df_chipotle = pd.read_csv("chipotle.tsv",sep='\t')
print(df_chipotle.head(10))

x = df_chipotle['item_name']
letter_counts = collections.Counter(x)
print(x.head())
df = pd.DataFrame.from_dict(letter_counts, orient="index")
df.columns = ['so luong']
print(df.head())
df_5 = df.sort_values(by = 'so luong', ascending = False)[0:5]
print(df_5)
plt.bar(df_5.index.values,df_5['so luong'], color = 'b')
plt.title("5 mon an dc goi nhieu nhat!")
plt.xlabel("Ten mon an")
plt.ylabel("so luong")
plt.xticks(rotation=60)
plt.grid(True)
plt.show()

df_chipotle.item_price = [float(value[1:]) for value in df_chipotle.item_price]
print(df_chipotle.head())

orders = df_chipotle.groupby('order_id').sum()
print(orders.head())

plt.scatter(x=orders['item_price'], y=orders['quantity'], s=50, color='r')
plt.xlabel("bill Item price")
plt.ylabel("Items ordered")
plt.title("Number of items orders and bill total")
plt.grid(True)
plt.show()