import random

print("주사위 던지기 게임을 시작합니다.")
dice = random.randrange(1, 7)
if dice == 1:
    print("1이 나왔습니다.")
elif dice == 2:
    print("2가 나왔습니다.")
elif dice == 3:
    print("3이 나왔습니다.")
elif dice == 4:
    print("4가 나왔습니다.")
elif dice == 5:
    print("5가 나왔습니다.")
else:
    print("6이 나왔습니다.")
print("게임이 종료되었습니다.")