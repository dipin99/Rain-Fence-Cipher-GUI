# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 12:00:13 2020

@author: HP
"""
from tkinter import *
from math import *
x=[]

    

def encrypt(p):
    plain=[char for char in p] 
    a=[]
    b=[]
    for i in range(0,len(plain)):
        if(i%2==0):
            a.append(plain[i])
        else:
            b.append(plain[i])
    
    x=a+b
    str = "" 
    c=str.join(x)
    return c

def decrypt(p):
    cipher=[char for char in p] 
    x=ceil(len(cipher)/2)
    a=[]
    b=[]
    p=int(len(cipher)/2)
    for i in range(0,x):
        a.append(cipher[i])
    for i in range(x,len(cipher)):
        b.append(cipher[i])
    c=[]
    for i in range(0,p):
       c.append(a[i])
       c.append(b[i])
    if(len(a)>len(b)):
        x=len(a)-len(b)
        for i in range(p,p+x):
            c.append(a[i])
    if(len(b)>len(a)):
        x=len(b)-len(a)
        for i in range(p,p+x):
            c.append(b[i])
    str=""
    return str.join(c)    
    




root = Tk()
frame = LabelFrame(root,text="Rain Fence Cipher",padx=100,pady=100)
frame.pack(padx=10,pady=10)
e=Entry(frame,width=50)


e.pack()

def Click1():
    c=encrypt(e.get())
    myLabel=Label(frame,text="Encrypted Text: "+c)
    myLabel.pack()

def Click2():
    c=decrypt(e.get())
    myLabel=Label(frame,text="Decrypted Text: "+c)
    myLabel.pack()

myButton = Button(frame, text="Encrypt", command=Click1)
myButton.pack()
myButton1 = Button(frame, text="Decrypt", command=Click2)
myButton1.pack()

root.mainloop()