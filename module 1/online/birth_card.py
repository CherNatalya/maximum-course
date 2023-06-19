from pdf import FPDF
from datetime import datetime
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.image('Birthday.jpg', w=210, h=297, x=0, y=0)
# название, пустой, путь, unicode
pdf.add_font('gabriola', '', 'C:\WINDOWS\FONTS\GABRIOLA.ttf', uni=True)
pdf.set_font('gabriola', size=74)
pdf.set_text_color(250, 0, 155)
friend = input('Введи имя друга: ')
sex = input('Пол друга - м или ж? ')
name = input('Введите ваше имя: ')
pdf.cell(0, 50, ln=1)
if sex == 'ж':
    pdf.cell(0, 20, txt='Дорогая, ' + friend + '!', align='C', ln=1)
elif sex == 'м':
    pdf.cell(0, 20, txt='Дорогой, ' + friend + '!', align='C', ln=1)
pdf.set_font('gabriola', size=38)
pdf.set_text_color(128, 0, 128)
text = input('Введи поздравление: ')
pdf.cell(0, 10, ln=1)
pdf.set_right_margin(25)
pdf.set_left_margin(25)
pdf.multi_cell(0, 15, txt=text, align='C')
today = datetime.today().strftime('%d.%m.%y')
pdf.cell(0, 20, txt=today, align='R', ln=1)
pdf.cell(0, 10, txt=name, align='R', ln=1)
pdf.output('birth_card.pdf')
