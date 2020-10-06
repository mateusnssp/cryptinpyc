
from RSA import gk
from RSA import conversion
from RSA import preCoding

keys = gk.Keys()
chavePublica = keys.pb
chaveProvada = keys.pv

def gerar_dadoPreCodificado(dado): return preCoding.precrypt(dado)



def Encrypt(chavePublica, dado):

    return 