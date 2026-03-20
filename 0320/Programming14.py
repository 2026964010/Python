a = float(input("a를 입력하시오: "))
b = float(input("b를 입력하시오: "))
c = float(input("c를 입력하시오: "))
D = b**2 - 4*a*c

if D > 0:
    r1 = (-b + D**0.5) / (2*a)
    r2 = (-b - D**0.5) / (2*a)
    print(f"2개의 실근이 존재합니다: {r1:f}와 {r2:f}")
elif D == 0:
    r = -b / (2*a)
    print(f"하나의 실근을 가집니다: {r:f}")
else:
    print("실근이 존재하지 않습니다.")