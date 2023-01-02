# Tkinter Calculator

from tkinter import *

page = Tk()
page.geometry("500x500")
page.title("Calculator")


def add():
    add_Label.config(text='Addition = '+str(int(E1.get())+int(E2.get())))

def sub():
    add_Label.config(text='Subtraction = '+str(int(E1.get())-int(E2.get())))
def mul():
    add_Label.config(text='Multiplication = '+str(int(E1.get())*int(E2.get())))
def div():
    add_Label.config(text='Division = '+str(int(E1.get())/int(E2.get())))
    
No1 = Label(page, text = "Enter the first number : ").place(x = 15, y = 15)
E1 = Entry(page, bd = 1 , relief = "solid")
E1.place(x = 170, y = 15) 

No2 = Label(page , text = "Enter the second number : ").place(x = 15, y = 45)
E2 = Entry(page, bd = 1, relief = "solid")
E2.place(x = 170 , y = 45)

add_Button = Button(page , text = "ADD" , bd = 1 , relief = "solid" , command = add)
add_Button.place(x =90 , y = 90)

sub_Button = Button(page , text = "SUB" , bd = 1 , relief = "solid" ,command = sub)
sub_Button .place(x=140,y =90)

mul_Button = Button(page , text = "MUL" , bd = 1 , relief = "solid" ,command = mul)
mul_Button.place(x = 190 , y =90)

div_Button = Button(page, text = "DIV" , bd = 1 , relief = "solid" , command = div)
div_Button.place(x = 240 , y = 90)

add_Label = Label(page,)
add_Label.place(x = 90 , y = 140)
