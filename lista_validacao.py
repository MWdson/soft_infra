from tkinter.ttk import Combobox
from tkinter import StringVar
from rotulo import Rotulo
from caixa_texto import TextView


class ListaValida:
    def __init__(self, x, y, width = 270, height = 20, texto = ""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.titulo = texto
        self.lista = None
        self.lista_produto = []
        self.rotulo = None
        self.var_material = None
        self.var_qntd = None

    def lista_view(self):
        self.var_material = StringVar()
        self.lista = Combobox(textvariable= self.var_material ,values= self.lista_produto)
        self.lista.place(x= self.x, y= self.y, width= self.width, height= self.height)
        self.rotulo = Rotulo(x= self.x, y= self.y-20, width= self.width, height= self.height, texto= self.titulo)

    def quantidade_text(self):
        self.var_qntd = StringVar()
        self.quantidade = TextView(x= (self.x+self.width+20),y= self.y, width= 50, texto= "Qntd.")
        self.quantidade.text_view()

