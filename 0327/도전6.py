import random

count = 0
total = 1000

for i in range(total):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    if dice1 + dice2 == 6:
        count += 1

print(f"{total}번 던졌을 때 합이 6이 나온 횟수: {count}번")
print(f"실제 확률: {count / total * 100:.2f}%")
print(f"이론적 확률: 약 13.89%")