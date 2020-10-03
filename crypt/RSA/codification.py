# Importações:
import random
from calc.mod_inverse import modinv
from calc.mdc import mdc


def key():

    """
    PROCESSO DE GERAÇÂO DE CHAVE:
        - Escolha de forma aleatória dois números primos grandes p e q;
        - Computar n = p * q;
        - Computar phi(n) = (p - 1)*(q - 1);
        - Escolher um inteiro  "e"  , 1 < "e" < phi(n) ,  "e" e phi(n) sejam primos entre si;
        - Calcular d --> d seja inverso multiplicativo de e.

        ::return [p, q, n, phi, e, d]::
    """

    # Abrir lista dos números primos:
    # ../../.glp/lp.txt  -->  Endereço para teste
    # ./.glp/lp.txt      -->  Endereço para main
    if __name__ == '__main__':
        file = open('../../.glp/lp.txt')
    else:
        file = open('./.glp/lp.txt')

    # Definição das variáveis
    p, q, p_diferente_q = None, None, False

    tamanho_da_linha = 7  # todas as linhas do arquivo lp.txt tem 7 bytes (contando com os \n)
    quantidade_de_linhas = 41637

    # Garantir que p seja diferente de q:
    while not p_diferente_q:
        if p == q:

            # Escolha de p
            linha_p = random.choice(range(quantidade_de_linhas))  # sorteio da linha
            file.seek(0, 0)  # Redefinição
            file.seek(tamanho_da_linha * linha_p)  # posicionamento na linha escolhida

            p = int(file.readline())

            # Escolha de q
            linha_q = random.choice(range(quantidade_de_linhas))  # sorteio da linha
            file.seek(0, 0)  # Redefinição
            file.seek(tamanho_da_linha * linha_q)  # posicionamento na linha escolhida

            q = int(file.readline())
        else:
            p_diferente_q = True

    # Fechar a lista dos números primos
    file.close()



    n = p * q




    phi = (p - 1) * (q - 1)




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



        # Abrir lista dos números primos:
        # ../../.glp/lp.txt  -->  Endereço para teste
        # ./.glp/lp.txt      -->  Endereço para main
        if __name__ == '__main__':
            file = open('../../.glp/lp.txt')
        else:
            file = open('./.glp/lp.txt')

        linha_e = random.choice(range(quantidade_de_linhas))  # sorteio da linha
        file.seek(0, 0)  # Redefinição
        file.seek(tamanho_da_linha * linha_e)  # posicionamento na linha escolhida

        e_beta = int(file.readline())

        e = generate_E(e_beta)

        # Fechar a lista dos números primos
        file.close()

        if mdc(phi, e) == 1:
            E_NO_OK = False

        else:
            E_NO_OK = True




    d = modinv(e, phi)

    return [p, q, n, phi, e, d]


if __name__ == '__main__':
    lista = key()

    print(
        f'p.....: {lista[0]}\nq.....: {lista[1]}\nn.....: {lista[2]}\nphi...: {lista[3]}\ne.....: {lista[4]}\nd.....: {lista[5]}')
