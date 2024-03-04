import pandas as pd


class Tabela:
    def __init__(self, caminho = ""):
        self.tabela = pd.read_excel(r"{}".format(caminho))
        self.caminho = caminho

    def atualiza(self, valor: dict):
        self.valor = pd.DataFrame(valor)
        self.tabela = pd.concat([self.tabela, self.valor], ignore_index= True)
        self.save()

    def save(self):
        self.tabela.to_excel(r"{}".format(self.caminho), index=False)
