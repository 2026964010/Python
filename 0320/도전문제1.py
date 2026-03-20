import random

x = random.randint(1, 100)
y = random.randint(1, 100)

answer1=int(input(f"{x}+{y}= "))
answer2=int(input(f"{x}-{y}= "))

flag1=(answer1==(x+y))
flag2=(answer2==(x-y))
print(flag1)
print(flag2)
