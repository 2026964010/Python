sum_pi = 0.0
divident = 4.0
divisor = 1.0
n = 1

while n <= 300:          # 300항까지 계산
    sum_pi += divident / divisor
    divident = -divident
    divisor += 2
    n += 1

print(f"Pi ≈ {sum_pi:.10f}")   # 소수점 10자리까지 출력