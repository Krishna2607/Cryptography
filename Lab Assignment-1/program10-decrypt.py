# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:24:19 2020

@author: LENOVO
"""
import string
key=''
text=open("program10.txt","r")
for i in text:
    key+=i
alpha=string.ascii_lowercase
cipher_text=input("Enter the cipher_text:")
cipher_text=cipher_text.lower()
plain_text=''
en=cipher_text
while len(key)!=len(en): 
    diff=len(en)-len(key)
    key=key+key[:diff]
key=list(key)
cipher_text=list(cipher_text)
length=len(cipher_text)
for i in range(length):
    plain_text+=alpha[(alpha.index(cipher_text[i])-alpha.index(key[i]))%26]
print(plain_text)
