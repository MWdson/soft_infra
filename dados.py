class Dados:
    def __init__(self):
        self._dict_dados = {}
        self._dict_material = {'Material': [], "Quantidade": []}
        self._dict_geral = {}

    def dados(self, chave, valor):
        self._dict_dados[chave] = [valor]
        print(self._dict_dados)

    def get_dados(self):
        self.padroniza_dict()
        return self._dict_geral

    def dados_material(self, material, qntd):
        self._dict_material["Material"].append(material)
        self._dict_material["Quantidade"].append(qntd)
        print(self._dict_material)

    def padroniza_dict(self):
        for chave in list(self._dict_dados.keys()):
            self._dict_geral[chave] = [self._dict_dados[chave][0] for i in range(len(self._dict_material["Material"]))]

        self._dict_geral["Material"] = self._dict_material["Material"]
        self._dict_geral["Quantidade"] = self._dict_material["Quantidade"]
