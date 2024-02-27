from tkinter import Label

class Rotulo:
    def __init__(self, x, y, width, height, texto = ""):
        self.titulo = Label(text= texto, anchor="w")
        self.titulo.place(x=x, y=y, width= width, height= height)
