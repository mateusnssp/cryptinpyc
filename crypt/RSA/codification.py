# Importações:
import random
from calc.mod_inverse import modinv
from calc.mdc import mdc



def key():
    #################################################################################################
    #Escolha de forma aleatória dois números primos grandes p e q
    #################################################################################################

    # Abrir lista dos números primos:
    file = open('../../.glp/lp.txt')

    # Definição da vairável que suportará a lista dos números primos:
    lp = []
    # Atribuir números primos para lp (transporte para o programa)
    for item in range(7287):
        i = file.readline()
        lp.append(int(i))

    # Definição das variáveis
    p, q, p_diferente_q = None, None, False

    # Garantir que p seja diferente de q:
    while not p_diferente_q:
        if p == q:
            p, q = random.choice(lp), random.choice(lp)
        else:
            p_diferente_q = True

    # Fechar a lista dos números primos
    file.close()


    #################################################################################################
    #Computar n = p * q
    #################################################################################################

    n = p * q


    #################################################################################################
    #Computart phi(n) = (p - 1)*(q - 1)
    #################################################################################################

    phi = (p - 1) * (q - 1)

    #################################################################################################
    #Escolha um inteiro  "e"  , 1 < "e" < phi(n) ,  "e" e phi(n) sejam primos entre si.
    #################################################################################################

    E_NO_OK = True
    while E_NO_OK:
        def generate_E(num):
            def mdc(n1, n2):
                rest = 1
                while n2 != 0:
                    rest = n1 % n2
                    n1 = n2
                    n2 = rest
                return n1

            while True:
                E = random.randrange(2, num)
                if mdc(num, E) == 1:
                    return E

        e = generate_E(random.choice(lp))
        if mdc(phi, e) == 1:
            E_NO_OK = False
            print(e)
        else:
            E_NO_OK = True


    #################################################################################################
    # Calcular d --> d seja inverso multiplicativo de e.
    #################################################################################################



    d = modinv(e, phi)


    print(f'p: {p}\nq: {q}\nn = p * q: {n}\nphi = (p - 1) * (q - 1): {phi}\ne: {e}\nd: {d}')



    return [p, q, n, phi, e, d]


if __name__ == '__main__':

    loop = True
    while loop:
        try:
            print(key())
            loop = False
        except:
            print('err!')
            loop = True
