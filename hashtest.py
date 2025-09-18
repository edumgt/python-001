# HashSetExample.py

def main():
    # set 생성
    fruits = set()

    # 요소 추가
    fruits.add("Apple")
    fruits.add("Banana")
    fruits.add("Orange")
    fruits.add("Apple")  # 이미 있는 값이면 무시됨 (중복 저장 안됨)

    # 크기 확인
    print("과일 개수:", len(fruits))  # 4

    # 출력 (순서는 보장되지 않음)
    print("과일 목록:", fruits)

    # 포함 여부 확인
    print("Banana 포함?", "Banana" in fruits)

    # 요소 제거
    fruits.remove("Orange")
    print("Orange 제거 후:", fruits)


if __name__ == "__main__":
    main()
