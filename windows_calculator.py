import math
from tkinter import *

root = Tk()
root.title("CALCULATOR")
# root.iconbitmap("calc.ico")
root.resizable(0, 0)


"""
def click(event):
    global sc_value
    text = event.widget.cget("text")
    print("text")
    if text == "=":
        if sc_value.get().isdigit():
            value = int(sc_value.get())
        else:
            value = eval(text_box.get())
        sc_value.set(value)
        text_box.update()

    elif text == "C":
        sc_value.set("")
        text_box.update()

    else:
        sc_value.set(sc_value.get() + text)
        text_box.update()
"""


text_in = StringVar()
operator = ""


def click(numbers):
    global operator
    operator = operator + str(numbers)
    text_in.set(operator)


def equal():
    global operator
    opp = str(eval(operator))
    text_in.set(opp)
    operator = ""


def clr_but():
    text_in.set("")


root.configure(bg="#D2D2D2")

text_box = Entry(root, textvar=text_in, width=30, font="Arial 15  bold", bd=2)
text_box.grid(row=1, rowspan=1, columnspan=5, sticky=N+S+W+E, padx=5, pady=5)
# text_box.configure(bg="#2AFFFF")

b1 = Button(root, text="MC", width=6, font="Arial 15 bold")
b1.grid(row=3, column=0, padx=4)

b2 = Button(root,  text="MR", width=6, font="Arial 15 bold")
b2.grid(row=3, column=1, padx=4)

b3 = Button(root, text="MS", width=6, font="Arial 15 bold")
b3.grid(row=3, column=2, padx=4)

b4 = Button(root, text="M+", width=6, font="Arial 15 bold")
b4.grid(row=3, column=3, padx=4)

b5 = Button(root, text="M-", width=6, font="Arial 15 bold")
b5.grid(row=3, column=4, padx=4)

b6 = Button(root, text="←", width=6, font="Arial 15 bold")
b6.grid(row=4, column=0, padx=4, pady=4)

b7 = Button(root, text="CE", width=6, font="Arial 15 bold")
b7.grid(row=4, column=1, padx=4, pady=4)

b8 = Button(root, text="C", width=6, font="Arial 15 bold", command=clr_but)
b8.grid(row=4, column=2, padx=4, pady=4)

b9 = Button(root, text="±", width=6, font="Arial 15 bold")
b9.grid(row=4, column=3, padx=4, pady=4)

b10 = Button(root, text="√", width=6, font="Arial 15 bold")
b10.grid(row=4, column=4, padx=4, pady=4)

b11 = Button(root, text="7", width=6, font="Arial 15 bold", command=lambda: click(7))
b11.grid(row=5, column=0, padx=4, pady=4)

b12 = Button(root, text="8", width=6, font="Arial 15 bold", command=lambda: click(8))
b12.grid(row=5, column=1, padx=4, pady=4)

b13 = Button(root, text="9", width=6, font="Arial 15 bold", command=lambda: click(9))
b13.grid(row=5, column=2, padx=4, pady=4)

b14 = Button(root, text="/", width=6, font="Arial 15 bold", command=lambda: click("/"))
b14.grid(row=5, column=3, padx=4, pady=4)

b15 = Button(root, text="%", width=6, font="Arial 15 bold", command=lambda: click("%"))
b15.grid(row=5, column=4, padx=4, pady=4)

b16 = Button(root, text="4", width=6, font="Arial 15 bold", command=lambda: click(4))
b16.grid(row=6, column=0, padx=4, pady=4)

b17 = Button(root, text="5", width=6, font="Arial 15 bold", command=lambda: click(5))
b17.grid(row=6, column=1, padx=4, pady=4)

b18 = Button(root, text="6", width=6, font="Arial 15 bold", command=lambda: click(6))
b18.grid(row=6, column=2, padx=4, pady=4)

b19 = Button(root, text="*", width=6, font="Arial 15 bold", command=lambda: click("*"))
b19.grid(row=6, column=3, padx=4, pady=4)

b20 = Button(root, text="1/x", width=6, font="Arial 15 bold")
b20.grid(row=6, column=4, padx=4, pady=4)

b21 = Button(root, text="1", width=6, font="Arial 15 bold", command=lambda: click(1))
b21.grid(row=7, column=0, padx=4, pady=4)

b22 = Button(root, text="2", width=6, font="Arial 15 bold", command=lambda: click(2))
b22.grid(row=7, column=1, padx=4, pady=4)

b23 = Button(root, text="3", width=6, font="Arial 15 bold", command=lambda: click(3))
b23.grid(row=7, column=2, padx=4, pady=4)

b24 = Button(root, text="-", width=6, font="Arial 15 bold", command=lambda: click("-"))
b24.grid(row=7, column=3, padx=4, pady=4)

b25 = Button(root, text="=", width=6, font="Arial 15 bold", command=equal)
b25.grid(row=7, column=4, rowspan=2, sticky=N+S+E+W, padx=4, pady=4)

b26 = Button(root, text="0", width=6, font="Arial 15 bold", command=lambda: click(0))
b26.grid(row=8, column=0, columnspan=2, sticky=N+S+E+W, padx=4, pady=4)

b27 = Button(root, text=".", width=6, font="Arial 15 bold", command=lambda: click("."))
b27.grid(row=8, column=2, padx=4, pady=4)

b28 = Button(root, text="+", width=6, font="Arial 15 bold", command=lambda: click("+"))
b28.grid(row=8, column=3, padx=4, pady=4)

root.mainloop()
