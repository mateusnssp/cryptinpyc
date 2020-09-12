def generate_prime_numbers(lim):
    """
    Gera lista de números primos acima de 10**100
    """

    l = []
    for num in range(10**100, lim):
        for n in range(2, num):
            if num % n == 0:
                break
        else:  # Se o módulo nunca for zero, é primo
            l.append(num)
            print(num)
    return l

test = generate_prime_numbers(10**101)