# Importações
# Builtins
from datetime import *
import platform

# Own
import main

#configurações de interface e informações básicas

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
standart = './'


def parametro():
    return input(f'{color_open["verde"]}{espera_parametro}{color_close["verde"]}')

def comando():
    return input(f'{color_open["verde"]}{espera_comando}{color_close["verde"]}')


def ajuda_console():
    print('Ajuda')




# INICIALIZAÇÃO
print(f'\n\n{color_open["verde"]}. . . cryptinpyc . . .\n{str(datetime.now())[0:22]}\n{greeting.center(22, " ")}\n......................{color_close["verde"]}\n\n\n"h" para ajuda;\n"e" para criptografar\n"d" para descriptografar\n"c" para configurar\n\n')


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
            print(conteudo)
        if resposta_exibir_conteudo_gerado.upper() == 'N':
            pass


        print('\n:::Caso queira, especifique um caminho para salvar ou cancele com "cancel":::\n:::Pressione enter para salvar no diretório padrão:::')
        file_name = parametro()

        if file_name.upper() == 'CANCEL':
            continue
        if file_name.upper() == '':
            file_name = standart
        else:
            pass

        print(file_name)

        print('\n:::Especifique um nome para o diretório ou pressione enter para escolha aleatória [protocolo de anonimidade]:::')
        name_dir = parametro()


        if name_dir == '':
            pass
        else:
            pass












    if command.upper() == 'D':
        pass

    if command.upper() == 'EXIT' or command.upper() == 'QUIT':
        exit()



















if __name__ != '__main__':

    def exe_externo():
        print('\nC O N S O L E  I N I C I A L I Z A D O')


