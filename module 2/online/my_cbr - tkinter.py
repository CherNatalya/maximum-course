from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime
window = Tk()
window.title('cbr')
window.geometry('500x500+200+200')
window.config(bg='dodger blue')
window.resizable(width=False, height=False)

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
today = datetime.today()
today = today.strftime('%d/%m/%Y')
date = f'date_req={today}'
response = requests.get(url+date)
xml = BeautifulSoup(response.content, 'lxml')


def get_course(my_id):
    xml1 = xml.find("valute", {'id': my_id})
    return {"value": xml1.value.text, "nominal": xml1.nominal.text, "name": xml1.charcode.text}


img_logo = PhotoImage(file='logo.png')
logo = Label(window, image=img_logo, bg='dodger blue')
logo.place(x=0, y=0)

lab = Label(window, text='Курс валют\n НАШ банк', fg='black', bg='dodger blue', font='Arial 22')
lab.place(y=25, x=150)

course_info = Label(window, text=f"Курс валют на: {today.replace('/', '.')}", bg='dodger blue', font='Arial 22')
course_info.place(y=150, x=90)

usd_dict = get_course('R01235')
usd_dict['value'] = float(usd_dict['value'].replace(',', '.'))
usd_dict['nominal'] = int(usd_dict['nominal'])
usd_course = Label(window, text=f'${round(usd_dict["value"]/usd_dict["nominal"], 2)}', bg='dodger blue',  font='Arial '
                                                                                                               '18')
usd_course.place(y=190, x=100)

eur_dict = get_course('R01239')
eur_dict['value'] = float(eur_dict['value'].replace(',', '.'))
eur_dict['nominal'] = int(eur_dict['nominal'])
eur_course = Label(window, text=f'€{round(eur_dict["value"]/eur_dict["nominal"], 2)}', bg='dodger blue', font='Arial '
                                                                                                              '18')
eur_course.place(y=230, x=100)

cny_dict = get_course('R01375')
cny_dict['value'] = float(cny_dict['value'].replace(',', '.'))
cny_dict['nominal'] = int(cny_dict['nominal'])
cny_course = Label(window, text=f'¥{round(cny_dict["value"]/cny_dict["nominal"], 2)}', bg='dodger blue', font='Arial '
                                                                                                              '18')
cny_course.place(y=270, x=100)

inr_dict = get_course('R01270')
inr_dict['value'] = float(inr_dict['value'].replace(',', '.'))
inr_dict['nominal'] = int(inr_dict['nominal'])
inr_course = Label(window, text=f'₹{round(inr_dict["value"]/inr_dict["nominal"], 2)}', bg='dodger blue', font='Arial '
                                                                                                              '18')
inr_course.place(y=350, x=100)

gbp_dict = get_course('R01035')
gbp_dict['value'] = float(gbp_dict['value'].replace(',', '.'))
gbp_dict['nominal'] = int(gbp_dict['nominal'])
gbp_course = Label(window, text=f'£{round(gbp_dict["value"]/gbp_dict["nominal"], 2)}', bg='dodger blue', font='Arial '
                                                                                                              '18')
gbp_course.place(y=310, x=100)

azn_dict = get_course('R01020A')
azn_dict['value'] = float(azn_dict['value'].replace(',', '.'))
azn_dict['nominal'] = int(azn_dict['nominal'])
azn_course = Label(window, text=f'₼{round(azn_dict["value"]/azn_dict["nominal"], 2)}', bg='dodger blue', font='Arial '
                                                                                                              '18')
azn_course.place(y=190, x=300)

amd_dict = get_course('R01060')
amd_dict['value'] = float(amd_dict['value'].replace(',', '.'))
amd_dict['nominal'] = int(amd_dict['nominal'])
amd_course = Label(window, text=f'֏{round(amd_dict["value"]/amd_dict["nominal"], 2)}', bg='dodger blue', font='Arial '
                                                                                                              '18')
amd_course.place(y=230, x=300)

huf_dict = get_course('R01135')
huf_dict['value'] = float(huf_dict['value'].replace(',', '.'))
huf_dict['nominal'] = int(huf_dict['nominal'])
huf_course = Label(window, text=f'ƒ{round(huf_dict["value"]/huf_dict["nominal"], 2)}', bg='dodger blue', font='Arial '
                                                                                                              '18')
huf_course.place(y=270, x=300)

thb_dict = get_course('R01675')
thb_dict['value'] = float(thb_dict['value'].replace(',', '.'))
thb_dict['nominal'] = int(thb_dict['nominal'])
thb_course = Label(window, text=f'฿{round(thb_dict["value"]/thb_dict["nominal"], 2)}', bg='dodger blue', font='Arial '
                                                                                                              '18')
thb_course.place(y=310, x=300)

brl_dict = get_course('R01115')
brl_dict['value'] = float(brl_dict['value'].replace(',', '.'))
brl_dict['nominal'] = int(brl_dict['nominal'])
brl_course = Label(window, text=f'R${round(brl_dict["value"]/brl_dict["nominal"], 2)}', bg='dodger blue', font='Arial '
                                                                                                               '18')
brl_course.place(y=390, x=100)

gel_dict = get_course('R01210')
gel_dict['value'] = float(gel_dict['value'].replace(',', '.'))
gel_dict['nominal'] = int(gel_dict['nominal'])
gel_course = Label(window, text=f'₾{round(gel_dict["value"]/gel_dict["nominal"], 2)}', bg='dodger blue', font='Arial '
                                                                                                              '18')
gel_course.place(y=430, x=100)

kzt_dict = get_course('R01335')
kzt_dict['value'] = float(kzt_dict['value'].replace(',', '.'))
kzt_dict['nominal'] = int(kzt_dict['nominal'])
kzt_course = Label(window, text=f'₸{round(kzt_dict["value"]/kzt_dict["nominal"], 2)}', bg='dodger blue', font='Arial '
                                                                                                              '18')
kzt_course.place(y=350, x=300)

uah_dict = get_course('R01720')
uah_dict['value'] = float(uah_dict['value'].replace(',', '.'))
uah_dict['nominal'] = int(uah_dict['nominal'])
uah_course = Label(window, text=f'₴{round(uah_dict["value"]/uah_dict["nominal"], 2)}', bg='dodger blue', font='Arial '
                                                                                                              '18')
uah_course.place(y=390, x=300)

krw_dict = get_course('R01815')
krw_dict['value'] = float(krw_dict['value'].replace(',', '.'))
krw_dict['nominal'] = int(krw_dict['nominal'])
krw_course = Label(window, text=f'₩{round(krw_dict["value"]/krw_dict["nominal"], 2)}', bg='dodger blue', font='Arial '
                                                                                                              '18')
krw_course.place(y=430, x=300)
window.mainloop()
