ph = float(input("pH를 입력하시오: "))
if ph < 7.0:
    print("산입니다.")
elif ph == 7.0:
    print("중성입니다.")
else:
    print("알칼리입니다.")