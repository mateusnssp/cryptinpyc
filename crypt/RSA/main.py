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



msg = str(input("Informe a mensagem: "))
msg_pre_criptografada = precrypt(list(msg), '../../precrypt/caracteres')


print(msg_pre_criptografada) #Imprimir



tamanho = len(msg_pre_criptografada)
lista_caracteres_criptografados = []
i = 0
for caractere_pre_criptografado in msg_pre_criptografada:

    lista_caracteres_criptografados.append(pow(caractere_pre_criptografado, key[4], mod=key[5]))




print(lista_caracteres_criptografados)

print(len(lista_caracteres_criptografados))