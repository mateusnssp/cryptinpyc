# own
from crypt.RSA.algo_class_RSA import *

def calculate_private_key(totiente, e):
    """
    Gerar chave privada
    """
    d = 0
    if (mod(d * e, totiente) != 1):
        d += 1
    return d

print(calculate_private_key(phi(2), generate_e()))
