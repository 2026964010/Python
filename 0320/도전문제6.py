print("===============================")
print("메뉴 1번: 치즈 버거")
print("메뉴 2번: 치킨 버거")
print("메뉴 3번: 불고기 버거")
print("================================")
selection=int(input("메뉴를 선택하세요: "))

print("===============================")
print("메뉴 1번: 콜라")
print("메뉴 2번: 사이다")
print("메뉴 3번: 물")
print("================================")
drink_selection=int(input("음료를 선택하세요: "))

if selection >=1 and selection <=3:
    print("메뉴", selection)
else:
    print("잘못 입력하셨습니다.")

if drink_selection >=1 and drink_selection <=3:
    print("음료", drink_selection)
else:
    print("잘못 입력하셨습니다.")
