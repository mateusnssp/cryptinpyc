import hashlib
from datetime import datetime

class File:
    def __init__(self, pb, pv, dado):
        self.pb = pb
        self.pv = pv
        self.dado = dado

        self.hash_l1 = list("0123456789[], ()")
        self.hash_l2 = list("01f3456789harbyk")

        self.dadoFormatado = self.gerar_dado_formatado(self.dado, self.hash_l1, self.hash_l2)
        self.pbFormatado = self.gerar_pb_formatado(self.pb, self.hash_l1, self.hash_l2)
        self.pvFormatado = self.gerar_pv_formatado(self.pv, self.hash_l1, self.hash_l2)

    def gerar_dado_formatado(self, dado, hash_l1, hash_l2):
        dado = str(dado)
        for char in dado:
            if dado.count(char) > 0:
                dado = dado.replace(char, str(hash_l2[hash_l1.index(char)]))

        hash_verificador = hashlib.md5(dado.encode('utf-8')).hexdigest()

        dado = f'{hash_verificador}{dado}{hash_verificador}'
        return dado

    def gerar_pb_formatado(self, pb, hash_l1, hash_l2):
        pb = str(pb)
        for char in pb:
            if pb.count(char) > 0:
                pb = pb.replace(char, str(hash_l2[hash_l1.index(char)]))

        hash_verificador = hashlib.md5(pb.encode('utf-8')).hexdigest()

        pb = f'{hash_verificador}{pb}{hash_verificador}'
        return pb

    def gerar_pv_formatado(self, pv, hash_l1, hash_l2):
        pv = str(pv)
        for char in pv:
            if pv.count(char) > 0:
                pv = pv.replace(char, str(hash_l2[hash_l1.index(char)]))

        hash_verificador = hashlib.md5(pv.encode('utf-8')).hexdigest()

        pv = f'{hash_verificador}{pv}{hash_verificador}'
        return pv

    def salvar_dado(self, dado_formatado):
        pass

    def salvar_pb(self, pb_formatado):
        pass

    def salvar_pv(self, pv_formatado):
        pass




if __name__ == '__main__':
    test = File((139167535853, 38798205863), (139167535853, 139166718300, 67749101327),
                [657345, 26395299, 5754352, 21413413, 5124512416])
    print(test.dadoFormatado)
    print(test.pbFormatado)
    print(test.pvFormatado)