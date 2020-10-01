# IMPORTAÇÕES


# Own
from precrypt.precrypt import *
from crypt.RSA.codification import key

"""
___REGRAS GERASI DE LÓGICA DE CRIPTOGRAFIA___

    1 --> Classe é definida como o conjunto de dados trabalhados, incluindo dados pre-criptografados, dados criptografados e chaves.

    2 --> Toda classe, deve conter um dado legível, com:
        -- Um par de chaves completo, contendo:
                -- Uma chave correspondente pública;
                -- Uma chave correspondente privada.
        -- Um dado correspondente pre-criptografado;
        -- Um dado correspondente criptografado.



"""


class RSA:

    def __init__(self, dado_legivel):
        """
        Função construtora define as variáveis em ordem algorítmica para se adequar com a regra 1.
        """

        self.caracteres_para_chaves_de_preCriptografia = './precrypt/caracteres'  # Caminho para caracteres,

        self.key = key()  # Definição das chaves (p, q, n, phi, e, d)

        self.dado_legivel = dado_legivel

        self.dado_preCriptografado = self.pre_criptografar(dado_legivel)
        self.dado_criptografado = self.criptografar(self.dado_preCriptografado)


    def pre_criptografar(self, dado):
        return precrypt(list(dado), self.caracteres_para_chaves_de_preCriptografia)

    def criptografar(self, dado):
        dado_criptografado = []
        for caractere in dado:
            caractere_criptografado = pow(caractere, self.key[4], mod=self.key[5])  # pow(caractere, e, mod=d)
            dado_criptografado.append(caractere_criptografado)

        return dado_criptografado

    def info(self):

        return f'CHAVE COMPLETA............................: {f"(p, q, n, phi, e, d) = {self.key}"}\nCHAVE PÚBLICA.............................:\33[m {f"(n, e) = {self.key[2], self.key[4]}"}\nCHAVE PRIVADA.............................:\33[m {f"(p, q, d) = {self.key[0], self.key[1], self.key[5]}"}\nDADO PRE-CRIPTOGRAFADO:...................:\33[m {self.dado_preCriptografado}\nDADO CRIPTOGRAFADO........................:\33[m {self.dado_criptografado}\nTAMANHO:..................................:\33[m {len(self.dado_legivel)}'



if __name__ == '__main__':
    test = RSA('mmmm')
    print(test.dado_criptografado)
    print(test.info())
