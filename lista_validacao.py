from tkinter.ttk import Combobox
from tkinter import StringVar, Entry, DISABLED, NORMAL
from rotulo import Rotulo


class ListaValida:
    def __init__(self, x, y, dados, lista, width=270, height=20, texto=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.titulo = texto
        self.lista = None
        self.lista_produto = lista
        self.rotulo = None
        self.var_material = None
        self.dados = dados
        self.lista_view()

    def lista_view(self):
        self.var_material = StringVar()
        self.lista = Combobox(textvariable=self.var_material, values=self.lista_produto)
        self.lista.place(x=self.x, y=self.y, width=self.width, height=self.height)
        self.lista.bind("<<ComboboxSelected>>", lambda event: self.guarda_dados())
        self.rotulo = Rotulo(x=self.x, y=self.y-20, width=self.width, height=self.height, texto=self.titulo)

    def guarda_dados(self):
        self.dados.dados(chave= self.titulo, valor= str(self.var_material.get()))

    def limpa(self):
        self.var_material.set("")


class ListaMaterial(ListaValida):
    def __init__(self, x, y, dados, lista, width=270, height=20, texto=""):
        super().__init__(x, y, dados, lista, width, height, texto)
        self.quantidade = None
        self.var_qntd = None
        self.txt_qnt = None
        self.quantidade_text()

    def lista_view(self):
        super().lista_view()
        self.lista.bind("<<ComboboxSelected>>", lambda event: self.habilita())

    def quantidade_text(self, valor="Valor"):
        self.txt_qnt = valor
        self.var_qntd = StringVar()
        self.quantidade = Entry(textvariable=self.var_qntd, state=DISABLED)
        self.quantidade.place(x=(self.x + self.width + 20), y=self.y, width=50, height=20)
        self.quantidade.bind("<FocusOut>", lambda event: self.guarda_dados())

    def habilita(self):
        self.quantidade.configure(state=NORMAL)

    def guarda_dados(self):
        self.dados.dados_material(self.titulo, str(self.var_material.get()), str(self.var_qntd.get()))

    def limpa(self):
        super().limpa()
        self.var_qntd.set("")