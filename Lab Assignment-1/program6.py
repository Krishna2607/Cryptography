# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:05:40 2020

@author: LENOVO
"""

key_file=open("key_text_file.txt","r")
key=''
for i in key_file:
    key=key+i
key=key.upper()
dummy_matrix=[]
for i in key:
    if i not in dummy_matrix:
        dummy_matrix.append(i)
            
for i in range(65,91):
    if chr(i) not in dummy_matrix and i!=74:
            dummy_matrix.append(chr(i))
    else:
            pass
    
key_matrix=[]
for i in range(5):
    key_matrix.append('')
key_matrix[0]=dummy_matrix[0:5]
key_matrix[1]=dummy_matrix[5:10]
key_matrix[2]=dummy_matrix[10:15]
key_matrix[3]=dummy_matrix[15:20]
key_matrix[4]=dummy_matrix[20:25]

print(key_matrix)
