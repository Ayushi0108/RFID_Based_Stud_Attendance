# !! Not to be included

# import openpyxl
# import datetime as dt
# from multiprocessing import Process
# def save(student_id, sheet_name):
#     p = Process(target=save_excel, args=(student_id, sheet_name))
#     p.start()
#     p.join()

# def save_excel(student_id, sheet_name):
#     print(student_id, sheet_name)
#     excel_sheet_path='Excel_Sheets/main/'
#     # student_id = [1, 2, 3, 4, 7,9,10] # <- replace it here with the data received by the server
#     date = dt.datetime.now()
#     date = f"{date:%d-%m-%Y}"
#     try:
#         workbook = openpyxl.load_workbook(excel_sheet_path+sheet_name)
#     except Exception:
#         # create_workbook(excel_sheet_path+sheet_name)
#         return
#     sheet = workbook.active
#     val = sheet.max_column+1
#     sheet.cell(1, val).value = date           
#     for row in range(2, sheet.max_row + 1):
#         key = int(sheet.cell(row, 1).value)
#         # print(i)
#         if str(key) in student_id:
#             print(key)
#             sheet.cell(row, val).value = "P"
#         else:
#             sheet.cell(row, val).value = "A"
#     workbook.save(excel_sheet_path+sheet_name)
#     workbook.close()


# from user_authentication.models import Record, Stud

# # def create_workbook(file):
# #     print(file)
# #     file = 'Excel_Sheets/main/test_File.xlsx'
# #     workbook = openpyxl.Workbook()
# #     students_info = Stud.objects.all().order_by('roll').values('roll','name')
# #     columns=['Roll No', 'Name']
# #     sheet = workbook.worksheets[0]
# #     sheet[1]=columns[0]
# #     sheet[2]=columns[1]

# #     workbook.save(file)