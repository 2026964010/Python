a = int(input("첫 번째 정수를 입력하시오: "))
b = int(input("두 번째 정수를 입력하시오: "))
gcd = 1
for k in range(1, min(a, b) + 1):
    if a % k == 0 and b % k == 0:
        gcd = k
print(f"{a}과 {b}의 최대 공약수는 {gcd}입니다.")