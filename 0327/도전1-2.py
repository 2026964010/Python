def f(x):
    return x**2 - x - 1

START = 1.0
END = 2.0
TOL = 0.0001   # 오차 허용
COUNT = 100    # 반복 횟수

a = START
b = END

for i in range(COUNT):
    m = (a + b) / 2
    fm = f(m)

    if abs(fm) < TOL:
        print("방정식의 해는", m)
        break

    if f(a) * fm < 0:
        b = m
    else:
        a = m

print("최종 근사값:", m)