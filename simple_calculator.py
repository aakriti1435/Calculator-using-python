import tkinter as t

root = t.Tk()          # object of imported library
root.title("calculator")        # title of application
root.state("zoomed")
# root.iconbitmap("smile.ico")
root.configure()           # for background changes attribute bg

# label1 = t.Label(root, text="Welcome !", font="arial 50 bold underline ")
# label1.grid(padx=300, pady=20, row=0, column=0)


label2 = t.Label(root, text="Enter A:", font="arial 25 bold")
label2.grid(padx=40, pady=10, row=0, column=0)

label3 = t.Label(root, text="Enter B:", font="arial 25 bold")
label3.grid(row=2, column=0)

textbox1 = t.Entry(root)
textbox1.grid(row=0, column=1)

textbox2 = t.Entry(root)
textbox2.grid(row=2, column=1)

textbox3 = t.Entry(root)


def add():
    a = textbox1.get()
    b = textbox2.get()
    c = int(a) + int(b)
    textbox3.delete(0, "end")
    textbox3.insert(0, c)


def sub():
    a = textbox1.get()
    b = textbox2.get()
    c = int(a) - int(b)
    textbox3.delete(0, "end")
    textbox3.insert(0, c)


def mul():
    a = textbox1.get()
    b = textbox2.get()
    c = int(a) * int(b)
    textbox3.delete(0, "end")
    textbox3.insert(0, c)


def div():
    a = textbox1.get()
    b = textbox2.get()
    c = int(a) / int(b)
    textbox3.delete(0, "end")
    textbox3.insert(0, c)


def power():
    a = textbox1.get()
    b = textbox2.get()
    c = int(a) ** int(b)
    textbox3.delete(0, "end")
    textbox3.insert(0, c)


# label4 = t.Label(root, text="Choose Operation:", font="arial 25 bold")
# label4.grid(row=5, column=0)


button1 = t.Button(root, text="A + B", command=add, bg="light blue")
button1.grid(row=4, column=0)

button2 = t.Button(root, text="A - B", command=sub, bg="light blue")
button2.grid(row=6, column=1)

button3 = t.Button(root, text="A * B", command=mul, bg="light blue")
button3.grid(row=8, column=0)

button4 = t.Button(root, text="A / B", command=div, bg="light blue")
button4.grid(row=10, column=1)

button5 = t.Button(root, text="A**B", command=power, bg="light blue")
button5.grid(row=12, column=0)

label5 = t.Label(root, text="RESULT:", font="arial 25 bold")
label5.grid(row=14, column=0)
textbox3.grid(row=14, column=1)

root.mainloop()
