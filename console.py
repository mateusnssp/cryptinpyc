# Importações
# Builtins
from datetime import datetime

# Own
from RSA import main

def receber_comando(): return input('cryptinpyc >>> ')


def receber_parametro(): return input('[] >>> ')


def init():
    data = str(datetime.today())
    data = data[11:27]
    # Definição saudação
    if 7 <= int(data[0:2]) < 12:
        cumprimento = 'Bom dia!'
    elif 12 <= int(data[0:2]) < 18:
        cumprimento = 'Boa tarde!'
    elif 18 <= int(data[0:2]) <= 24 or 0 <= int(data[0:2]) < 7:
        cumprimento = 'Boa noite!'
    else:
        cumprimento = 'Olá'

    # Saudação
    space = 30
    print(f'{data.center(space, ".")}\n{"cryptinpyc".center(space)}\n{cumprimento.center(space)}\n{"." * space}\n')


def ajuda():
    space = 13
    print(
        f'\n{"- e".ljust(space)}para criptografar\n{"- d".ljust(space)}para decodificar\n{"- quit".ljust(space)}para sair\n{"- help".ljust(space)}para ajuda\n')



def encrypt():
    pass


def decrypt():
    pass


# Inicialização
def __init__():
    print('"help" para ajuda\n')

    # Loop entrada-retorno
    while True:
        comando = receber_comando()
        if comando.upper() == 'HELP':
            ajuda()

        if comando.upper() == 'EXIT' or comando == 'QUIT':
            break


if __name__ == '__main__':
    __init__()
