import tkinter as tk
import math  
window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)
entryfont = (100)




#images

img0 = tk.PhotoImage(file = "images/0.png")
img1 = tk.PhotoImage(file = "images/1.png")
img2 = tk.PhotoImage(file = "images/2.png")
img3 = tk.PhotoImage(file = "images/3.png")
img4 = tk.PhotoImage(file = "images/4.png")
img5 = tk.PhotoImage(file = "images/5.png")
img6 = tk.PhotoImage(file = "images/6.png")
img7 = tk.PhotoImage(file = "images/7.png")
img8 = tk.PhotoImage(file = "images/8.png")
img9 = tk.PhotoImage(file = "images/9.png")

img_div = tk.PhotoImage(file = "images/÷.png")
img_mult = tk.PhotoImage(file = "images/x.png")
img_add = tk.PhotoImage(file = "images/+.png")
img_sub = tk.PhotoImage(file = "images/-.png")
img_equals = tk.PhotoImage(file = "images/=.png")
img_ce = tk.PhotoImage(file = "images/ce.png")
img_c = tk.PhotoImage(file = "images/c.png")
img_dec = tk.PhotoImage(file = "images/..png")
img_del = tk.PhotoImage(file = "images/del.png")


#functions for every button
def button_clicked(x):
    current = entrymain.get()
    entrymain.delete(0, tk.END)
    entrymain.insert(tk.END, str(current) + str(x))
    

def add_clicked():
    global number1 
    global operator
    operator = "addition"
    number1 = float(entrymain.get())
    entrymain.delete(0, tk.END)

def sub_clicked():
    global number1 
    global operator
    operator = "subtraction"
    number1 = float(entrymain.get())
    entrymain.delete(0, tk.END)

def mult_clicked():
    global number1 
    global operator
    operator = "multiplacation"
    number1 = float(entrymain.get())
    entrymain.delete(0, tk.END)

def div_clicked():
    global number1 
    global operator
    operator = "division"
    number1 = float(entrymain.get())
    entrymain.delete(0, tk.END)

def delete_clicked():
    entrymain.delete(len(entrymain.get())-1,tk.END)

def ce_clicked():
    number1 = 0
    number2 = 0
    operator = ""
    entrymain.delete(0, tk.END)

def clear_clicked():
    entrymain.delete(0, tk.END)

def equals_clicked():
    number2 = float(entrymain.get())
    entrymain.delete(0, tk.END)

    if operator == "addition":
        entrymain.delete(0, tk.END)
        entrymain.insert(0, number1 + number2)
    elif operator == "subtraction":
        entrymain.delete(0, tk.END)
        entrymain.insert(0, number1 - number2)
    elif operator == "multiplacation":
        entrymain.delete(0, tk.END)
        entrymain.insert(0, number1 * number2)
    elif operator == "division":
        entrymain.delete(0, tk.END)
        entrymain.insert(0, number1 / number2)
    else:
        pass

#frames for the GUI
frm1 = tk.Frame(master = window,
                    height = 490,
                    width = 290,
                    bg = '#68A6B6',
                    borderwidth = 4
                    )
frm2 = tk.Frame (master = frm1,
                    height = 480,
                    width = 280,
                    bg = '#68A6B6',
                    borderwidth = 2
                    )
frm3 = tk.Frame(master = frm2,
                    height = 460,
                    width = 260,
                    bg = '#F9F1DC',
                    borderwidth = 1
                    )

#buttons for the GUI
entrymain = tk.Entry(master = frm3, relief = tk.FLAT, width = 18, bg = '#F9F1DC', font = entryfont)

btn_0 = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img0, width = 40, height = 37, borderwidth = 0, command = lambda:button_clicked("0"))
btn_1 = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img1, width = 40, height = 37, borderwidth = 0, command = lambda:button_clicked("1"))
btn_2 = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img2, width = 40, height = 37, borderwidth = 0, command = lambda:button_clicked("2"))
btn_3 = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img3, width = 40, height = 37, borderwidth = 0, command = lambda:button_clicked("3"))
btn_4 = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img4, width = 40, height = 37, borderwidth = 0, command = lambda:button_clicked("4"))
btn_5 = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img5, width = 40, height = 37, borderwidth = 0, command = lambda:button_clicked("5"))
btn_6 = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img6, width = 40, height = 37, borderwidth = 0, command = lambda:button_clicked("6"))
btn_7 = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img7, width = 40, height = 37, borderwidth = 0, command = lambda:button_clicked("7"))
btn_8 = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img8, width = 40, height = 37, borderwidth = 0, command = lambda:button_clicked("8"))
btn_9 = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img9, width = 40, height = 37, borderwidth = 0, command = lambda:button_clicked("9"))


btn_add = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img_add, width = 40, height = 37, borderwidth = 0, command = lambda:add_clicked())


btn_sub = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img_sub, width = 40, height = 37, borderwidth = 0, command = lambda:sub_clicked())


btn_mult = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img_mult, width = 40, height = 37, borderwidth = 0, command = lambda:mult_clicked())


btn_div = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img_div, width = 40, height = 37, borderwidth = 0, command = lambda:div_clicked())


btn_ce = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img_ce, width = 40, height = 37, borderwidth = 0, command = lambda:ce_clicked())


btn_clear = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img_c, width = 40, height = 37, borderwidth = 0, command = lambda:clear_clicked())


btn_equals = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img_equals, width = 40, height = 37, borderwidth = 0, command = lambda:equals_clicked())


btn_delete = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img_del, width = 40, height = 37, borderwidth = 0, command = lambda:delete_clicked())


btn_decimal = tk.Button(master = frm3, padx = 10, pady = 10, bg = '#F9F1DC',
                    activebackground = '#F9F1DC', image = img_dec, width = 40, height = 37, borderwidth = 0, command = lambda:button_clicked("."))


#layout of frames and buttons
frm1.grid()
frm2.grid()
frm3.grid()


entrymain.grid(column = 0, row = 0, columnspan = 4, padx = 10, pady = 10)

btn_clear.grid(column = 1, row = 1, padx = 10, pady = 10)
btn_ce.grid(column = 0, row = 1, padx = 10, pady = 10)
btn_delete.grid(column = 2, row = 1, padx = 10, pady = 10)
btn_div.grid(column = 3, row = 1, padx = 10, pady = 10)

btn_7.grid(column = 0, row = 2, padx = 10, pady = 10)
btn_8.grid(column = 1, row = 2, padx = 10, pady = 10)
btn_9.grid(column = 2, row = 2, padx = 10, pady = 10)
btn_mult.grid(column = 3, row = 2, padx = 10, pady = 10)

btn_4.grid(column = 0, row = 3, padx = 10, pady = 10)
btn_5.grid(column = 1, row = 3, padx = 10, pady = 10)
btn_6.grid(column = 2, row = 3, padx = 10, pady = 10)
btn_add.grid(column = 3, row = 3, padx = 10, pady = 10)

btn_1.grid(column = 0, row = 4, padx = 10, pady = 10)
btn_2.grid(column = 1, row = 4, padx = 10, pady = 10)
btn_3.grid(column = 2, row = 4, padx = 10, pady = 10)
btn_sub.grid(column = 3, row = 4, padx = 10, pady = 10)

btn_0.grid(column = 1, row = 5, padx = 10, pady = 10)
btn_decimal.grid(column = 2, row = 5, padx = 10, pady = 10)
btn_equals.grid(column = 3, row = 5, padx = 10, pady = 10)


window.mainloop()
