import win32com.client as win32
import os

# HWP 실행
hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

# 새 문서 생성 (isTab = False → 새 창으로)
hwp.XHwpDocuments.Add(False)

# 텍스트 입력
hwp.HAction.GetDefault("InsertText", hwp.HParameterSet.HInsertText.HSet)
hwp.HParameterSet.HInsertText.Text = "안녕하세요, Python에서 생성한 HWP 문서입니다!"
hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)

# 저장
save_path = os.path.abspath("python_hwp_example.hwp")
hwp.SaveAs(save_path)

# 종료
hwp.Quit()

print(f"HWP 문서 생성 완료: {save_path}")
