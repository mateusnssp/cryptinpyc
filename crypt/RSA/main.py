
from precrypt.precrypt import *
from crypt.RSA.codification import key

loop = True
while loop:
    try:
        chave = key()
        print(chave)
        loop = False
    except:
        loop = True

key = key()



msg = str(input("\33[32mINFORME A MENSAGEM...............:\33[m ")) ###RECEBER A MENSAGEM


#PRE CRIPTOGRAFAR
msg_pre_criptografada = precrypt(list(msg), '../../precrypt/caracteres')





lista_caracteres_criptografados = []
i = 0
for caractere_pre_criptografado in msg_pre_criptografada:

    lista_caracteres_criptografados.append(pow(caractere_pre_criptografado, key[4], mod=key[5]))





repetir_pergunta_visualizar = True
while repetir_pergunta_visualizar:
    visualizar = input('\33[37mDESEJA VIZUALIZAR O CONTEÚDO GERADO? (Y/N): \33[m')
    print()
    if visualizar.upper() == 'Y':
        print(f'\33[92mMENSAGEM PRE-CRIPTOGRAFADA:......:\33[m {msg_pre_criptografada}')
        print(f'\33[92mMENSAGEM CRIPTOGRAFADA...........:\33[m {lista_caracteres_criptografados}')
        print(f'\33[92mTAMANHO:.........................:\33[m {len(lista_caracteres_criptografados)}')
        repetir_pergunta_visualizar = False
    else:
        if visualizar.upper() == 'N':
            repetir_pergunta_visualizar = False
            pass
        else:
            print("\33[31mOPÇÃO DESCONHECIDA, RESPONDA NOVAMENTE.\33[m")


