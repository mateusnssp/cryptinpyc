# Importações builtins
from random import choice


# Own
import precrypt.precrypt
import crypt.RSA.generate_encryption_key



encryption_key = crypt.RSA.generate_encryption_key.generate_encryption_key()

def codification(precrypt):

    # Escolher expoente e aleatório:
    e = choice(range(100, 999))


    c = []
    # transformar cada item pré-criptografado criptografando-os:
    for i in precrypt:
        caractere_in_c = (i**e)%encryption_key
        c.append(caractere_in_c)

    return c


if __name__ == '__main__':
    print(codification(conteudo_precrypt))