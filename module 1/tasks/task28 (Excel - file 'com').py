import win32com.client
Excel = win32com.client.Dispatch("Excel.Application")
wb = Excel.Workbooks.Open(u'D:\\Scripts\\DataScience\\ArticleScripts\\ExcelPython\\xl.xls')
sheet = wb.ActiveSheet
# получаем значение первой ячейки
val = sheet.Cells(1, 1).value
# получаем значения цепочки A1:A2
vals = [r[0].value for r in sheet.Range("A1:A2")]
# записываем значение в определенную ячейку
sheet.Cells(1, 2).value = val
# записываем последовательность
i = 1
for rec in vals:
    sheet.Cells(i, 3).value = rec
    i = i + 1
# сохраняем рабочую книгу
wb.Save()
# закрываем ее
wb.Close()
# закрываем COM объект
Excel.Quit()
