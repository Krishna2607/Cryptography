# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 00:07:17 2020

@author: LENOVO
"""
import string
cipher_text=''
text=open("program2.txt","r")
for k in text:
    cipher_text+=k
Alphabet=string.ascii_uppercase

for i in range(len(Alphabet)):
    plain_text=' '
    for j in cipher_text:
        if j in Alphabet:
            temp=Alphabet.find(j)
            temp-=i
            if temp<0:
                temp+=len(Alphabet)
            plain_text+=Alphabet[temp]
        else:
            plain_text+=j
    print('Key %s: %s' % (i,plain_text))
    

    