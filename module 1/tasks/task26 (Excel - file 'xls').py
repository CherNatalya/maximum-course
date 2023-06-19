import xlrd
import xlwt
# открываем файл
rb = xlrd.open_workbook('../ArticleScripts/ExcelPython/xl.xls', formatting_info=True)
# выбираем активный лист
sheet = rb.sheet_by_index(0)
# получаем значение первой ячейки A1
val = sheet.row_values(0)[0]
# получаем список значений из всех записей
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
# получаем значение первой ячейки A1
val = sheet.row_values(0)[0]
# получаем список значений из всех записей
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
wb = xlwt.Workbook()
ws = wb.add_sheet('Test')
# в A1 записываем значение из ячейки A1 прошлого файла
ws.write(0, 0, val[0])
# в столбец B запишем нашу последовательность из столбца A исходного файла
i = 0
for rec in vals:
    ws.write(i, 1, rec[0])
    i += i
# сохраняем рабочую книгу
wb.save('../ArticleScripts/ExcelPython/xl_rec.xls')
