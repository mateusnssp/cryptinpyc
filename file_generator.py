# Importações

import random
from datetime import datetime
import os




separador_diretorios = '/'


def write(conteudo, path, name_dir, escolha_aleatoria):
    """
    Esta função salva o conteúdo gerado.
    """

    # Tratamento do conteúdo
    conteudo_criptografado = str(conteudo[0])
    chave_publica = str((conteudo[1][2], conteudo[1][4]))
    chave_privada = str((conteudo[1][0], conteudo[1][1], conteudo[1][5]))



    # Nomeação do arquivo e do diretório
    m1 = random.choice(list(range(90))) + random.choice(list(range(90)))
    m2 = random.choice(list(range(90))) + random.choice(list(range(90)))
    m3 = random.choice(list(range(90))) + random.choice(list(range(90)))
    m4 = random.choice(list(range(90))) + random.choice(list(range(90)))

    file_name = datetime.now()
    file_name = str(file_name)
    file_name = hex(int(file_name.replace('-', str(m1)).replace(':', str(m2)).replace(' ', str(m3)).replace('.', str(m4))))

    if escolha_aleatoria:
        name_dir = file_name



    # Criação do diretório
    if path[-1] != separador_diretorios:
        os.mkdir(f'{path}{separador_diretorios}{name_dir}')
    else:
        os.mkdir(f'{path}{name_dir}')


    # Criação dos arquivos
    #  --> CONTEÚDO CRIPTOGRAFADO <--
    caminho_do_arquivo = f'{path}{separador_diretorios}{name_dir}/{file_name}'
    arquivo_conteudo = open(caminho_do_arquivo, 'w+')  # Criação

    arquivo_conteudo.write(f'{conteudo_criptografado}'.replace('[', '&').replace(']', '!').replace(',', 'x').replace(' ', ''))

    arquivo_conteudo.close()

    # --> CHAVE PÚBLICA <--
    caminho_do_arquivo = f'{path}{separador_diretorios}{name_dir}/pb'

    arquivo_key_pb = open(caminho_do_arquivo, 'w+')

    arquivo_key_pb.write(f'PB-{chave_publica.replace(", ", ">").replace("(", "").replace(")", "")}')

    arquivo_key_pb.close()

    # --> CHAVE PRIVADA <--
    caminho_do_arquivo = f'{path}{separador_diretorios}{name_dir}/pv'

    arquivo_key_pv = open(caminho_do_arquivo, 'w+')

    arquivo_key_pv.write(f'PV-{chave_privada.replace(", ", ">").replace("(", "").replace(")", "")}')

    arquivo_key_pv.close()





def read():
    pass