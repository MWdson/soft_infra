class Dados:
    def __init__(self):
        self._dict_dados = {}

    def atualiza(self, chave, valor):
        self._dict_dados[chave] = [valor]
        print(self._dict_dados)

    def get_dados(self):
        return self._dict_dados
