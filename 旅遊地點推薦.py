# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 21:49:52 2018

@author: user
"""

#%matplotlib inline
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
import gc
import random as rd
from ipywidgets import interact
import re
gc.enable()

#記憶體配置
loc_to_num=[]#地址to對應的數字
user_loc={}#user去過的地方&次數
Table_list=loc_to_num
Data_dict=user_loc

#body(短的list) 
#tail(常的list)
def tail_connect(body,tail): 
    #身體長度
    body_length=len(body)
    #尾巴歸零
    tail_zero = [0] * len(tail[body_length:])
    #尾巴接起來
    body+=tail_zero
    return 

def initial_and_plus(key,value,data_dict=Data_dict,table_list=Table_list):
    k=table_list.index(value)#找到地址對應的數字
    data_dict[key][k]+=1#賦值或是增加
    #print("+1->",user_loc[user])
    return

def update(key,value,data_dict=Data_dict,table_list=Table_list):
    if key not in data_dict:#新人
        #新增新人     
        #print("新人:",key)
        data_dict[key]=[]
        if value not in table_list:#新地
            table_list.append(value)
            #print("ltn",table_list)
        #這個人沒去過，不判斷
        tail_connect(body=data_dict[key],tail=table_list)#1
        initial_and_plus(key,value)    
    
    else:#舊人
        if value not in table_list:#新地
            table_list.append(value)
            #print("ltn",table_list)
            #必然沒去過，不判斷
            tail_connect(data_dict[key],table_list)#2          
            initial_and_plus(key,value)
            
        else:#舊地
            #判斷            
            if table_list.index(value)+1>len(data_dict[key]) :#沒去過
                print("舊人舊地沒去過")#無法重現
                tail_connect(data_dict[key],table_list)#3            
                initial_and_plus(key,value)
            else:#去過
                initial_and_plus(key,value) 
#假裝是對的    
    return data_dict,table_list

#Data_arrange

#首次讀進資料
NewYork_Data_list=list(pd.read_table("NewYork_Data.txt", sep=" ",header=None).values)
               
def insert_data():
    s=NewYork_Data_list.pop()
    parts= re.split(r'[;,:\s]\s*',s[0])
    #print(parts)
    for i in range(2,len(parts),2):
        sending=([parts[0],parts[1],parts[i],parts[i+1]])
        yield sending
    yield 
    
              
while NewYork_Data_list !=[]:            
    generator=insert_data() 
    #print("開始")
    while True:
        received=next(generator)
        if received == None:
            break
        #print(received)
        #正在處理的這一筆資料
        dealing=received
        #各項分別代表的意義
        human=dealing[0]
        #workingday=dealing[1]
        address=dealing[2]
        #time=dealing[3]
        update(human,address)
        #print("繼續")
    #print("結束")

print(user_loc)