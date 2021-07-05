from tkinter import *
root = Tk()
root.title("Ihsan's Calculator")

ebox = Entry(root, width=40,  borderwidth=5)
ebox.grid(row=0, column=0, columnspan=3)


# ebox.insert(0, "Enter your name: ")
def button_click(number):
	now=ebox.get()
	ebox.delete(0, END)
	ebox.insert(0, str(now) + str(number))


def button_clear():
	ebox.delete(0, END)


def button_add():
	first_numbers=ebox.get()
	global f_num
	global math
	math='addition'
	f_num=int(first_numbers)
	ebox.delete(0, END)

def button_subtract():
	first_numbers = ebox.get()
	global f_num
	global math
	math = 'subtract'
	f_num = int(first_numbers)
	ebox.delete(0, END)


def button_multiply():
	first_numbers = ebox.get()
	global f_num
	global math
	math = 'multiplication'
	f_num = int(first_numbers)
	ebox.delete(0, END)


def button_divide():
	first_numbers = ebox.get()
	global f_num
	global math
	math = 'divide'
	f_num = int(first_numbers)
	ebox.delete(0, END)


def button_equal():
	second_numbers=int(ebox.get())
	ebox.delete(0, END)

	if math=='addition':
		ebox.insert(0, f_num + second_numbers)
	if math=='subtract':
		ebox.insert(0, f_num - second_numbers)
	if math=='multiplication':
		ebox.insert(0, f_num * second_numbers)
	if math=='divide':
		ebox.insert(0, f_num / second_numbers)


# define number buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))


# define operational buttons
button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
button_equal = Button(root, text='=', padx=91, pady=20, command=button_equal)
button_clear = Button(root, text='Clear', padx=79, pady=20, command=button_clear)
button_subtract = Button(root, text='-', padx=39, pady=20, command=button_subtract)
button_multiply = Button(root, text='x', padx=39, pady=20, command=button_multiply)
button_divide = Button(root, text='÷', padx=39, pady=20, command=button_divide)

'''button_ac = Button(root, text='AC', padx=39, pady=40, command=lambda: button_click())
button_transform = Button(root, text='+/-', padx=39, pady=40, command=lambda: button_click())
button_percent = Button(root, text='%', padx=39, pady=40, command=lambda: button_click())
button_divide = Button(root, text=':', padx=39, pady=40, command=lambda: button_click())
button_add = Button(root, text='+', padx=39, pady=40, command=lambda: button_click())
button_multiple = Button(root, text='x', padx=39, pady=40, command=lambda: button_click())
button_minus = Button(root, text='-', padx=39, pady=40, command=lambda: button_click())
button_equal = Button(root, text='=', padx=39, pady=40, command=lambda: button_click())
button_comma = Button(root, text=',', padx=39, pady=40, command=lambda: button_click())'''


# buttons placement on grid
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)


# operational button placement on grid
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

'''button_ac.grid(row=1, column=0)
button_transform.grid(row=1, column=1)
button_percent.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_multiple.grid(row=2, column=3)

button_minus.grid(row=3, column=3)

button_add.grid(row=4, column=3)

button_comma.grid(row=5, column=2)
button_equal.grid(row=5, column=3)'''



'''def clicked():
	hello = "Hello" + ebox.get()
	mylabel = Label(root, text=hello)
	mylabel.pack()


mybutton = Button(root, text="Enter your stock quote", command=clicked)
'''

root.mainloop()
