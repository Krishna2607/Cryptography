# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:58:17 2020

@author: LENOVO
"""
cipher_text=''
text=open("program5.txt","r")
for i in text:
    cipher_text+=i
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
mapped=['A','N','D','R','E','W','I','C','K','S','O','H','T','B','F','G','J','L','M','P','Q','U','V','X','Y','Z']
plain_text=''
for i in cipher_text:
    plain_text += mapped[alphabet.index(i)]
print(plain_text)