import random

flag = True
while flag:
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    if random.choice([True, False]):
        operator = '+'
        correct_answer = x + y
    else:
        operator = '-'
        if y > x:
            x, y = y, x
        correct_answer = x - y
    answer = int(input(f"{x} {operator} {y} = "))
    
    if answer == correct_answer:
        print("잘했어요!!")
        flag = False
    else:
        print("틀렸어요. 하지만 다음번에는 잘할 수 있죠?")