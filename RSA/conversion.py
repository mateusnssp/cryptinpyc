# IMPORTAÇÕES


# Own


"""
___REGRAS GERAIS DE LÓGICA DE CRIPTOGRAFIA___

    1 --> Classe é definida como o conjunto de dados trabalhados, incluindo dados pre-criptografados, dados criptografados e chaves.

    2 --> Toda classe, deve conter um dado legível, com:
        -- Um par de chaves completo, contendo:
                -- Uma chave correspondente pública;
                -- Uma chave correspondente privada.
        -- Um dado correspondente pre-criptografado;
        -- Um dado correspondente criptografado.
"""



class Encrypt:
    def __init__(self, pb, dado):  # Dado deve estar pré-criptografado pelo preCoding.py
        self.pb = pb
        self.dado = dado

        self.dadoCriptografado = self.criptografar(self.pb, self.dado)


    @staticmethod
    def criptografar(chave_pb, dado):
        """
        pow(caractere, e, mod=n)
        """
        dadoCriptografado = []
        for caractere in dado:
            caractereCriptografado = pow(caractere, chave_pb[1], mod=chave_pb[0])  # c = (m, e, mod=n)
            dadoCriptografado.append(caractereCriptografado)
        return dadoCriptografado




class Decrypt:
    def __init__(self, pv, dado):
        self.pv = pv
        self.dado = dado

        self.dadoDecodificado = self.decodificar(self.pv, self.dado)


    @staticmethod
    def decodificar(chave_pv, dado):
        """
        pow(caractere, e, mod=n)
        """
        n = chave_pv[0] * chave_pv[1]
        dadoPreDecodificado = []
        for caractere in dado:
            caracterePreDecodificado = pow(caractere, chave_pv[-1], n)  # m = (c, d, mod=n)
            dadoPreDecodificado.append(caracterePreDecodificado)
        return dadoPreDecodificado




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


    # testeE = Encrypt((35, 7), [27, 28, 10])
    # print(testeE.dadoCriptografado)
    #
    # testeD = Decrypt((5, 7, 7), [13, 7, 10])
    # print(testeD.dadoDecodificado)

    from RSA import gk

    # keys = gk.Keys()
    # pb = keys.pb
    # pv = keys.pv
    # print(pb)
    # print(pv)

    testeE = Encrypt((222631833847, 149206200581), [12, 13])
    print(testeE.dadoCriptografado)

    """
    pb - (n,e) = (222631833847, 149206200581)
    pv - (p, q, d) = (558791, 398417, 150760677421)
    phi = 222630876640
    d * e = 22494427875005163781601
    dadoCriptografado = [148418125426, 127705656928]
    """

    testeD = Decrypt((558791, 398417, 150760677421), [148418125426, 127705656928])
    print(testeD.dadoDecodificado)