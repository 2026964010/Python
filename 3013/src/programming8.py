num = int(input("정수="))

a = num % 10
num = num // 10

b = num % 10
num = num // 10

c = num % 10
num = num // 10

d = num % 10

print(a + b + c + d)