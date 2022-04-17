from tkinter import *

root = Tk()


def add_1_to_display():
    display.insert(END, "1")


def add_2_to_display():
    display.insert(END, "2")


def add_3_to_display():
    display.insert(END, "3")


def add_4_to_display():
    display.insert(END, "4")


def add_5_to_display():
    display.insert(END, "5")


def add_6_to_display():
    display.insert(END, "6")


def add_7_to_display():
    display.insert(END, "7")


def add_8_to_display():
    display.insert(END, "8")


def add_9_to_display():
    display.insert(END, "9")


def add_0_to_display():
    display.insert(END, "0")


def clear_display():
    display.delete(0, END)


def add_plus_to_display():
    display.insert(END, '+')


def equals_button_pressed():
    fulldisplay = display.get().split('+')
    numbers = []
    sum = 0
    for values in fulldisplay:
        numbers.append(int(values))
    for num_values in numbers:
        sum = sum + num_values
    display.delete(0, END)
    display.insert(0, sum)


root.title('Calculator')
display = Entry(root, width=30)
button1 = Button(root, text='1', width=10, height=5, command=add_1_to_display)
button2 = Button(root, text='2', width=10, height=5, command=add_2_to_display)
button3 = Button(root, text='3', width=10, height=5, command=add_3_to_display)
button4 = Button(root, text='4', width=10, height=5, command=add_4_to_display)
button5 = Button(root, text='5', width=10, height=5, command=add_5_to_display)
button6 = Button(root, text='6', width=10, height=5, command=add_6_to_display)
button7 = Button(root, text='7', width=10, height=5, command=add_7_to_display)
button8 = Button(root, text='8', width=10, height=5, command=add_8_to_display)
button9 = Button(root, text='9', width=10, height=5, command=add_9_to_display)
button0 = Button(root, text='0', width=10, height=5, command=add_0_to_display)
buttonPlus = Button(root, text='+', width=10, height=5, command=add_plus_to_display)
buttonEqual = Button(root, text='=', width=33, height=5, command=equals_button_pressed)
buttonClear = Button(root, text='Clear', width=10, height=5, command=clear_display)

display.grid(row=0, column=0, columnspan=3)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
buttonEqual.grid(row=5, column=0, columnspan=3)
buttonPlus.grid(row=4, column=1)
buttonClear.grid(row=4, column=2)

root.mainloop()