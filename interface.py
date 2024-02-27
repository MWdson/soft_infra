from janela import Janela
from caixa_texto import TextView, TextViewDesabilita
from lista_validacao import ListaValida


def teste(event):
    print(window.childrena)


window = Janela(800,400)
window.janela()


# ID da requisição
id_requisita = TextView(30,50, texto= "ID Requisição")
id_requisita.text_view()

# Data atividade
data_os = TextViewDesabilita(160,50, texto= "Data")
data_os.text_view()

# Assunto
assunto = TextViewDesabilita(30, 90, 210, texto='Assunto')
assunto.text_view()

# Material 1
espacamento = abs(id_requisita.y - assunto.y)
x = 30
y = id_requisita.y + assunto.y
y_dois = id_requisita.y

for i in range(12):
    if i < 5:
        material = ListaValida(x= x,y= y, texto=f'Material {i+1}')
        material.lista_view()
        material.quantidade_text()
        material.lista.bind('<Tab>', teste)
        y += espacamento
    else:
        x = 390
        material = ListaValida(x=x, y=y_dois, texto=f'Material {i + 1}')
        material.lista_view()
        material.quantidade_text()
        y_dois += espacamento

window.loop()
