import random

tries=0
guess=0;
answer=random.randint(1,100)

print("숫자 1~100 맞추시오.")

while guess != answer:
    guess=int(input("숫자입력"))
    tries=tries+1
    if guess<answer:
        print("낮음")
    elif guess>answer:
        print("높음")

if guess==answer:
    print("정답")
else:
    print("정답은",answer)