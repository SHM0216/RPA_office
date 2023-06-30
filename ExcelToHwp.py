import win32com.client as win32

# 한/글 열기
hwp = win32.gencache.EnsureDispatch("HwpFrame.HwpObject")
hwp.XHwpWindows.Item(0).Visible = True
hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")
path_hwp = r"C:\Users\Owner\OneDrive\바탕 화면\RPA\Python\win32.com\필드.hwp"
hwp.Open(path_hwp)

# 엑셀 열기
excel = win32.gencache.EnsureDispatch("Excel.Application")
excel.Visible = True
path_excel = r"C:\Users\Owner\OneDrive\바탕 화면\RPA\Python\win32.com\취미.xlsx"
wb = excel.Workbooks.Open(path_excel)
ws = wb.Worksheets(1)

# 필드삽입 함수 정의
def 필드삽입(index, value):
    field_list = ["이름", "성별", "생일", "취미"]
    for idx, field in enumerate(field_list):
        hwp.PutFieldText(f"{field}{{{{{index}}}}}", value[idx])

# 첫 쪽 복사
# hwp.Run("CopyPage")

# while문 실행
row = 2
while True:
    if not ws.Cells(row, 1).Value:
        # hwp.Run("DeletePage")
        break
    else:
        data = list(ws.Range(ws.Cells(row, 1), ws.Cells(row, 4)).Value[0])
        data[2] = data[2].strftime("%Y년 %#m월 %#d일")
        필드삽입(row - 2, data)
        # hwp.Run("PastePage")
        row += 1
