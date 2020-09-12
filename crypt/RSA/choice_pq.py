"""
Escolher número primo aleatório.
"""

# Importações:
import random

def choice_pq():

    """"
    main function
    """

    # Abrir lista dos números primos:
    file = open('../../.glp/lp.txt')


    # Definição da vairável que suportará a lista dos números primos:
    lp = []
    # Atribuir números primos para lp (transporte para o programa)
    for i in range(6772):
        i = file.readline()
        lp.append(int(i))



    # Definição das variáveis
    p, q, p_diferente_q = None, None, False




    # Garantir que p seja diferente de q:
    while not p_diferente_q:
        if p == q:
            p, q = random.choice(lp) , random.choice(lp)
        else:
            p_diferente_q = True



    # Fechar a lista dos números primos
    file.close()

    return [p, q]


if __name__ == '__main__':
    print(choice_pq())