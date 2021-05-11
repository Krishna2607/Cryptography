# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:24:53 2020

@author: LENOVO
"""
import string
key=''
text=open("program10.txt","r")
for i in text:
    key=key+i
plaintext=input("Enter the plain text:")
alphas=string.ascii_lowercase
cipertext=''
en=plaintext
while len(key)!=len(en):
    diff=len(en)-len(key)
    key=key+key[:diff]
key=list(key)
plaintext=list(plaintext)
lenght=len(plaintext)
for i in range(lenght):
    cipertext+=alphas[(alphas.index(plaintext[i])+alphas.index(key[i]))%26]
print(cipertext.upper())