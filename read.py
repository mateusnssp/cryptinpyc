
class Read:
    """
    Recebe diretório, o lê e retorna dados formatados para a decodificação.
    """
    def __init__(self, path):

        self.path = path if path[-1] == '/' else f'{path}/'

        self.dado = self.read_dado()
        self.pb = self.read_pb()
        self.pv = self.read_pv()

    def read_dado(self):
        with open(f'{self.path}ief', 'r+') as file:
            dado = file.read()
        return dado

    def read_pb(self):
        with open(f'{self.path}pb', 'r+') as file:
            pv = file.read()
        return pv

    def read_pv(self):
        with open(f'{self.path}pv', 'r+') as file:
            pv = file.read()
        return pv


if __name__ == '__main__':
    test = Read('./66c')
    print(test.dado)
    print(test.pb)
    print(test.pv)