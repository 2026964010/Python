values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("실행전", values)
values = [x if x <= 2 or x >= 9 else -x for x in values]
print("실행후", values)