number = 2
count = 0

while number <= 100:
    divisor = 2
    prime = True
    
    while divisor < number:
        if number % divisor == 0:
            prime = False
            break
        divisor += 1
    
    if prime:
        count += 1
        print(number, end=" ")
    
    number += 1

print()
print(f"1부터 100 사이의 소수는 총 {count}개입니다.")