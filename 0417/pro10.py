seats = [[0]*10 for _ in range(10)]
print("  ", end="")
print(*range(1, 11))
print("-" * 35)
for row in seats:
    print(*row)

while True:
    r = int(input("원하시는 좌석의 행번호를 입력하세요(종료는 -1): "))
    if r == -1: break
    c = int(input("원하시는 좌석의 열번호를 입력하세요(종료는 -1): "))
    if c == -1: break
    seats[r-1][c-1] = 1
    print("예약되었습니다.")