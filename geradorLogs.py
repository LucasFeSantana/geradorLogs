import os
from datetime import date, datetime

def criaLog():
    caminho = ""
    try:
        if os.path.exists(caminho):
            return f'o log já existe'
    except Exception as e:
        return f'Ocorreu um erro inesperado: {e}'
    else:
        with open(caminho,'w',encoding='UTF-8') as log:
            log.write(f'Início do Log\nDia de referência: {date.today()}')
        print('Log criado com êxito em '+caminho)
        return caminho