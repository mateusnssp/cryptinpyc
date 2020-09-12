# Importações builtins
from random import choice


# Own

import crypt.RSA.generate_encryption_key
encryption_key = crypt.RSA.generate_encryption_key.generate_encryption_key()


e = choice(range(100, 999))
def codification(precrypt):

    # Escolher expoente e aleatório:


    c = []
    # transformar cada item pré-criptografado criptografando-os:
    for i in precrypt:
        caractere_in_c = (i**e)%encryption_key[0]
        c.append(caractere_in_c)
    return c
