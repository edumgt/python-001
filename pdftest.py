from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

# ✅ 한글 폰트 추가 (경로 주의!)
pdf.add_font("malgun", fname="C:/Windows/Fonts/malgun.ttf", uni=True)
pdf.set_font("malgun", size=16)

# ✅ 한글 텍스트 출력
pdf.cell(200, 10, text="Python으로 PDF 만들기 예제", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.cell(200, 10, text="한글도 잘 출력됩니다!", new_x="LMARGIN", new_y="NEXT", align="L")

# PDF 저장
pdf.output("example_korean.pdf")
print("PDF 생성 완료!")
