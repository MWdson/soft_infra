from tkinter import *
from rotulo import Rotulo


class TextView:
    def __init__(self, x, y, width = 80, height = 20, texto = ""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.var_str = StringVar()
        self.titulo = texto
        self.rotulo = None
        self.text = None

    def text_view(self):
        self.text = Entry(textvariable= self.var_str)
        self.text.place(x= self.x, y= self.y, width= self.width, height= self.height)
        self.rotulo = Rotulo(self.x, self.y-20, self.width, self.height, texto=self.titulo)


class TextViewDesabilita(TextView):
    def __init__(self,x, y, width = 80, height = 20, texto = ""):
        super().__init__(x, y, width, height, texto)

    def text_view(self):
        super().text_view()
        self.text.config(state= DISABLED)
