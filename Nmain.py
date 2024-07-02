
import tkinter as tk

win=tk.Tk()
win.geometry("1200x800")
win.resizable(False,False)

win.config(bg="aqua")
sovalat=[0,1,2,3,4,5,6,7,8]
x=0
def print():
    # تغیر سوالات
    a="svalat"
    lab.config(text=a,font="Homa 10")
    btn.place(x=500,y=1000)
    btn2=tk.Button(text="<<",bg="yellow",fg="blue",font="calibri 35")
    btn2.place(x=480,y=660)

    btn3=tk.Button(text=">>",bg="yellow",fg="blue",font="calibri 35",command=next)
    btn3.place(x=580,y=660)

def next():
    x=x+1
    lab.config(text=sovalat[x])
    
    





# تغیر سلام
lab=tk.Label(win,width=100,height=26,font="Homa 10",text="salam")
lab.place(x=160,y=50)
str=tk.StringVar
btn=tk.Button(win,text="start",bg="black",fg="yellow",font="calibri 35",command=print)
btn.place(x=500,y=660)

win.mainloop()
