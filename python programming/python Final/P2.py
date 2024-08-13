from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.geometry("400x300")
num=1
files=["./img/1.gif","./img/2.gif","./img/3.gif","./img/4.gif"]

def Rbtn(Event):
    num+=1
    idx=num%4
    img=Image.open(files[idx],)

btnL=Button()
btnR=Button()

btnL.bind("<cli>")
btnR.bind()
root.mainloop()












