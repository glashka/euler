""" Problem 381
"""

primes = []

def generate_primes(n):
    composites = set()
    primes.append(2)
    composites |= set(2 * i for i in range(2, n // 2 + 1))
    for j in range(3, n, 2):
        if j in composites:
            continue
        else:
            primes.append(j)
            composites |= set(j * i for i in range(j, n // j + 1))

def linear_generate_primes(n):
    lp = [0 for i in range(n)]
    for i in range(2, n):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        j = 0
        while j < len(primes) and i * primes[j] < n and primes[j] <= lp[i]:
            lp[i * primes[j]] = primes[j]
            j += 1

linear_generate_primes(10 ** 8)
primes.remove(2)
primes.remove(3)

def get_big_s(p):
    result = 0

    # k = 3
    nom = 1
    while nom % (p - 2) != 0:
        nom += p
    x = int(nom / (p - 2))
    
    # k = 4
    nom = x
    while nom % (p - 3) != 0:
        nom += p
    y = int(nom / (p - 3))

    # k = 4
    nom = y
    while nom % (p - 4) != 0:
        nom += p    
    z = int(nom / (p - 4))
    
    return (x + y + z) % p

def get_sum_p(n):
    result = 0
    for p in primes[:n]:
        result += get_big_s(p)
    return result

%timeit get_sum_p(10)
%timeit get_sum_p(100)
%timeit get_sum_p(1000)
