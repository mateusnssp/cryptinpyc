
def precrypt(conteudo):
    conteudo = list(conteudo)
    for i in conteudo:
        conteudo[conteudo.index(i)] = ord(i)
    return conteudo



if __name__ == '__main__':
    print(precrypt('rsdddddddatifuyaseiufgxagfbcandyafsdatsdtd437985294285nhc385691236cx1b689s3n'))




