num=int(input("Enter a number: "))

fact=1
print(num,"!=",end=" ")

for i in range(1,num+1):
    fact*=i
    if num>i:
        print(i,end=" * ")
    else:        print(i,end=" = ")

print(fact)
