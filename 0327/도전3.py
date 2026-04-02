import random

tries = 0
guess = 0
answer = random.randint(1, 100)

print("1부터 100 사이의 숫자")

while guess != answer and tries < 10:
    guess = int(input("숫자를 입력: "))
    tries = tries + 1

    if guess < answer:
        print("낮음!")
    elif guess > answer:
        print("높음!")

if guess == answer:
    print("정답,시도횟수=", tries)
else:
    print("실패,정답", answer)