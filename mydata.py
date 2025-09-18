import json

def get_data():
    # HashMap 같은 dict 생성
    data = {
        "name": "홍길동",
        "age": 25,
        "email": "hong@example.com"
    }
    return data

# 원래 main() 로직 → 콘솔에서 실행 시 동작
def main():
    json_string = json.dumps(get_data(), ensure_ascii=False)
    print("JSON 출력:", json_string)

if __name__ == "__main__":
    main()
