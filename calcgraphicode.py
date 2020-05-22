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

text11=Text(root,width=30,height=3,font=('arial 10 bold'))
text11.grid(row=1,columnspan=5,sticky=N+S+W+E,padx=5,pady=5)
text11.configure(background='powder blue')

button1=Button(root,text="MC",width=6)
button1.grid(row=2,column=0,padx=4)

button2=Button(root,text="MR",width=6)
button2.grid(row=2,column=1,padx=4)

button3=Button(root,text="MS",width=6)
button3.grid(row=2,column=2,padx=4)

button4=Button(root,text="M+",width=6)
button4.grid(row=2,column=3,padx=4)

button5=Button(root,text="M-",width=6)
button5.grid(row=2,column=4,padx=4)

button6=Button(root,text="←",width=6)   
button6.grid(row=3,column=0,padx=4,pady=4)

button7=Button(root,text="CE",width=6)
button7.grid(row=3,column=1,padx=4,pady=4)

button8=Button(root,text="C",width=6)
button8.grid(row=3,column=2,padx=4,pady=4)

button9=Button(root,text="±",width=6)   
button9.grid(row=3,column=3,padx=4,pady=4)

button10=Button(root,text="√",width=6)  
button10.grid(row=3,column=4,padx=4,pady=4)

button11=Button(root,text="7",width=6)
button11.grid(row=4,column=0,padx=4,pady=4)

button12=Button(root,text="8",width=6)
button12.grid(row=4,column=1,padx=4,pady=4)

button13=Button(root,text="9",width=6)
button13.grid(row=4,column=2,padx=4,pady=4)

button14=Button(root,text="/",width=6)
button14.grid(row=4,column=3,padx=4,pady=4)

button15=Button(root,text="%",width=6)
button15.grid(row=4,column=4,padx=4,pady=4)

button16=Button(root,text="4",width=6)
button16.grid(row=5,column=0,padx=4,pady=4)

button17=Button(root,text="5",width=6)
button17.grid(row=5,column=1,padx=4,pady=4)

button18=Button(root,text="6",width=6)
button18.grid(row=5,column=2,padx=4,pady=4)

button19=Button(root,text="*",width=6)
button19.grid(row=5,column=3,padx=4,pady=4)

button20=Button(root,text="1/x",width=6)
button20.grid(row=5,column=4,padx=4,pady=4)

button21=Button(root,text="1",width=6)
button21.grid(row=6,column=0,padx=4,pady=4)

button22=Button(root,text="2",width=6)
button22.grid(row=6,column=1,padx=4,pady=4)

button23=Button(root,text="3",width=6)
button23.grid(row=6,column=2,padx=4,pady=4)

button24=Button(root,text="-",width=6)
button24.grid(row=6,column=3,padx=4,pady=4)

button25=Button(root,text="=",width=6)
button25.grid(row=6,column=4,rowspan=2,sticky=N+S+W+E,padx=4,pady=4)

button26=Button(root,text="0",width=6)
button26.grid(row=7,column=0,columnspan=2,sticky=N+S+W+E,padx=4,pady=4)

button27=Button(root,text=".",width=6)
button27.grid(row=7,column=2,padx=4,pady=4)

button28=Button(root,text="+",width=6)
button28.grid(row=7,column=3,padx=4,pady=4)


root.mainloop()
