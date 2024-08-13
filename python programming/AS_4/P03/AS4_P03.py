from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk 
tk = Tk()
#초기 화면 크기 설정, 이름 설정
tk.geometry("400x300")
tk.title("Image Viewer")
#사진 배치 초기 설정(위로 배치)
label = Label(tk)
label.pack(side="top")

#사진을 너비 400에 맞춰 리사이징 해주는 함수
def resizer(IMG):
    #사진의 너비, 높이 저장변서
    width, height=IMG.size
    #너비를 400으로 맞추고, 높이를 이에 맞춰 조정
    y=int((400 / width) * height)
    IMG=IMG.resize((400 ,y))
    #만약 높이가 너무 클경우 창의 세로 길이를 늘리기
    if(y >= 280):
        tk.geometry(f"400x{y+50}")
    return IMG
#한번만 클릭했을때 준비된 사진 띄우기
def one_click(Event):
    img = Image.open("./P03/nugget.jpg")
    show(img)
#두번 클릭했을때 선택된 파일을 띄우기
def double_click(Event):
    filepath = filedialog.askopenfilename()
    if filepath:
        img = Image.open(filepath)
        show(img)  
#사진을 화면에 표시하는 함수
def show(IMG):
    IMG = resizer(IMG)
    tk_img = ImageTk.PhotoImage(IMG)
    label.config(image=tk_img)
    label.image= tk_img
    
#버튼과 한번, 두번 클릭했을때 동작할 함수 지정
btn=Button(tk, text="Mouse Clicks")
btn.pack(side="bottom")
btn.bind('<Double-Button-1>',double_click)
btn.bind('<Button-1>', one_click)
tk.mainloop()