from tkinter import *

root = Tk()
root.title("calcultor")
root.geometry("200x200")
root.resizable(height = False, width =  False)

def clear_(event=None):
    operator.delete(0, "end")
    operator.insert(0, "..")
    result.delete(0, "end")
    result.insert(0, "0")
    num_1.delete(0, "end")
    num_1.insert(0, "0")
    num_2.delete(0, "end")
    num_2.insert(0, "0")

def get_sum(event=None):
    num1 = float(num_1.get())
    num2 = float(num_2.get())
    sum = num1 + num2

    operator.delete(0, "end")
    operator.insert(0, "+")

    result.delete(0, "end")
    result.insert(0, sum)

def get_product(event=None):
    num1 = float(num_1.get())
    num2 = float(num_2.get())
    product = num1 * num2

    operator.delete(0, "end")
    operator.insert(0, "*")

    result.delete(0, "end")
    result.insert(0, product)

def get_divide(event=None):
    num1 = float(num_1.get())
    num2 = float(num_2.get())
    if num2 == 0.0:
        result.delete(0, "end")
        result.insert(0, "division by zero")

    divide = num1 / num2

    operator.delete(0, "end")
    operator.insert(0, "/")

    result.delete(0, "end")
    result.insert(0, divide)

def get_minus(event=None):
    num1 = float(num_1.get())
    num2 = float(num_2.get())
    minus = num1 - num2

    operator.delete(0, "end")
    operator.insert(0, "-")

    result.delete(0, "end")
    result.insert(0, minus)

def get_percent(event=None):
    num1 = float(num_1.get())
    num2 = float(num_2.get())
    percent = (num1 * num2)/100

    operator.delete(0, "end")
    operator.insert(0, "%")

    result.delete(0, "end")
    result.insert(0, percent)

frame = Frame(root)

num_1 = Entry(frame, width = 12)
num_1.grid(row = 1, columnspan = 2,sticky = W,pady = 3)
operator = Entry(frame, width = 3 )
operator.grid(row = 3,columnspan = 2,sticky = W,pady = 3)
num_2 = Entry(frame, width = 12)
num_2.grid(row = 2,columnspan = 2, sticky = W,pady = 3)
result = Entry(frame, width = 18)
result.grid(row = 4,columnspan = 3, sticky = W,pady = 5)

clear = Button(frame, text = 'C',fg="red", height = 2, width = 6, command = clear_)
clear.grid(row = 6,column =0, padx = 2, pady = 2)

minus = Button(frame, text = '-', height = 2, width = 6, command = get_minus)
minus.grid(row = 6, column = 1, padx=2 )
multiply = Button(frame, text = '*', height = 2, width = 6, command = get_product)
multiply.grid(row = 6, column = 2, padx=2)
divide = Button(frame, text = '/', height = 2, width = 6, command = get_divide)
divide.grid(row = 7 , column = 0, padx=2 )
plus = Button(frame, text = '+', height = 2, width = 6, command = get_sum)
plus.grid(row = 7, column = 1, padx=2 )
percent = Button(frame, text = '%', height = 2, width = 6, command = get_percent)
percent.grid(row = 7, column = 2,pady=2 )

frame.pack()

root.mainloop()
