
# Own
from crypt.RSA.codification import *
while True:
    conteudo_precrypt = precrypt.precrypt.precrypt(list(input('str: ')), '../../precrypt/caracteres')

    print(codification(conteudo_precrypt))
