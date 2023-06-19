from fpdf import FPDF
pdf = FPDF('P', 'cm', (12, 20))
pdf.add_page()
# 'c' - название шрифта, которое мы ему дали
pdf.add_font('c', '', 'C:\WINDOWS\FONTS\CORBEL.ttf', uni=True)
pdf.set_font('c', size=16)
pdf.set_text_color(0, 255, 0)
pdf.set_fill_color(155, 50, 140)
# align - выравнивание, 'C' - по центру
pdf.cell(10, 5, txt='Hello', align='C', fill=True)
pdf.image('pic.jpg', h=0, w=0, x=1, y=9)
pdf.output('test pdf.pdf')
