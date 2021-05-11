# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:39:28 2020

@author: LENOVO
"""
import string
plaintext=''
text = open("program4.txt","r")
for i in text:
    plaintext+=i
uniq_plaintext=list(set(plaintext))
alphas=string.ascii_lowercase
ciphertext=''
for i in plaintext:
    ciphertext += alphas[(alphas.index(i)+uniq_plaintext.index(i))%26]
print(ciphertext)
