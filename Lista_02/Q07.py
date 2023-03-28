#Using a generator, create an infinite list
#of prime numbers.

def prime_generator():
    primes = [2]
    yield 2
    num = 3
    while True:
        for p in primes:
            if num % p == 0:
                num += 1
                break
        else:
            primes.append(num)
            yield num

pg = prime_generator()
next(pg)


