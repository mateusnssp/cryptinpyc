# Importações
# Builtins
from datetime import *
import platform

# Own
import main

# configurações de interface e informações básicas

# Sistema operativo
sistema_operativo = platform.system()

# Cumprimentos
time = str(datetime.now())
time = int(time[11:13])

if 5 <= time < 12:
    greeting = 'Bom dia!'
if 12 <= time < 18:
    greeting = 'Boa tarde!'
if 0 <= time < 5 or 18 <= time <= 24:
    greeting = 'Boa noite!'
# else:
#     greeting = "Olá"


# Definição das cores.
if sistema_operativo == 'Linux':
    color_open = {'verde': '\33[92m'}
    color_close = {'verde': '\33[m'}
else:
    color_open = {'verde': ''}
    color_close = {'verde': ''}

# Atributos do console
espera_parametro = '[] >>> '
espera_comando = '[cryptinpyc] >>> '

# Configuráveis:
if sistema_operativo == 'Windows':
    standart = input("Defina um diretório padrão")
else:
    standart = './'


def parametro():
    return input(f'{color_open["verde"]}{espera_parametro}{color_close["verde"]}')


def comando():
    return input(f'{color_open["verde"]}{espera_comando}{color_close["verde"]}')


def ajuda_console():
    print('Ajuda')


# INICIALIZAÇÃO
print(
    f'\n\n{color_open["verde"]}. . . cryptinpyc . . .\n{str(datetime.now())[0:22]}\n{greeting.center(22, " ")}\n......................{color_close["verde"]}\n\n\n"h" para ajuda;\n"e" para criptografar\n"d" para descriptografar\n"c" para configurar\n\n')

console_running = True
while console_running:

    command = comando()

    if command.upper() == 'H':
        ajuda_console()

    if command.upper() == 'E':
        print('\n:::Informe os dados a serem criptografados:::')
        dado = parametro()
        conteudo = main.criptografar(dado)

        print('\n:::Deseja exibir o conteúdo gerado? [Y/N]:::')
        resposta_exibir_conteudo_gerado = parametro()
        if resposta_exibir_conteudo_gerado.upper() == 'Y':
            print(conteudo[0])
        if resposta_exibir_conteudo_gerado.upper() == 'N':
            pass

        # SALVAR CONTEÚDO

        print(
            '\n:::Caso queira, especifique um caminho para salvar ou cancele com "cancel":::\n:::Pressione enter para salvar no diretório padrão:::')
        path = parametro()

        if path.upper() == 'CANCEL':
            continue
        if path.upper() == '':
            path = standart
        else:
            pass

        print(path)

        print(
            '\n:::Especifique um nome para o diretório dos arquivos ou pressione enter para escolha pseudoaleatoria [protocolo de anonimidade]:::')
        name_dir = parametro()

        if name_dir == '':
            escolha_aleatoria = True
            name_dir = None

        else:
            escolha_aleatoria = False

        main.salvar(conteudo[1], path, name_dir, escolha_aleatoria)

    if command.upper() == 'D':
        pass

    if command.upper() == 'EXIT' or command.upper() == 'QUIT':
        exit()

if __name__ != '__main__':
    def exe_externo():
        print('\nC O N S O L E  I N I C I A L I Z A D O')
