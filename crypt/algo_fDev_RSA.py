import random

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

test = generate_prime_numbers(10**120)

sorteio = random.choice(test)
print(sorteio)

def totiente():
    pass


