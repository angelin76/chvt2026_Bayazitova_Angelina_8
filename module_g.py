
from tkinter import *

 
root = Tk()     # создаем корневой объект - окно
root.title("Графическое окно ")     # устанавливаем заголовок окна
root.geometry("300x250")    # устанавливаем размеры окна
 
label = Label(text="webots_test_edited") # создаем текстовую метку
label.pack()    # размещаем метку в окне
 
root.mainloop()
