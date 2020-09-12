
# Builtins
import random
from math import gcd


# Módulos próprios


def generate_prime_numbers(lim = 100):
    """
    Gera lista de números primos
    """
    l = []
    for num in range(2, lim):
        for item in range(2, num):
            if num % item == 0:
                pass
        else:  # Se o módulo nunca for zero, é primo
            l.append(num)
    return l

p, q = random.choice(generate_prime_numbers()), random.choice(generate_prime_numbers())
print(p, q)
n = (p-1)*(q-1)

def phi(expression_n):
    """
    Retorna totiente
    """
    amount = 0
    for k in range(1, expression_n + 1):
        if gcd(expression_n, k) == 1:
            amount += 1
    return amount




def generate_e(num = 100):
    """
    Gera um numero aleatório e tal que 1 < e <phi(expression_n)
    """
    def mdc(n1, n2):
        rest = 1
        while n2 != 0:
            rest = n1 % n2
            n1 = n2
            n2 = rest
        return n1
    while True:
        e = random.randrange(2, num)
        if mdc(num, e) == 1:
            return e

print(generate_e())







if __name__ == '__main__':

    print(phi(n))