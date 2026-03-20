ftemp=float(input("화씨 온도를 입력하세요: "))
if ftemp<=32:
    print("얼음")
elif ftemp>32 and ftemp<212:
    print("액체")
else:
    print("기체")
    