import random

initial_money = 50
goal = 250
wins = 0
total_games = 100

# 확률을 0.1부터 0.5까지 0.1씩 증가시키며 테스트
for prob in [0.1, 0.2, 0.3, 0.4, 0.5]:
    wins = 0
    for i in range(total_games):
        cash = initial_money
        while cash > 0 and cash < goal:
            # prob 확률로 이기기 (1 나오면 승리)
            if random.random() < prob:
                cash = cash + 1
            else:
                cash = cash - 1
        if cash == goal:
            wins += 1
    
    success_rate = wins / total_games * 100
    print(f"승리 확률 {prob:.1f} → {wins}번 성공 / {total_games}번 → 성공률 {success_rate:.1f}%")