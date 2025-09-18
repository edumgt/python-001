# HashSetExample.py

def get_fruits_info():
    # set 생성
    fruits = set()

    # 요소 추가
    fruits.add("Apple")
    fruits.add("Banana")
    fruits.add("Orange")
    fruits.add("Apple")  # 중복 무시

    info = {}
    info["초기_과일_개수"] = len(fruits)
    info["초기_과일_목록"] = list(fruits)  # set → list 변환
    info["Banana_포함"] = "Banana" in fruits

    # Orange 제거
    fruits.remove("Orange")
    info["Orange_제거_후"] = list(fruits)

    return info


def main():
    result = get_fruits_info()
    print("HashSetExample 실행 결과:", result)


if __name__ == "__main__":
    main()
