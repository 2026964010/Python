import random
x=random.randint(1, 100)
y=random.randint(1, 100)

A=int(input(f"{x} + {y} = "))
flag=(A == (x + y))
print(flag)
