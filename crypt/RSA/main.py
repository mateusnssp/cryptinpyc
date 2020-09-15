
# Own
import precrypt.precrypt
from crypt.RSA.codification import *



while True:
    conteudo_precrypt = precrypt.precrypt.precrypt(list(input('str: ')), '../../precrypt/caracteres')

    print(codification(conteudo_precrypt))
    print(f'Chave PÚBLICA: (n,e) = ({encryption_key[0]}, {e})')
    print(f'CHAVE PRIVADA: (p, q, d) = ({encryption_key[1][0]}, {encryption_key[1][1]}, {"d"})')