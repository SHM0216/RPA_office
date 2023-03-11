import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = False  # Set this to True if you want to see the Excel file being opened

input_file_path = r"C:\Users\Owner\OneDrive\바탕 화면\운동일지.xlsx"  # input file path
output_file_path = r"C:\Users\Owner\OneDrive\바탕 화면\운동일지.pdf"  # output file path 

workbook = excel.Workbooks.Open(input_file_path)
workbook.ExportAsFixedFormat(0, output_file_path, 1, 0)

workbook.Close()

excel.Quit()
