import openpyxl
wb = openpyxl.load_workbook(filename='../ArticleScripts/ExcelPython/openpyxl.xlsx')
sheet = wb['test']
# считываем значение определенной ячейки
val = sheet['A1'].value
# считываем заданный диапазон
vals = [v[0].value for v in sheet.range('A1:A2')]
# записываем значение в определенную ячейку
sheet['B1'] = val
# записываем последовательность
i = 0
for rec in vals:
    sheet.cell(row=i, column=2).value = rec
    i += 1
# сохраняем данные
wb.save('../ArticleScripts/ExcelPython/openpyxl.xlsx')
