def prime_sieve_eratosthenes(num):

    primes = [True for i in range(num + 1)]
    p = 2

    while p * p <= num:
        if primes[p]:
            for i in range(p * p, num + 1, p):
                primes[i] = False
        p += 1

    for prime in range(2, num + 1):
        if primes[prime]:
            print(prime, end=" ")


if __name__ == "__main__":
    num = int(input())

    prime_sieve_eratosthenes(num)
