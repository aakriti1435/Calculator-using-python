from tkinter import *

root=Tk()
root.title("Calculator")
# root.geometry("210x250")

x=0
y=0
r=0
c=''
temp=0
mem=0
global op,clrscr,fstage,dotcl
op=False
clrscr=True
fstage=True
dotcl=True
def normal():
    textbox1.config(state=NORMAL)
def disable():
    textbox1.config(state=DISABLED)
def justify():
    textbox1.tag_configure('sometag', justify='right') #This is for Right Justify

    textbox1.tag_add('sometag', 1.0, 'end')
def recip():
    normal()
    temp=int(textbox1.get("1.0","end-1c"))
    r=1/temp
    textbox1.delete("1.0","end")
    textbox1.insert('1.0', r)
    justify()
    disable()

def negpos():
    global x
    textbox1.config(state=NORMAL)

    temp=int(textbox1.get("1.0","end-1c"))
    textbox1.delete('1.0','end-1c')
    temp = temp * -1
    textbox1.insert('1.0', temp)

    textbox1.config(state=NORMAL)

    #temp=x * (temp/100)

def cfun():
    textbox1.delete(0,'end')
    op=False
    clrscr=True
    fstage=True
    dotcl=True

def cefun():
    textbox1.delete(0,'end')
    op=False
    clrscr=True
    dotcl=True

def addtext(a): #30*900/100
    global clrscr
    textbox1.config(state=NORMAL)
    if(clrscr==True):

        textbox1.delete('1.0','end')
        textbox1.insert('1.0', a)


        textbox1.tag_configure('sometag', justify='right') #This is for Right Justify

        textbox1.tag_add('sometag', 1.0, 'end')#This is for adding configured tag

        clrscr=False
    else:
        #b=textbox1.get()
        b=textbox1.get("1.0","end-1c")
        # print(b,a)
        if(a!="0"):
            if(b!="0"):
                textbox1.delete('1.0','end-1c')
                #print(b)
                b=b+a
                # print(a,b)
                textbox1.insert('1.0', b)

                textbox1.tag_configure('sometag', justify='right') #This is for Right Justify
                textbox1.tag_add('sometag', 1.0, 'end')#This is for adding configured tag

                #textbox1.delete(0,'end')

                #textbox1.insert(0,b)
            if(b=="0"):
                textbox1.delete('1.0','end-1c')
                textbox1.insert('1.0', a)
        if(a=="0"):
            if(b!="0"):
                textbox1.delete('1.0','end-1c')
                #print(b)
                b=b+a
                # print(a,b)
                textbox1.insert('1.0', b)

    textbox1.config(state=DISABLED)
    return

def plusclick():
    global op,clrscr,fstage

    global c
    c='s'
    global r

    if(fstage==True):
        op=True
        getFirstValue()
        fstage=False
    else:
        op=False
        getSecondValue()
        fstage=True

    clrscr = True


def minusclick():
    global c
    c='m'
    getFirstValue()

def divideclick():
    global c
    c='d'
    getFirstValue()

def productclick():
    global c
    c='p'
    getFirstValue()
def result():
    global r,c,x,y,clrscr

    if c=='s':
        print(x,r,y,c)
        r=int(x)+int(y)
        
    if c=='m':
            r=int(x)-int(y)
    if c=='d':
            r=int(x)/int(y)
    if c=='p':
            r=int(x)*int(y)

    textbox1.delete('1.0','end-1c')
    textbox1.insert('1.0', r)
    #textbox1.delete(0,'end')
    #textbox1.insert(0,r)

def getFirstValue():
    global x
    x=textbox1.get("1.0","end-1c")#textbox1.get()
    #textbox1.delete(0,'end')
    return

def getSecondValue():
    global y,r,x,c,op
    #print(x,r,y,c,op)
    if(fstage==True):
        y=textbox1.get("1.0","end-1c")#textbox1.get()
        textbox1.delete(0,'end')
        result()
    else:
        y=textbox1.get("1.0","end-1c")#textbox1.get()
        result()


    textbox1.delete(0,'end')
    textbox1.insert(0,r)
    return

def equalClick():

    getSecondValue()

    result()

textbox1 = Text(root, height=1.5, width=25)
#textbox1.insert('1.0',"r")
#textbox1.tag_configure("right", justify='right')
#textbox1.tag_add('right', 1.0, 'end')
#textbox1.tag_configure('sometag', justify='right')
#textbox1.tag_add('sometag', 1.0, 'end')
#t.pack()
textbox1.grid(padx=5,pady=5,row=0,column=0,columnspan=4)


#textbox1=Entry(root,width=30,height=20)
#textbox1.grid(padx=5,pady=5,row=0,column=0,columnspan=4)



button1=Button(root,text="1",command=lambda :addtext("1"))
button1.grid(row=1,column=0)

button2=Button(root,text="2",command=lambda :addtext("2"))
button2.grid(row=1,column=1)

button3=Button(root,text="3",command=lambda :addtext("3"))
button3.grid(row=1,column=2)

buttonplus=Button(root,text="+",command=plusclick)
buttonplus.grid(row=1,column=3)

button4=Button(root,text="4",command=lambda :addtext("4"))
button4.grid(row=2,column=0,pady=7)

button5=Button(root,text="5",command=lambda :addtext("5"))
button5.grid(row=2,column=1)

button6=Button(root,text="6",command=lambda :addtext("6"))
button6.grid(row=2,column=2)

buttonminus=Button(root,text="-",command=minusclick)
buttonminus.grid(row=2,column=3)

button7=Button(root,text="7",command=lambda :addtext("7"))
button7.grid(row=3,column=0,pady=5)

button8=Button(root,text="8",command=lambda :addtext("8"))
button8.grid(row=3,column=1)

button9=Button(root,text="9",command=lambda :addtext("9"))
button9.grid(row=3,column=2)

buttonproduct=Button(root,text="*",command=productclick)
buttonproduct.grid(row=3,column=3)

button0=Button(root,text="0",command=lambda :addtext("0"))
button0.grid(row=4,column=0,pady=5)

buttondot=Button(root,text=".")
buttondot.grid(row=4,column=1,pady=10)

buttonequal=Button(root,text="=",command=equalClick)
buttonequal.grid(row=4,column=2)

buttondivide=Button(root,text="/",command=divideclick)
buttondivide.grid(row=4,column=3)

buttonmc=Button(root,text="MC",command=lambda :addtext("1"))
buttonmc.grid(row=5,column=0)

buttonmr=Button(root,text="MR",command=lambda :addtext("1"))
buttonmr.grid(row=5,column=1)

buttonms=Button(root,text="MS",command=lambda :addtext("1"))
buttonms.grid(row=5,column=2)

buttonplusminus=Button(root,text="+/-",command=negpos)
buttonplusminus.grid(row=5,column=3)

buttonce=Button(root,text="CE ",command=cefun)
buttonce.grid(row=6,column=0,pady=10)

buttonce=Button(root,text=" C ",command=cfun)
buttonce.grid(row=6,column=1,pady=10)

buttonsqrt=Button(root,text="sqrt",command=lambda :addtext("1"))
buttonsqrt.grid(row=6,column=2,pady=10)

buttondivx=Button(root,text="1/x",command=lambda :recip())
buttondivx.grid(row=6,column=3,pady=10)



root.resizable(0,0)

root.mainloop()
