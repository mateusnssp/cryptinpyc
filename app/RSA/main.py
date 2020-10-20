# Importações

# Own
from RSA import conversion, preCoding, gk

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
    t_dado = input("Dado legível: ")
    t_dado_criptografado = test.encrypt(t_dado)
    print(t_dado_criptografado)
    print(f'chave privada: {test.pv}')
    print(f'chave pública: {test.pb}')
    t_dado_decodificado =''.join(test.decrypt(t_dado_criptografado, test.pv))
    print(f'Dado decodificado: {t_dado_decodificado}')

    test_pb = (325755551873, 78130628441)
    test_pv = (610957, 533189, 139346978633)
    test_dado = [94333172122, 171896840767]

    test = RSA()
    test_dado_deCodificado = test.decrypt(test_dado, test_pv)
    print('. .'*30)
    print(test_dado_deCodificado)



