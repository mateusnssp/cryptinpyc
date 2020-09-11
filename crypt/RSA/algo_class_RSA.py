
from math import gcd

class Crypt:

    def __init__(self, n):
        self.n = n


    def phi(self):
        """
        Totient
        :return: phi(n)
        """
        amount = 0
        for k in range(1, self.n + 1):
            if gcd(self.n, k) == 1:
                amount += 1
        return amount


if __name__ == '__main__':

    test = Crypt(100)
    print(test.phi())