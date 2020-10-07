# Importações
# Builtins
import random
# OWn
import calc

"""
(AS CHAVES DEVEM SEGUIR ESTE PADRÃO)
pb --> n, e
pv --> p, q, d

"""


class Keys:
    """
    Os componentes construtores da classe foram divididos em tipos:
        - Variáveis de cálculo
            Variáveis pseudoaleatorias --> (p, q, e) [Variáveis base, geradas pelo computador]
            Variáveis de calculo --> (n, phi, d) [Variáveis derivadas das variáveis base, geradas conforme funções]

        - Variáveis de retorno (resultados)
            Chaves --> (pb, pv) [Conjunto das variáveis de cálculo]
    """

    def __init__(self):
        self.variaveisPseudoaleatorias = self.gerar_variaveis_pseudoaleatorias()
        self.variaviesDeCalculo = self.calcular_vairaveis_de_calculo(self.variaveisPseudoaleatorias[0],
                                                                     self.variaveisPseudoaleatorias[1],
                                                                     self.variaveisPseudoaleatorias[2])
        self.pb = self.g_pb(self.variaviesDeCalculo[0], self.variaveisPseudoaleatorias[2])
        self.pv = self.g_pv(self.variaveisPseudoaleatorias[0], self.variaveisPseudoaleatorias[1],
                            self.variaviesDeCalculo[2])

    @staticmethod
    def gerar_variaveis_pseudoaleatorias():

        # Definição de variáveis
        p, q, p_diferente_q = None, None, False
        tamanho_da_linha = 7  # todas as linhas do arquivo lp.txt tem 7 bytes (contando com os \n)
        quantidade_de_linhas = 41637

        caminhoBancoDeDados = '../.glp/lp.txt' if __name__ == '__main__' else '../.glp/lp.txt'

        with open(caminhoBancoDeDados) as bd:

            # (p, q)
            while not p_diferente_q:  # Garantir que p e q sejam diferentes
                if p == q:
                    # Escolha de p
                    linha_p = random.choice(range(quantidade_de_linhas))  # sorteio da linha
                    bd.seek(0, 0)  # Redefinição
                    bd.seek(tamanho_da_linha * linha_p)  # posicionamento na linha escolhida

                    p = int(bd.readline())

                    # Escolha de q
                    linha_q = random.choice(range(quantidade_de_linhas))  # sorteio da linha
                    bd.seek(0, 0)  # Redefinição
                    bd.seek(tamanho_da_linha * linha_q)  # posicionamento na linha escolhida

                    q = int(bd.readline())
                else:
                    p_diferente_q = True

            # (e)
            e = calc.gerar_e((p - 1) * (q - 1))  # argumento equivalente a phi.

        return p, q, e

    @staticmethod
    def calcular_vairaveis_de_calculo(p, q, e):
        n = calc.n(p, q)
        phi = calc.phi(p, q)
        d = calc.modinv(e, phi)
        return n, phi, d

    @staticmethod
    def g_pb(n, e):
        return n, e

    @staticmethod
    def g_pv(p, q, d):
        return p, q, d


if __name__ == '__main__':
    test = Keys()
    print(f'(p, q, e)..........: {test.variaveisPseudoaleatorias}')
    print(f'(n, phi, d)........: {test.variaviesDeCalculo}')
    print(f'(n, e).............: {test.pb}')
    print(f'(p, q, d)..........: {test.pv}')
