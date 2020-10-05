# IMPORTAÇÕES


# Own
import pre.conversion

"""
___REGRAS GERASI DE LÓGICA DE CRIPTOGRAFIA___

    1 --> Classe é definida como o conjunto de dados trabalhados, incluindo dados pre-criptografados, dados criptografados e chaves.

    2 --> Toda classe, deve conter um dado legível, com:
        -- Um par de chaves completo, contendo:
                -- Uma chave correspondente pública;
                -- Uma chave correspondente privada.
        -- Um dado correspondente pre-criptografado;
        -- Um dado correspondente criptografado.



preCodificação = [27, 28, 10]

"""


class Encrypt:

    def __init__(self, pb, dado):
        self.pb = pb
        self.dado = dado

        self.dadoPreCriptografado = self.pre_criptografar(self.dado)
        self.dadoCriptografado = self.criptografar(self.pb, self.dadoPreCriptografado)

    @staticmethod
    def pre_criptografar(dado): return pre.conversion.precrypt(dado)

    @staticmethod
    """
    pow(caractere, e, mod=n)
    """
    def criptografar(chave_pb, dadoPreCriptografado):
        dadoCriptografado = []
        for caractere in dadoPreCriptografado:
            caractereCriptografado = pow(caractere, chave_pb[1], mod=chave_pb[0])
            dadoCriptografado.append(caractereCriptografado)
        return dadoCriptografado






if __name__ == '__main__':

    """
    Teste criptografia
    variáveis aleatórias --> (p, q) = (5, 7)
    chave pb --> (n, e) = (35, 7)
    dado legível --> ['\n']
    pré-codificação --> [27, 28, 10]
    dado codificado --> [13, 7, 10]
    """
    test = Encrypt((35, 7), '\n')
    print(test.dadoPreCriptografado)
    print(test.dadoCriptografado)


