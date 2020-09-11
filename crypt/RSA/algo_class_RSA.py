
import random
from math import gcd

def generate_prime_numbers(lim):
    """
    Gera lista de números primos
    """

    l = []
    for num in range(10**100, lim):
        for n in range(10**100, num):
            if num % n == 0:
                pass
        else:  # Se o módulo nunca for zero, é primo
            l.append(num)
            print(num)
    return l




def phi(n):
    """
    Totient
    :return: phi(n)
    """
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount





if __name__ == '__main__':

    print(phi(8))