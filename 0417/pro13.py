primes = list(range(2, 101))
for i in range(2, 101):
    for j in range(i*2, 101, i):
        if j in primes:
            primes.remove(j)
print(*primes, None)