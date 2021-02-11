#!/bin/python3
from math import e, gcd
from tkinter import *
import tkinter.messagebox as pop_up





def isPrime(n):
    
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if (n%i) == 0:
            return False
        i+=1
    return True

def Mobius(n):
    
    if n == 1:
        return 1
    
    prime = 0
    for i in range(1,n+1):
        if( (n%i == 0) & isPrime(i)):

            if (n % (i*i) == 0):
                return 0
            else:
                prime+=1

    if (prime%2):
        return -1
    else:
        return 1

def Eu_tot(n):
    ans = 1
    for i in range(2,n):
        if(gcd(i,n) == 1):
            ans+=1
    return ans


def PrintMob():
    global text
    try:
        val = int(text.get())
        pop_up.showinfo("Mobius Value", "Mobius of "+str(val)+" is: "+str(Mobius(int(val))))
    except ValueError:
        pop_up.showerror("Error","Non integer Value entered!!")

def PrintEu_Tot():
    global text
    try:
        val = int(text.get())
        pop_up.showinfo("Euler's Tuotient", "Totient of "+str(val)+" is: "+str(Eu_tot(val)))

    except ValueError :
        pop_up.showerror("Error","Non integer Value entered!!")




if __name__ == "__main__":

    
    #GUI Part
    window = Tk()
    window.geometry("480x360")
    window.resizable()
    window.title("Crypto Assignment 1: Mobius and Euler's Totient")
    text = StringVar()



    lbl = Label(window,text="This is a program to calculate the output of the Mobius and the Euler's Totient function for any given value.",wraplength=500)
    lbl.grid(column=0,row=0)
    lbl2 = Label(window,text="Enter the n value: ")
    lbl2.grid(column=0,row = 1)


    textbox = Entry(window,width=20,textvariable=text)
    textbox.grid(column = 0,row = 2,pady=30)


    btn1 = Button(window,text = "Mobius",command=PrintMob)
    btn1.grid(column=0,row = 3,pady=30)

    btn2 = Button(window,text = "Euler's Totient",command=PrintEu_Tot)
    btn2.grid(column=0,row = 4,pady=30)

    window.mainloop()
    # n = int(input("Enter the number: "))
    # print("The Mobius is:",Mobius(n))
    # print("The Euler's Totient is:",Eu_tot(n))
