import json

def main():
    # HashMap 같은 dict 생성
    data = {
        "name": "홍길동",
        "age": 25,
        "email": "hong@example.com"
    }

    # dict → JSON 문자열 변환
    json_string = json.dumps(data, ensure_ascii=False)

    print("JSON 출력:", json_string)

if __name__ == "__main__":
    main()
