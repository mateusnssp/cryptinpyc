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
    def criptografar(chave_pb, dadoPreCriptografado):
        """
        pow(caractere, e, mod=n)
        """
        dadoCriptografado = []
        for caractere in dadoPreCriptografado:
            caractereCriptografado = pow(caractere, chave_pb[1], mod=chave_pb[0])
            dadoCriptografado.append(caractereCriptografado)
        return dadoCriptografado


class Decrypt:

    def __init__(self, pv, dado):
        self.pv = pv
        self.dado = dado

        self.dadoDecodificado = self.decodificar(self.pv, self.dado)
        self.dadoLegivel = self.pre_decodificar(self.dadoDecodificado)

    @staticmethod
    def decodificar(chave_pv, dadoCriptografado):
        """
        pow(caractere, d, mod=n
        """
        n = chave_pv[0] * chave_pv[1]
        dadoDecodificado = []
        for caractere in dadoCriptografado:
            caractereDecodificado = pow(caractere, chave_pv[2], mod=n)
            dadoDecodificado.append(caractereDecodificado)
        return dadoDecodificado

    @staticmethod
    def pre_decodificar(dado): return pre.conversion.de_precrypt(dado)


if __name__ == '__main__':
    """
    variáveis aleatórias --> (p, q) = (5, 7)
    chave pb --> (n, e) = (35, 7)
    cahve pv --> (p, q, d) = (5, 7, 7)
    
    Criptografia:
    dado legível --> ['\n']
    pré-codificação --> [27, 28, 10]
    dado codificado --> [13, 7, 10]
    
    Decodificação:
    dado codificado --> [13, 7, 10]
    pré-codificação --> [27, 28, 10]
    dado decodificado / legível --> ['\n']
    """

    testeCriptografar = Encrypt((35, 7), 'oi')
    print(testeCriptografar.dadoPreCriptografado)
    print(testeCriptografar.dadoCriptografado)

    testeDecodificar = Decrypt((5, 7, 7), [6, 0])
    print(testeDecodificar.dadoDecodificado)
    print(testeDecodificar.dadoLegivel)
