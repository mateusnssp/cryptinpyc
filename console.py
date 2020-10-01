# Importações
# Builtins
from datetime import *
import platform


#configurações de interface e informações básicas

time = str(datetime.now())
time = int(time[11:13])

if 5 <= time < 12:
    greeting = 'Bom dia!'
if 12 <= time < 18:
    greeting = 'Boa tarde!'
if 0 <= time < 5 or 18 <= time <= 24:
    greeting = 'Boa noite!'
else:
    greeting = "Olá"


# Definição das cores.
if platform.system() == 'Linux':
    color_open = {'verde': '\33[92m'}
    color_close = {'verde': '\33[m'}
else:
    color_open = {'verde': ''}
    color_close = {'verde': ''}




# Atributos do console
espera_parametro = '[] >>> '
espera_comando = '[cryptinpyc] >>> '


def parametro():
    return input(espera_parametro)

def comando():
    return input(f'{color_open["verde"]}{espera_comando}{color_close["verde"]}')


def ajuda_console():
    print('Ajuda')




# INICIALIZAÇÃO
print(f'\n\n{color_open["verde"]}. . . cryptinpyc . . .\n{str(datetime.now())[0:22]}\n{greeting.center(22, " ")}\n......................{color_close["verde"]}\n\n\n"h" para ajuda;\n"e" para criptografar\n"d" para descriptografar\n\n')


console_running = True
while console_running:

    command = comando()

    if command.upper() == 'H':
        ajuda_console()

    if command.upper() == 'E':
        pass

    if command.upper() == 'D':
        pass

    if command.upper() == 'EXIT' or command.upper() == 'QUIT':
        exit()


