correct_id = "python"
correct_password = "pythonisfun"

while True:
    user_id = input("아이디를 입력하세요: ")
    user_pw = input("암호를 입력하세요: ")
    
    if user_id == correct_id and user_pw == correct_password:
        print("로그인 성공")
        break
    else:
        print("아이디 또는 암호가 틀렸습니다. 다시 입력해주세요.")