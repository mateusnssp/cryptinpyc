# Importações
# Builtins
from datetime import datetime

# Own

import RSA.main as principal
import gfile

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
    print(f'\n{"- e".ljust(space)}para criptografar\n{"- d".ljust(space)}para decodificar\n{"- quit".ljust(space)}para sair\n{"- help".ljust(space)}para ajuda\n')










def encrypt():
    print(':::Informe os dados a serem criptografados ou especifique o caminho de um arquivo com "$" antes')
    dado = receber_parametro()
    dado = dado.lstrip()

    if dado[0] == '$':
        print("Caminho")

    else:
        e = principal.RSA()

        dadoCriptografado = e.encrypt(dado)
        pb = e.pb
        pv = e.pv

        print(":::Deseja exibir dados gerados?::: (Y/N)")
        resposta = receber_parametro()
        if resposta.upper() == 'Y':
            print(f'DADO CRIPTOGRAFADO................: {dadoCriptografado}\nCHAVE PÚBLICA.....................: (n, e) = {pb}\nCHAVE PRIVADA.....................: (p, q, d) = {pv}')

            print(":::Informe o caminho para salvar o conteúdo:::")
            path = receber_parametro()

            file =  gfile.File(pb, pv, dadoCriptografado, path)



        else:
            pass







def decrypt():
    print('D')
























# Inicialização
def init():
    print('"help" para ajuda\n')

    # Loop entrada-retorno
    while True:
        comando = receber_comando()
        if comando.upper() == 'HELP':
            ajuda()

        elif comando.upper() == 'E' or comando == 'e':
            encrypt()

        elif comando.upper() == 'D' or comando == 'd':
            decrypt()

        elif comando.upper() == 'EXIT' or comando.upper() == 'QUIT':
            break

        else:
            print('Comando não reconhecido')



if __name__ == '__main__':
    # Saudação
    space = 30
    print(f'{data.center(space, ".")}\n{"cryptinpyc".center(space)}\n{cumprimento.center(space)}\n{"." * space}\n')
    init()
