from pandas import read_excel, DataFrame, concat


class Tabela:
    def __init__(self, caminho = ""):
        self.tabela = read_excel(caminho)
        self.caminho = caminho

    def atualiza(self, valor: dict):
        self.valor = DataFrame(valor)
        self.tabela = concat([self.tabela, self.valor], ignore_index= True)
        self.save()

    def save(self):
        self.tabela.to_excel(self.caminho, index=False)
