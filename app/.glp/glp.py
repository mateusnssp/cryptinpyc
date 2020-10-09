#!/bin/python3

def generate_prime_numbers(lim):
    """
    Gera lista de números primos acima de 10**100
    """
    inicio = 10**100
    l = []
    for num in range(inicio, lim):
        for n in range(2, num):
            if num % n == 0:
                print("Nenhum primo encontrado")
                break
        else:  # Se o módulo nunca for zero, é primo
            print(num)
    return l

test = generate_prime_numbers((10**100)+38)