import random
ops = ['+', '-', '*', '/']
op = random.choice(ops)
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)

answer = float(input(f"{n1} {op} {n2}의 값은?"))
result = eval(f"{n1}{op}{n2}")

if abs(answer - result) < 0.01: # 소수점 오차 고려
    print("맞았습니다.")
else:
    print("틀렸습니다.")