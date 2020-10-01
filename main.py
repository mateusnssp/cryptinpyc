def master(self):
    print('master')


def encrypt(self):
    import encrypt

    dado_legivel = input(
        f'{color_open["verde"]}:::Insira o dado a ser criptografado:::\n{self.espera_parametro}{color_close["verde"]}')
    encrypt = encrypt.RSA(dado_legivel)

    resposta_pretendeVizualizar = input(
        f'{color_open["verde"]}:::Pretende vizualizar o conteúdo criado? (Y/N):::\n{self.espera_parametro}{color_close["verde"]}')
    if resposta_pretendeVizualizar.upper() == 'Y':
        print(f'{encrypt.info()}')
    else:
        pass


def descrypt(self):
    print("EM CONSTRUÇÃO")


def ajuda(self):
    print('\n\n"h" para ajuda;\n"e" para criptografar\n"d" para descriptografar\n\n')
