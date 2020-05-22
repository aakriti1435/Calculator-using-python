import math
from tkinter import *
root=Tk()

x=0
y=0
r=0
b=0
c=''

global clrscr
clrscr=True
op=False
fstage=True
global temp
temp=""
dotcl=True
def calculator():
    root.title("Calculator")
    root.resizable(0,0)
    return

def normal():
    text11.config(state=NORMAL)
    return
def disable():
    text11.config(state=DISABLED)
    return
def justify():
    text11.tag_configure('sometag',
                         justify='right')#for right justify
    text11.tag_add('sometag','1.0','end')
    return

def values(text):
    global clrscr
    global a,b
    normal()
    zero=text11.get("1.0","end-1c")
    if(clrscr==True):
        text11.delete('1.0','end')
        a=text["text"]
        text11.insert('1.0',a)
        clrscr=False
    else:
        if(text["text"]!="0"):
            if(zero!="0"):
                a=text["text"]
                text11.delete("1.0",'end-1c')
                zero=zero+a
                text11.insert('1.0',zero)
            if(zero=="0"):
                a=text["text"]
                text11.delete('1.0','end-1c')
                text11.insert('1.0', a)
        if(text["text"]=="0"):
            if(zero!="0"):
                a=text["text"]
                text11.delete('1.0','end-1c')
                zero=zero+a
                text11.insert('1.0', zero)

    justify()
    disable()
    return
def plusClick():
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
    clrscr=True
    return
def minusclick():
    global op,clrscr,fstage
    global c
    c='m'
    global r
    if(fstage==True):
        op=True
        getFirstValue()
        fstage=False
    else:
        op=False
        getSecondValue()
        fstage=True
    clrscr=True
    return
def divideclick():
    global op,clrscr,fstage
    global c
    c='d'
    global r
    if(fstage==True):
        op=True
        getFirstValue()
        fstage=False
    else:
        op=False
        getSecondValue()
        fstage=True
    clrscr=True
    return
def productclick():
    global op,clrscr,fstage
    global c
    c='p'
    global r
    if(fstage==True):
        op=True
        getFirstValue()
        fstage=False
    else:
        op=False
        getSecondValue()
        fstage=True
    clrscr=True
    return
def percent():
    global op,clrscr,fstage
    global c,x
    c='rr'
    global r

    normal()
    temp=text11.get('1.0','end')
    r=temp*(x/100)
    text11.delete('1.0','end')
    text11.insert('1.0',r)
    justify()
    disable()

    clrscr=True

def result():
    global r,c,x,y,clrscr
    if c=='s':
        r=int(x)+int(y)
    if c=='m':
        r=int(x)-int(y)
    if c=='d':
        r=int(x)/int(y)
    if c=='p':
        r=int(x)*int(y)
    if c=='rr':
        r=str((int(x)/100)*int(y))
    text11.delete('1.0','end-1c')
    text11.insert('1.0',r)
    return
def getFirstValue():
    global x
    x=text11.get("1.0","end-1c")
    justify()
    return
def getSecondValue():
    global y,r,x,c,op
    if(fstage==True):
        y=text11.get("1.0","end-1c")
        text11.delete('1.0','end')
        result()
    else:
        y=text11.get("1.0","end-1c")
        result()
    normal()
    text11.delete('1.0','end')
    text11.insert('1.0',r)
    justify()
    disable()
    return
def equalClick():
    getSecondValue()
    result()
    justify()
    return
def clear():
     global op,a,b,c
     a=0
     b=0
     c=0
     op=""
     normal()

     text11.delete('1.0','end')
     dotcl=True
     disable()

def negative():
    global b
    normal()
    b=text11.get('1.0','end-1c')
    b=str(int(b)*(-1))
    text11.delete('1.0','end-1c')
    text11.insert('1.0',b)
    justify()
    disable()
    return
def mPlus():
    global temp
    normal()
    if(temp==""):
         temp=text11.get('1.0','end-1c')
         justify()
         disable()
    return
def mMinus():
    global temp
    temp=""
    return

def MS():
    global temp
    normal()
    if(temp==""):
         temp=text11.get('1.0','end-1c')
         justify()
         disable()

def MR():
    normal()
    if(temp!=""):
        text11.delete('1.0','end-1c')
        text11.insert('1.0',temp)
    elif(temp==""):
        text11.delete('1.0','end-1c')
        text11.insert('1.0',"0")
        justify()
    disable()
    return
def MC():
    global temp
    temp=""
    return
def CE():
    normal()
    global b
    b=""
    text11.delete('1.0','end-1c')
    #text11.insert('1.0',"0")
    justify()
    disable()
    return
def divison():
    global b
    normal()
    b=text11.get('1.0','end-1c')
    b=str(1/int(b))
    text11.delete('1.0','end-1c')
    text11.insert('1.0',b)
    justify()
    disable()
    return
def squareRoot():
    global b

    normal()

    b=text11.get('1.0','end-1c')
    b=math.sqrt(int(b))

    text11.delete('1.0','end-1c')

    text11.insert('1.0',b)

    justify()
    disable()

    return
def dot():
    global d,dotcl
    d="."
    normal()
    b=text11.get('1.0','end-1c')
    if(dotcl):
        b=b+d
        text11.delete('1.0','end-1c')
        text11.insert('1.0',b)
        dotcl=False
    justify()
    disable()
    return

text11=Text(root,width=30,height=3,font=('arial 10 bold'))

text11.grid(row=1,columnspan=5,sticky=N+S+W+E,padx=5,pady=5)

text11.configure(background='powder blue')




button1=Button(root,text="MC",width=6,command=MC)
button1.grid(row=2,column=0,padx=4)

button2=Button(root,text="MR",width=6,command=MR)
button2.grid(row=2,column=1,padx=4)

button3=Button(root,text="MS",width=6,command=MS)
button3.grid(row=2,column=2,padx=4)

button4=Button(root,text="M+",width=6,command=mPlus)
button4.grid(row=2,column=3,padx=4)

button5=Button(root,text="M-",width=6,command=mMinus)
button5.grid(row=2,column=4,padx=4)

button6=Button(root,text="←",width=6)   #alt27(23 to 27)
button6.grid(row=3,column=0,padx=4,pady=4)

button7=Button(root,text="CE",width=6,command=CE)
button7.grid(row=3,column=1,padx=4,pady=4)

button8=Button(root,text="C",width=6,command=clear)
button8.grid(row=3,column=2,padx=4,pady=4)

button9=Button(root,text="±",width=6,command=negative)   #alt+0177
button9.grid(row=3,column=3,padx=4,pady=4)

button10=Button(root,text="√",width=6,command=squareRoot)  #alt+251
button10.grid(row=3,column=4,padx=4,pady=4)

button11=Button(root,text="7",width=6,command=lambda:values(button11))
button11.grid(row=4,column=0,padx=4,pady=4)

button12=Button(root,text="8",width=6,command=lambda:values(button12))
button12.grid(row=4,column=1,padx=4,pady=4)

button13=Button(root,text="9",width=6,command=lambda:values(button13))
button13.grid(row=4,column=2,padx=4,pady=4)

button14=Button(root,text="/",width=6,command=divideclick)
button14.grid(row=4,column=3,padx=4,pady=4)

button15=Button(root,text="%",width=6,command=percent)
button15.grid(row=4,column=4,padx=4,pady=4)

button16=Button(root,text="4",width=6,command=lambda:values(button16))
button16.grid(row=5,column=0,padx=4,pady=4)

button17=Button(root,text="5",width=6,command=lambda:values(button17))
button17.grid(row=5,column=1,padx=4,pady=4)

button18=Button(root,text="6",width=6,command=lambda:values(button18))
button18.grid(row=5,column=2,padx=4,pady=4)

button19=Button(root,text="*",width=6,command=productclick)
button19.grid(row=5,column=3,padx=4,pady=4)

button20=Button(root,text="1/x",width=6,command=divison)
button20.grid(row=5,column=4,padx=4,pady=4)

button21=Button(root,text="1",width=6,command=lambda:values(button21))
button21.grid(row=6,column=0,padx=4,pady=4)

button22=Button(root,text="2",width=6,command=lambda:values(button22))
button22.grid(row=6,column=1,padx=4,pady=4)

button23=Button(root,text="3",width=6,command=lambda:values(button23))
button23.grid(row=6,column=2,padx=4,pady=4)

button24=Button(root,text="-",width=6,command=minusclick)
button24.grid(row=6,column=3,padx=4,pady=4)

button25=Button(root,text="=",width=6,command=equalClick)
button25.grid(row=6,column=4,rowspan=2,sticky=N+S+W+E,padx=4,pady=4)

button26=Button(root,text="0",width=6,command=lambda:values(button26))
button26.grid(row=7,column=0,columnspan=2,sticky=N+S+W+E,padx=4,pady=4)

button27=Button(root,text=".",width=6,command=dot)
button27.grid(row=7,column=2,padx=4,pady=4)

button28=Button(root,text="+",width=6,command=plusClick)
button28.grid(row=7,column=3,padx=4,pady=4)

if(__name__=="__main__"):
    calculator()
root.mainloop()
