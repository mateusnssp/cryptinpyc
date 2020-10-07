# Importações

# Own
from RSA import gk, preCoding, conversion

"""
    ATRIBUTOS:
    Passados pelo usuário:
        - Dado legível;
    Retorno:
    - Dado pré-criptografado;
    - Chaves;
        - PB
        - PV
    - Dado criptografado.

    MÈTODOS:
    - Pré-codificação
    - Codificação
    
"""


class RSA:
    def __init__(self):
        self.keys = gk.Keys()
        self.pb, self.pv = self.keys.pb, self.keys.pv

    def encrypt(self, dado):
        dado = preCoding.precrypt(dado)
        encrypt = conversion.Encrypt(self.pb, dado)

        return encrypt.dadoCriptografado

    def decrypt(self, dado, pv):
        decrypt = conversion.Decrypt(pv, dado)

        decrypt = preCoding.de_precrypt(decrypt.dadoDecodificado)

        return decrypt


if __name__ == '__main__':
    test = RSA()
    dado = input("Dado: ")
    print(test.encrypt(dado))
    print(test.pv)
    print(''.join(
        test.decrypt([114150791279, 109345633586, 162773109449, 35164162070, 43250113339, 43133982253, 109387188070],
                     (612811, 279857, 46067732203))))
"""



[84941406504, 1148071510]
(579017, 189701, 13722099571)
[1721840915746191216871, 362787738830932334885, 123637340442391470039]
"""
