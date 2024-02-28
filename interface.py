from janela import Janela
from caixa_texto import TextView, TextViewDesabilita
from lista_validacao import ListaValida
from funcoes import *
from tkinter import messagebox


def buscando_os(event, id_da_os):
    if verifica_numero(id_da_os):
        try:
            dados = req_os(id_da_os)
        except:
            exibir_alerta(msg="Erro de requisição, verifique a sua conexão")
            return

    else:
        return

    assunto.var_str.set(assunto_api(pasta='su_oss_assunto', busca_id=dados['id_assunto'][0])['assunto'][0])
    data_os.var_str.set(data_pt_br(dados['data_final'][0]))



def verificando_numero_id(id_da_os):
    pass


def exibir_alerta(title = "Alerta", msg = "Essa é uma mensagem de alerta"):
    messagebox.showinfo(title= title, message= msg)


def mostra_classe(event, objeto):
    print(objeto.__class__.__name__)
    print(type(objeto).__name__)


# Buscando lista de materiais
try:
    dados_material = material()
    lista_material = sorted(list(dados_material['descricao']))
except:
    lista_material = []
    print("Erro de requisição, verifique a sua conexão")


lista_de_objetos = []
espaçamento_x = 20
espacamento_y = 40
base_x = 40
base_y = 40


window = Janela(800,400)
window.janela()


# ID da requisição
id_requisita = TextView(base_x,base_y, texto= "ID Requisição")
id_requisita.text_view()
id_requisita.text.bind("<Tab>", lambda event: buscando_os(event, str(id_requisita.var_str.get())))

# Data atividade
data_os = TextViewDesabilita((base_x + id_requisita.width + espaçamento_x),base_y, texto= "Data")
data_os.text_view()

# Estrutura
estrutura = TextViewDesabilita((data_os.x + data_os.width + espaçamento_x), base_y, width= 140 ,texto= "Estrutura")
estrutura.text_view()

# Assunto
assunto = TextViewDesabilita(base_x, (data_os.y + espacamento_y), 340, texto='Assunto')
assunto.text_view()

lista_de_objetos.extend([id_requisita, data_os, estrutura, assunto])

y = espacamento_y + assunto.y
for i in range(12):
    if i < 5:
        material = ListaValida(x= base_x,y= y, texto=f'Material {i+1}')
        material.lista_produto = lista_material
        material.lista_view()
        material.quantidade_text()
        material.lista.bind("<Tab>", lambda event: mostra_classe(event, material))
        y += espacamento_y
    else:
        base_x = 420
        material = ListaValida(x=base_x, y=base_y, texto=f'Material {i + 1}')
        material.lista_produto = lista_material
        material.lista_view()
        material.quantidade_text()
        material.lista.bind("<Tab>", lambda event: mostra_classe(event, material))
        base_y += espacamento_y
    lista_de_objetos.append(material)

window.loop()
