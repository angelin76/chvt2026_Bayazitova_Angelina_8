from tkinter import *
 
root = Tk()
root.title("webots_test_edited")
root.geometry("250x150") 
 
main_menu = Menu()
main_menu.add_cascade(label="Карта")
main_menu.add_cascade(label="Роботы и точки")
main_menu.add_cascade(label="Терминал")
main_menu.add_cascade(label="Параметры Nav2")
 
root.config(menu=main_menu)
root.mainloop()
