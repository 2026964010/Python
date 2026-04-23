words = ['aba', 'xyz', 'abc', '121']
count = sum(1 for w in words if w[0] == w[-1])
print(words)
print("문자열의 개수=", count)