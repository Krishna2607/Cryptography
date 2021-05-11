# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:18:49 2020

@author: LENOVO
"""

input_message=''
text=open("program1.txt","r")
for i in text:
    input_message+=i
print("Words in the given input file is/are:",str(input_message.split()))
x=input_message.replace(' ','')
print('The charcter count of the input is:',len(x))
for i in x:
    print("The ascii value of "+i+" is: ",ord(i)) 