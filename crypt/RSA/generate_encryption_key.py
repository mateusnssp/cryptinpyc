from crypt.RSA.choice_pq import choice_pq

def generate_encryption_key():
    pq = choice_pq()
    encryption_key = pq[0] * pq[1]
    return encryption_key

if __name__ == '__main__':
    print(generate_encryption_key())
    print(type(generate_encryption_key()))
    