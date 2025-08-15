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
def criaLogVazio():
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
                    log.write(f'Início do Log\nData de referência: {datetime.now().strftime('%d/%m/%Y')}\n\n')
                print('Log criado com êxito em '+caminho)
                return True
        else:
            print(f'Não foi possível criar o diretório de destino dos Logs\nVerifique seus acesso a pasta {os.getcwd()}')
            return False
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')
        return False
def geraLog(registro:str):
    'Armazena os dados passados como parâmetro dentro de um arquivo LOG.'
    caminho = f".\\logs\\LOG-{datetime.now().strftime('%d%m%Y')}.txt"
    if registro == None:
        print('A operação exige o parâmetro dados do tipo String')
        return False
    else:
        try:
            if os.path.exists(caminho):
                with open(caminho, 'a',encoding='UTF-8') as log:
                    log.write(f"\n{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n{registro}\n")
                return True
            else:
                criaLogVazio()
                with open(caminho, 'a',encoding='UTF-8') as log:
                    log.write(f"\n{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n{registro}\n")
                return True
        except Exception as e:
            print(f'Ocorreu um erro inesperado: {e}')
            return False