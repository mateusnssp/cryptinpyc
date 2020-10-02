# Importações

#builtins
import os
from datetime import datetime


# Own
import encrypt

def criptografar(dado):
    criptografia = encrypt.RSA(dado)
    return criptografia.info()



#CRIAÇÃO DO DIRETÓRIO

def criar_diretorio(path):



    # Nomeação do arquivo

    name_file = datetime.now()
    name_file = str(name_file)
    name_file = hex(int(name_file.replace('-', '0').replace(':', '4').replace(' ', '5').replace('.', '7')))

    return name_file
    # os.mkdir(path + name_dir)



if __name__ == '__main__':

    name_file = criar_diretorio('./')
    print(name_file)


    # import console
    # console.exe_externo()






