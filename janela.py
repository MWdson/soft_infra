from tkinter import *

class Janela:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = None

    def janela(self):
        self.window = Tk()
        self.window.geometry(f"{self.width}x{self.height}")

    def loop(self):
        self.window.mainloop()

    def childrena(self):
        return list(self.window.children())
