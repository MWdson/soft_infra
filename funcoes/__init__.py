import pandas as pd
import pytz
import requests
import json
from datetime import datetime


token = 'MjI2OjdkMzQ0YzZkNzE4MWE3NDdhNzYxNGY0M2NlN2FkMjIyODQ3NmYwM2M2NmYxMDM2OTEyYjUyNWI2YTNlMTE1NTc='


def req_os(text_os: str):
    url = 'https://gestao.estrelasinternet.com.br/webservice/v1/su_oss_chamado'
    headers = {"ixcsoft": "listar", "Authorization": "Basic {}".format(token), "Content-Type": "application/json"}
    payload = json.dumps({
        "qtype": "su_oss_chamado.id",
        "query": text_os,
        "oper": "=",
        "rp": "12",
        "sortname": "su_oss_chamado.data_fechamento",
        "sortorder": "asc",
    })
    response = requests.get(url, headers=headers, data=payload)
    lista = json.loads(response.text)
    return pd.DataFrame(lista['registros'])


def data_pt_br(data_os):
    data = datetime.strptime(data_os, "%Y-%m-%d %H:%M:%S")
    data_ptbr = datetime.strftime(data, "%d/%m/%Y %H:%M:%S")
    return data_ptbr


def data_agora():
    zona = pytz.timezone("Brazil/East")
    agora = datetime.now(zona)
    return datetime.strftime(agora,"%d/%m/%Y %H:%M:%S")


def assunto_api(pasta: str, busca_id: str):
    url = 'https://gestao.estrelasinternet.com.br/webservice/v1/{}'.format(pasta)
    headers = {"ixcsoft": "listar", "Authorization": "Basic {}".format(token), "Content-Type": "application/json"}
    payload = json.dumps({
        'qtype': '{}.id'.format(pasta),
        'query': '{}'.format(busca_id),
        'oper': '=',
        'rp': '1050',
        'page': '1',
        'sortname': '{}.id'.format(pasta),
        'sortorder': 'asc'
    })
    response = requests.get(url, headers=headers, data=payload)
    lista = json.loads(response.text)
    return pd.DataFrame(lista['registros'])


def verifica_numero(numero: str):
    if numero.isnumeric():
        return True
    else:
        return False


def material(pasta="produtos"):
    url = 'https://gestao.estrelasinternet.com.br/webservice/v1/{}'.format(pasta)
    headers = {"ixcsoft": "listar", "Authorization": "Basic {}".format(token), "Content-Type": "application/json"}
    payload = json.dumps({
        "qtype": "{}.id".format(pasta),
        "query": "0",
        "oper": ">",
        "rp": "2500",
        "sortname": "{}.id".format(pasta),
        "sortorder": "asc",
        "grid_param": '[{"TB": "produtos.id_sub_grupo", "OP": ">=", "P": "25"},{"TB": "produtos.id_sub_grupo", "OP": "<=", "P": "26"},{"TB":"produtos.ativo", "OP":"=", "P":"Sim"}]'
    })
    response = requests.get(url, headers=headers, data=payload)
    lista = json.loads(response.text)
    return pd.DataFrame(lista['registros'])


def fun_estrutura(id_estrutura="0"):
    try:
        pasta = "estrutura"
        url = 'https://gestao.estrelasinternet.com.br/webservice/v1/{}'.format(pasta)
        headers = {"ixcsoft": "listar", "Authorization": "Basic {}".format(token), "Content-Type": "application/json"}
        payload = json.dumps({
            "qtype": "{}.id".format(pasta),
            "query": "{}".format(id_estrutura),
            "oper": "=",
            "rp": "2500",
            "sortname": "{}.id".format(pasta),
            "sortorder": "asc",
            })
        response = requests.get(url, headers=headers, data=payload)
        lista = json.loads(response.text)
        estrutura_dados = pd.DataFrame(lista['registros'])
        return estrutura_dados['descricao'][0]
    except:
        return "Erro!"

