# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:12:45 2020

@author: LENOVO
"""

import sys
import numpy as np

text = open("program9.txt","r")
msg = input("Enter message: ").upper()
msg = msg.replace(" ", "")
len_chk = 0
if len(msg) % 2 != 0:
    msg += "0"
    len_chk = 1
row = 2
col = int(len(msg) / 2)
msg2d = np.zeros((row, col), dtype=int)

itr1 = 0
itr2 = 0
for i in range(len(msg)):
    if i % 2 == 0:
        msg2d[0][itr1] = int(ord(msg[i]) - 65)
        itr1 += 1
    else:
        msg2d[1][itr2] = int(ord(msg[i]) - 65)
        itr2 += 1

key = " "
for i in text:
    key += i
key = key.replace(" ", "").upper()
key2d = np.zeros((2, 2), dtype=int)
itr3 = 0
for i in range(2):
    for j in range(2):
        key2d[i][j] = ord(key[itr3]) - 65
        itr3 += 1

deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
deter = deter % 26
mul_inv = -1
for i in range(26):
    temp_inv = deter * i
    if temp_inv % 26 == 1:
        mul_inv = i
        break
    else:
        continue
key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0]
key2d[0][1] *= -1
key2d[1][0] *= -1
key2d[0][1] = key2d[0][1] % 26
key2d[1][0] = key2d[1][0] % 26

for i in range(2):
    for j in range(2):
        key2d[i][j] *= mul_inv 

for i in range(2):
    for j in range(2):
        key2d[i][j] = key2d[i][j] % 26

decryp_text = ""
itr_count = int(len(msg) / 2)
if len_chk == 0:
    for i in range(itr_count):
        temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
        decryp_text += chr((temp1 % 26) + 65)
        temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
        decryp_text += chr((temp2 % 26) + 65)
else:
    for i in range(itr_count - 1):
        temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
        decryp_text += chr((temp1 % 26) + 65)
        temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
        decryp_text += chr((temp2 % 26) + 65)

print("Decrypted Text: {}".format(decryp_text))