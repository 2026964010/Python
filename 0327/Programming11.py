import random
hits = 0
total = 1000000
for _ in range(total):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1.0:
        hits += 1
pi = 4 * hits / total
print(f"파이의 값은 {pi}입니다.")