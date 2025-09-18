# -----------------------------
# ListCrudExample in Python
# -----------------------------

def main():
    # 파이썬의 리스트 생성 (제네릭 개념 없음, 어떤 타입이든 저장 가능)
    fruits = []

    # -----------------------------
    # C: Create (생성/추가)
    # -----------------------------
    fruits.append("Apple")   # 리스트에 "Apple" 추가 → ["Apple"]
    fruits.append("Orange")  # 리스트에 "Orange" 추가 → ["Apple", "Orange"]

    # -----------------------------
    # R: Read (조회)
    # -----------------------------
    print("First fruit:", fruits[1])
    # 인덱스 1의 값 "Orange" 반환
    # 출력: First fruit: Orange

    # 리스트의 모든 요소를 순회하며 출력
    for f in fruits:
        print("Fruit:", f)          # 각 요소 문자열 출력
        print("Fruit:", len(f))     # 각 문자열 길이 출력
        # 결과:
        # Fruit: Apple
        # Fruit: 5
        # Fruit: Orange
        # Fruit: 6

    # -----------------------------
    # U: Update (수정)
    # -----------------------------
    fruits[1] = "Banana"
    # 인덱스 1의 값 "Orange" → "Banana"로 변경 → ["Apple", "Banana"]

    print(fruits[1])
    # 출력: Banana

    # -----------------------------
    # D: Delete (삭제)
    # -----------------------------
    fruits.remove("Apple")
    # "Apple" 요소 삭제 → ["Banana"]

    fruits.clear()
    # 리스트의 모든 요소 제거 → []

if __name__ == "__main__":
    main()
