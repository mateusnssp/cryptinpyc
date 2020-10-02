# Importações

#builtins
import os
from datetime import datetime
import platform

import random

# Own
import encrypt


# Configurações de endereços
sistema_operativo = platform.system()
separador_diretorios = None

if sistema_operativo == 'Windows':
    separador_diretorios = r'\\'
else:
    separador_diretorios = '/'


def criptografar(dado):
    criptografia = encrypt.RSA(dado)
    return criptografia.info()




def salvar(path, name_dir, escolha_aleatoria):

    """
    Esta função salva o conteúdo gerado.
    """

    # Nomeação do arquivo

    m1 = random.choice(list(range(90))) + random.choice(list(range(90)))
    m2 = random.choice(list(range(90))) + random.choice(list(range(90)))
    m3 = random.choice(list(range(90))) + random.choice(list(range(90)))
    m4 = random.choice(list(range(90))) + random.choice(list(range(90)))

    file_name = datetime.now()
    file_name = str(file_name)
    file_name = hex(int(file_name.replace('-', str(m1)).replace(':', str(m2)).replace(' ', str(m3)).replace('.', str(m4))))

    # Definição do nome do diretório
    if escolha_aleatoria == True:
        name_dir = file_name

    # Criação do diretório
    if path[-1] != separador_diretorios:
        os.mkdir(f'{path}{separador_diretorios}{name_dir}')
    else:
        os.mkdir(f'{path}{name_dir}')



if __name__ == '__main__':

    salvar('./', 'oi', False)


    # import console
    # console.exe_externo()






