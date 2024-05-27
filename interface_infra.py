from func import *
from janela import Janela
from caixa_texto import TextView, TextViewDesabilita
from lista_validacao import ListaValida, ListaMaterial
from tkinter import messagebox, Button
from dados import *
from tabelas import Tabela


def processo_interface(usuario="Não informado"):
    user = usuario

    def buscando_os(event, id_da_os):
        if verifica_numero(id_da_os):
            try:
                dados = req_os(id_da_os)
                if ((dados['id_estrutura'][0]) == "") or ((dados['id_estrutura'][0]) == "0"):
                    exibir_alerta(msg="ERRO!\nEssa atividade não é de requisição de material!")
                    return
            except:
                exibir_alerta(msg="Erro de requisição, verifique a sua conexão")
                return

        else:
            return

        data_registro.set_var(data_agora())
        assunto.set_var(assunto_api(pasta='su_oss_assunto', busca_id=dados['id_assunto'][0])['assunto'][0])
        data_os.set_var(data_pt_br(dados['data_final'][0]))
        estrutura.set_var(fun_estrutura(dados['id_estrutura'][0]))

    def exibir_alerta(title="Alerta", msg="Essa é uma mensagem de alerta"):
        messagebox.showinfo(title=title, message=msg)

    def salvar():
        tabela_dados.atualiza(dados_caixas.get_dados())
        exibir_alerta("REGISTRADO COM ÊXITO!", "Dados Salvos!")
        for elemento in lista_objetos:
            elemento.limpa()

    # Buscando lista de materiais
    try:
        dados_material = fun_material()
        lista_material = sorted(list(dados_material['descricao']))
    except:
        lista_material = []
        print("Erro de requisição, verifique a sua conexão")

    espacamento_x = 20
    espacamento_y = 40
    base_x = 40
    base_y = 40
    lista_objetos = []

    tabela_dados = Tabela(r"registro.xlsx")

    window = Janela(800, 400)
    window.janela()

    dados_caixas = Dados()

    # Button teste para salvar daddos
    btt_salvar = Button(text="SALVAR", command=salvar)
    btt_salvar.place(x=600, y=360, width=80, height=35)

    # ID da Auditoria
    id_auditoria = TextView(base_x, base_y, texto="ID Auditoria", dados=dados_caixas)
    id_auditoria.text_view()


    # Retirante
    retirante = ListaValida((base_x + espacamento_x + id_auditoria.width), base_y, width=240, dados=dados_caixas, lista=['TK Engenharia', "JCE", "Equipe Interna"], texto="Solicitante")


    # Alterando base Y para a proxima Linha de objetos
    base_y += espacamento_y

    # ID da requisição
    id_requisita = TextView(base_x, base_y, texto="ID Requisição", dados=dados_caixas)
    id_requisita.text_view()
    id_requisita.text.bind("<Tab>", lambda event: buscando_os(event, str(id_requisita.var_str.get())))

    # Data atividade
    data_os = TextViewDesabilita((base_x + id_requisita.width + espacamento_x), base_y, texto="Data Final OS", dados=dados_caixas)
    data_os.text_view()

    # Estrutura
    estrutura = TextViewDesabilita((data_os.x + data_os.width + espacamento_x), base_y, width=140, texto="Estrutura", dados=dados_caixas)
    estrutura.text_view()

    # Alterando base Y para a proxima Linha de objetos
    base_y += espacamento_y

    # Assunto
    assunto = TextViewDesabilita(base_x, base_y, width=340, texto='Assunto', dados=dados_caixas)
    assunto.text_view()

    # Alterando base Y para a proxima Linha de objetos
    base_y += espacamento_y
    # Usuario
    usuario = TextViewDesabilita(base_x, base_y, width=160, texto='Usuario', dados=dados_caixas)
    usuario.text_view()
    usuario.set_var(user)

    # Data Registro
    data_registro = TextViewDesabilita((base_x + usuario.width + espacamento_x), base_y, width=160, texto='Data Registro', dados=dados_caixas)
    data_registro.text_view()

    lista_objetos.extend([dados_caixas, id_auditoria, retirante, id_requisita, data_os, estrutura, assunto, usuario, data_registro])
    # Material
    y = espacamento_y + base_y
    base_y = 40
    for i in range(13):
        if i < 5:
            material = ListaMaterial(x=base_x, y=y, texto=f'Material {i + 1}', dados=dados_caixas, lista=lista_material)
            y += espacamento_y
        else:
            base_x = 420
            material = ListaMaterial(x=base_x, y=base_y, texto=f'Material {i + 1}', dados=dados_caixas, lista=lista_material)
            base_y += espacamento_y
        lista_objetos.append(material)

    window.loop()


processo_interface()
