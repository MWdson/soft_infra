from janela import Janela
from caixa_texto import TextView, TextViewDesabilita
from lista_validacao import ListaValida, ListaMaterial
from funcoes import *
from tkinter import messagebox, Button
from dados import *
from tabelas import Tabela


def buscando_os(event, id_da_os):
    if verifica_numero(id_da_os):
        try:
            dados = req_os(id_da_os)
        except:
            exibir_alerta(msg="Erro de requisição, verifique a sua conexão")
            return

    else:
        return

    id_requisita.set_dados()

    assunto.set_var(assunto_api(pasta='su_oss_assunto', busca_id=dados['id_assunto'][0])['assunto'][0])
    data_os.set_var(data_pt_br(dados['data_final'][0]))
    estrutura.set_var(fun_estrutura(dados['id_estrutura'][0]))


def fun_estrutura(id_estrutura):
    descricao = "Não identificado" if (id_estrutura == "") else id_estrutura
    return descricao


def exibir_alerta(title="Alerta", msg="Essa é uma mensagem de alerta"):
    messagebox.showinfo(title=title, message=msg)


def salvar():
    tabela_dados.atualiza(dados_caixas.get_dados())


# Buscando lista de materiais
try:
    dados_material = material()
    lista_material = sorted(list(dados_material['descricao']))
except True:
    lista_material = []
    print("Erro de requisição, verifique a sua conexão")

espacamento_x = 20
espacamento_y = 40
base_x = 40
base_y = 40

tabela_dados = Tabela(r"tabelas\registro.xlsx")

window = Janela(800, 400)
window.janela()

dados_caixas = Dados()

# Button teste para salvar daddos
btt_salvar = Button(text="SALVAR", command=salvar)
btt_salvar.place(x=720, y=610, width=80, height=35)


# ID da requisição
id_requisita = TextView(base_x, base_y, texto="ID Requisição", dados=dados_caixas)
id_requisita.text_view()
id_requisita.text.bind("<Tab>", lambda event: buscando_os(event, str(id_requisita.var_str.get())))

# Data atividade
data_os = TextViewDesabilita((base_x + id_requisita.width + espacamento_x), base_y, texto="Data", dados= dados_caixas)
data_os.text_view()

# Estrutura
estrutura = TextViewDesabilita((data_os.x + data_os.width + espacamento_x), base_y, width=140, texto="Estrutura", dados= dados_caixas)
estrutura.text_view()

# Alterando base Y para a proxima Linha de objetos
base_y += espacamento_y

# Assunto
assunto = TextViewDesabilita(base_x, base_y, width=340, texto='Assunto', dados= dados_caixas)
assunto.text_view()

base_y = 40
y = espacamento_y + assunto.y
for i in range(12):
    if i < 5:
        material = ListaMaterial(x=base_x, y=y, texto=f'Material {i + 1}',dados= dados_caixas)
        material.lista_produto = lista_material
        material.lista_view()
        y += espacamento_y
    else:
        base_x = 420
        material = ListaMaterial(x=base_x, y=base_y, texto=f'Material {i + 1}',dados= dados_caixas)
        material.lista_produto = lista_material
        material.lista_view()
        base_y += espacamento_y


window.loop()
