sum_pi = 0.0
divident = 4.0

for i in range(300):          # 0 ~ 299 → 300번 반복
    sum_pi += divident / (2 * i + 1)
    divident = -divident

print(f"Pi ≈ {sum_pi:.10f}")