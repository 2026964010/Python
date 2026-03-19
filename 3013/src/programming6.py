cost = float(input("음식 비용: "))
tip_rate = float(input("팁 비율(%): "))

total = cost + (cost * tip_rate / 100)
print(f"총액: {total:.0f} 달러")