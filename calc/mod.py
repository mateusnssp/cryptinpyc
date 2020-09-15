def mod(a, b):  # Função mod

    if a < b:
        return a
    else:
        c = a % b
        return c


if __name__ == '__main__':
    print(mod(8, 3))