w = float(input("무게(킬로그램): "))
h = float(input("키(미터): "))
bmi = w / (h**2)
print(f"당신의 BMI: {bmi}")

if 20 <= bmi <= 24.9:
    print("정상입니다.")
elif 25 <= bmi <= 29.9:
    print("과체중입니다.")
elif bmi >= 30:
    print("비만입니다.")