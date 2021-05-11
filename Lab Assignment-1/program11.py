# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:58:00 2020

@author: LENOVO
"""

def split_len(seq, length):
   return [seq[i:i + length] for i in range(0, len(seq), length)]
def encode(key, plaintext):
    order = {int(val): num for num, val in enumerate(key)}
    ciphertext = ''
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue
    return ciphertext
p = ""
text = open("program11.txt","r")
for i in text:
    p += i
k = input("enter the key: ").replace(' ','')
print(encode(k, p))
