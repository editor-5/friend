from tkinter import *

root = Tk()
root.geometry("200x250")

upFrame = Frame(root)
upFrame.pack()
downFrame = Frame(root)
downFrame.pack()

editBox = Entry(upFrame, width=10)  # 오타 수정: upFramewidth -> upFrame, width 추가
editBox.pack(padx=20, pady=20)

listbox = Listbox(downFrame, bg='yellow')  # 오타 수정: bq -> bg
listbox.pack()

listbox.insert(END, "하나")
listbox.insert(END, "둘")
listbox.insert(END, "셋")


root.mainloop()

