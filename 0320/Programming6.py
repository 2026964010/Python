import random
user = int(input("선택하시오(1: 가위 2: 바위 3: 보): "))
com = random.randint(1, 3)
print(f"컴퓨터의 선택(1: 가위 2: 바위 3: 보): {com}")

if user == com:
    print("비겼음")
elif (user==1 and com==3) or (user==2 and com==1) or (user==3 and com==2):
    print("사용자가 이겼음")
else:
    print("컴퓨터가 이겼음")