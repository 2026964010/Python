a=set()  #중복된 값 허용 X
a={1,2,3,5,7,11}

a.add(13)  #값 추가

print(a)

#print(a[0])  #인덱스 X

n=0
b={i for i in range(1,10) if i%2==0}
print(b)