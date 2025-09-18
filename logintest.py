import json
import os

USERS_FILE = "users.json"
LOGIN_FILE = "loginusers.json"

def load_users():
    """users.json에서 전체 사용자 정보 로드"""
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_login_users():
    """loginusers.json에서 현재 로그인 사용자 목록 로드"""
    if not os.path.exists(LOGIN_FILE):
        return []
    with open(LOGIN_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_login_users(login_users):
    """현재 로그인 사용자 목록 저장"""
    with open(LOGIN_FILE, "w", encoding="utf-8") as f:
        json.dump(login_users, f, ensure_ascii=False, indent=4)

def main():
    users = load_users()
    login_users = load_login_users()

    while True:
        user_id = input("아이디 입력해 주세요: ")
        pw = input("비번 입력해 주세요: ")
        print("")

        if user_id in users:
            if users[user_id] == pw:
                if user_id in login_users:
                    print("이미 로그인 상태입니다. 중복 로그인 불가!")
                else:
                    print("Login Success ✅")
                    login_users.append(user_id)
                    save_login_users(login_users)
                    break  # 프로그램 종료
            else:
                print("Login Fail (비밀번호 오류)")
        else:
            print("Login ID Not Exist")

if __name__ == "__main__":
    main()
