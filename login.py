from tkinter import messagebox
import pandas as pd
import subprocess
from janela import *
from caixa_texto import *


def valida():
    if user.var_str.get() in list(verifica['user']):
        localiza = list(verifica['user']).index(user.var_str.get())
        teste = senha.var_str.get() == verifica['senha'][localiza]
        nome = verifica['nome'][localiza] if teste else "Não informado"
        muda_processo(login, nome) if teste else exibir_alerta('Senha Invalida!', 'Digite a senha correta, para iniciar.')

    else:
        exibir_alerta(msg="Usuario e senha não identificados")


def exibir_alerta(title='Alerta', msg="Esta é uma mensagem de alerta!"):
    messagebox.showinfo(title=title, message=msg)


def fun_senha():
    senha.text['show'] = "" if (senha.text['show'] == "*") else "*"


def muda_processo(janela, usuario=""):
    subprocess.Popen(['python', 'interface.py', usuario])
    janela.finaliza()


# Importando dados planilha
verifica = pd.read_excel(r'tabelas\login.xlsx', sheet_name='Usuarios')


# Abrindo Janela
login = Janela(200, 200, 'Login')
login.janela()
# login.center_windows()

# Caixa de texto com dados do usuario
user = TextLogin(x=25, y=30, width= 150, texto='Usuario')
user.text_view()

# Informando a senha
senha = TextLogin(x=25, y=90, width=150, texto="Senha", show = "*")
senha.text_view()

# Botão Senha
btt_senha = Button(text="!", command= fun_senha)
btt_senha.place(x= 150, y= 90, width=25, height= 20)
btt_senha.bind("<Return>", lambda event: fun_senha())

# Botão de acesso LOGIN
btt_login = Button( text= "LOGIN", command=valida)
btt_login.place(width= 100, height= 25, x= 50, y= 150)
btt_login.bind("<Return>", lambda event: valida())

# Loop da janela
login.loop()

