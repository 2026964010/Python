import random
coins = [random.randint(0, 1) for _ in range(10)]
print(coins)

max_len = cur_len = 1
for i in range(1, len(coins)):
    if coins[i] == coins[i-1]:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
print("최대 연속 길이=", max_len)