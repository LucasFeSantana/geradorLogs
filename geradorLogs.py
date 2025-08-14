import os
from datetime import datetime
def criaPastaLogs():
    'Valida a existência de uma pasta Logs e a cria em caso negativo'
    try:
        if os.path.exists('.\\logs'):
            print('Pasta Logs Já existente')
            return True
        else:
            os.mkdir('logs')
            print('Pasta criada com êxito')
            return True
    except Exception as e:
        msg = f'Ocorreu um erro inesperado: {e}'
        print(msg)
        return False
def criaLog():
    'Cria um arquivo de texto nomeado com a data atual precedido do prefixo "LOG-" retornando True ou False dependendo de seu êxito'
    pastaLogs = criaPastaLogs()
    caminho = f".\\logs\\LOG-{datetime.now().strftime('%d%m%Y')}.txt"
    try:
        if pastaLogs == True:
            if os.path.exists(caminho):
                print('O Log já existe')
                return False
            else:
                with open(caminho,'w',encoding='UTF-8') as log:
                    log.write(f'Início do Log\nData de referência: {datetime.now().strftime('%d/%m/%Y')}')
                print('Log criado com êxito em '+caminho)
                return True
        else:
            print(f'Não foi possível criar o diretório de destino dos Logs\nVerifique seus acesso a pasta {os.getcwd()}')
            return False
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')
        return False