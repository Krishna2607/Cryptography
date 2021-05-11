# -*- cwe oding: utf-8 -*-
"""
Created on Fri Sep  4 15:57:37 2020

@author: LENOVO
"""

key_file=open("key_text_file.txt","r")
key=''
for i in key_file:
    key=key+i
key=key.upper()


def pos(key_matrix,alpha):
    x=y=0 
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j]==alpha:
                x=i 
                y=j 
    return x,y
   
    
   

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


plain_text=(input("Enter the plain text:"))
plain_text=plain_text.upper()
message=[]
for i in plain_text:
    message.append(i)


j=0    
for _ in range(len(plain_text)//2):
    if message[j]==message[j+1]:
        message.insert(j+1,'X')
    j=j+2

if len(message)%2==1:
    message.append("X")
  
k=0  
divide_message=[]
for m in range(1,(len(message)//2)+1):
    divide_message.append(message[k:k+2])
    k=k+2    
print(divide_message)

cipher_text=[]
for i in divide_message:
    a1,b1=pos(key_matrix,i[0])
    a2,b2=pos(key_matrix,i[1])
    if a1==a2:
            if b1==4:
                    b1=-1
            if b2==4:
                    b2=-1
            cipher_text.append(key_matrix[a1][b1+1])
            cipher_text.append(key_matrix[a1][b2+1])
    elif b1==b2:
            if a1==4:
                    a1=-1;
            if a2==4:
                    a2=-1;
            cipher_text.append(key_matrix[a1+1][b1])
            cipher_text.append(key_matrix[a2+1][b2])
    else:
           cipher_text.append(key_matrix[a1][b2])
           cipher_text.append(key_matrix[a2][b1])
str1=''.join(cipher_text)
print(str1)
 