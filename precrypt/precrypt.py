def precrypt(conteudo, path_file):
    """
    Pré-criptografar conteudo.
    conteudo deve ser do tipo <class 'list'>
    """

    # Abrir banco de caracteres.
    l = open(path_file)




    # Passar banco de caracteres para variável do programa
    caracteres = [x for x in l.read()]

    # Fechar banco de caracteres
    l.close()


    # Definir itens correspodentes para realizar as substituições
    # Padrão obrigatório do momento (12-07-2020): len(str(codigo[1])) = 4
    codigo = [i for i in range(1000, 1000 + len(caracteres))]


    # Realizar as substituições
    for i in conteudo:
        conteudo[conteudo.index(i)] = codigo[caracteres.index(i)]


    return conteudo


if __name__ == '__main__':
    print(precrypt(list('mmm'), './caracteres'))

