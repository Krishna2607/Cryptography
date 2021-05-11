# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:42:11 2020

@author: LENOVO
"""

plain_text=''
text=open("program1.2.txt","r")
for i in text:
    plain_text+=i
key=4
cipher_text=''
for i in range(len(plain_text)):
    cipher_text+=chr((ord(plain_text[i])+key-97)%26+97)
print("The Cipher Text is: ",cipher_text)