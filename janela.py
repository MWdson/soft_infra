from tkinter import *


class Janela:
    def __init__(self, width, height, texto = ""):
        self.width = width
        self.height = height
        self.window = None
        self.texto = texto

    def janela(self):
        self.window = Tk()
        self.window.resizable(width=False, height=False)
        #img_icon = PhotoImage(file=r"logoas.png")
        #self.window.iconphoto(False, img_icon)
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.title(self.texto)

    def loop(self):
        self.window.mainloop()

    def finaliza(self):
        self.window.destroy()
