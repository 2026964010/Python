size = int(input("게임판의 크기: "))
for _ in range(size):
    print("--- " * size)
    print("|   " * (size + 1))
print("--- " * size)