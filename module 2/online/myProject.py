from tkinter import *
from decimal import *
import calendar
import datetime
import time
import requests
from bs4 import BeautifulSoup
from random import *
import speech_recognition as sr
days = []
now = datetime.datetime.now()
year = now.year
month = now.month
activeStr = ''
stack = []


class Ball:
    def __init__(self, canvas, color, platforma):
        self.__canvas = canvas
        self.__platforma = platforma
        self.__oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.__v_x = choice([-3, -2, -1, 1, 2, 3])
        self.__v_y = -1
        self.__is_end = False

    def get_end(self):
        return self.__is_end

    def draw(self):
        self.__canvas.move(self.__oval, self.__v_x, self.__v_y)
        pos = self.__canvas.coords(self.__oval)
        if self.__touch_platform():
            self.__v_y = -3
        if pos[1] <= 0:
            self.__v_y = 3
        if pos[3] >= 400:
            self.__is_end = True
        if pos[0] <= 0:
            self.__v_x = 3
        if pos[2] >= 500:
            self.__v_x = -3

    def __touch_platform(self):
        pos_rect = self.__canvas.coords(self.__platforma.get_rect())
        pos_oval = self.__canvas.coords(self.__oval)
        if pos_oval[3] <= pos_rect[1]:
            if pos_rect[0] <= pos_oval[0] <= pos_rect[3] or pos_rect[0] <= pos_oval[2] <= pos_rect[3]:
                return True
        return False


class Platform:
    def __init__(self, canvas, color):
        self.__canvas = canvas
        self.__rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.__v_x = 0
        self.__canvas.bind_all('<KeyPress-Left>', self.__left)
        self.__canvas.bind_all('<KeyPress-Right>', self.__right)

    def get_rect(self):
        return self.__rect

    def __left(self, event):
        self.__v_x = -2

    def __right(self, event):
        self.__v_x = 2

    def draw(self):
        self.__canvas.move(self.__rect, self.__v_x, 0)
        pos = self.__canvas.coords(self.__rect)
        if pos[0] <= 0 or pos[2] >= 500:
            self.__v_x = 0


class Knight:
    def __init__(self):
        h = 600
        self.x = 70
        self.y = h // 2
        self.v = 0
        self.photo = PhotoImage(file='knight.png')

    def up(self, event):
        self.y -= 8

    def down(self, event):
        self.y += 8

    def left(self, event):
        self.x -= 8

    def right(self, event):
        self.x += 8

    def stop(self, event):
        self.v = 0


class Dragon:
    def __init__(self):
        self.x = 750
        self.y = randint(100, 500)
        self.v = randint(1, 3)
        self.photo = PhotoImage(file='dragon.png')


def calendfunc(event):
    global days, month, year, now
    days = []
    now = datetime.datetime.now()
    year = now.year
    month = now.month

    def foll():
        global month, year
        month -= 1
        if month == 0:
            month = 12
            year -= 1
        fill()

    def nextt():
        global month, year
        month += 1
        if month == 13:
            month = 1
            year += 1
        fill()

    def fill():
        global days
        info_label['text'] = calendar.month_name[month] + ', ' + str(year)
        month_days = calendar.monthrange(year, month)[1]
        if month == 1:
            prev_month_days = calendar.monthrange(year - 1, 12)[1]
        else:
            prev_month_days = calendar.monthrange(year, month - 1)[1]
        week_day = calendar.monthrange(year, month)[0]
        for i in range(month_days):
            days[i + week_day]['text'] = i + 1
            days[i + week_day]['fg'] = 'black'
            if year == now.year and month == now.month and i == now.day - 1:
                days[i + week_day]['background'] = 'DodgerBlue2'
            else:
                days[i + week_day]['background'] = 'lightgray'
        for i in range(week_day):
            days[week_day - i - 1]['text'] = prev_month_days - i
            days[week_day - i - 1]['fg'] = 'gray'
            days[week_day - i - 1]['background'] = '#f3f3f3'
        for i in range(6 * 7 - month_days - week_day):
            days[week_day + month_days + i]['text'] = i + 1
            days[week_day + month_days + i]['fg'] = 'gray'
            days[week_day + month_days + i]['background'] = '#f3f3f3'

    calender = Tk()
    calender.title('Календарь')
    calender.resizable(False, False)
    prev_button = Button(calender, text='<', command=foll)
    prev_button.grid(row=0, column=0, sticky='nsew')
    next_button = Button(calender, text='>', command=nextt)
    next_button.grid(row=0, column=6, sticky='nsew')
    info_label = Label(calender, text='0', width=1, height=1, font=('Verdana', 16, 'bold'), fg='blue')
    info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')
    for n in range(7):
        lbl = Label(calender, text=calendar.day_abbr[n], width=1, height=1,
                    font=('Verdana', 10, 'normal'), fg='darkblue')
        lbl.grid(row=1, column=n, sticky='nsew')
    for row in range(6):
        for col in range(7):
            lbl = Label(calender, text='0', width=4, height=2,
                        font=('Verdana', 16, 'bold'))
            lbl.grid(row=row + 2, column=col, sticky='nsew')
            days.append(lbl)
    fill()
    calender.mainloop()


def speech_rec(event):
    def get_poem():
        response = requests.get("https://rustih.ru/stihi-russkih-poetov-klassikov/")
        response = response.content
        html = BeautifulSoup(response, 'lxml')
        poems = choice(html.find_all(class_='entry-title'))
        return poems.text, poems.a.attrs['href']

    def get_film():
        response = requests.get("https://kino.mail.ru/cinema/all/")
        response = response.content
        html = BeautifulSoup(response, 'lxml')
        film = choice(html.find_all(class_="text text_block text_fixed text_light_large"))
        return film.a.attrs['href'], film.text

    def get_fact():
        response = requests.get('https://i-fakt.ru/')
        response = response.content
        html = BeautifulSoup(response, 'lxml')
        fact = choice(html.find_all(class_='p-2 clearfix'))
        return fact.a.attrs['href'], fact.text

    def get_kino():
        response = requests.get("https://kudago.com/msk/kino/schedule-cinema/")
        response = response.content
        html = BeautifulSoup(response, 'lxml')
        movie = choice(html.find_all(class_='post-header'))
        return movie.text, movie.a.attrs['href']

    def get_test():
        response = requests.get("https://testometrika.com/tests/")
        response = response.content
        html = BeautifulSoup(response, 'lxml')
        tests = choice(html.find_all(class_='col-xs-12 col-sm-6'))
        return tests.find(class_='test-list__test__title').text.lstrip(), 'https://testometrika.com' + tests.a.attrs[
            'href']

    text = Label(window, text='Закрой это окно и перейди в консоль', bg='DeepSkyBlue2', font=['Arial 18'])
    text.place(x=0, y=10, width=750, height=35)
    while True:
        window.mainloop()
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            print('Скажи что-нибудь... ')
            audio = r.listen(source)
        speech = r.recognize_google(audio, language='ru_RU').lower()
        greets = ['Привет', 'Здравствуй)', 'Hi', 'Hello', 'Приветик', 'Салют!', 'Хай :)', 'Hola', 'Салам', 'Чао',
                  'Бонжур']
        if speech == 'привет':
            print(choice(greets))
        elif speech == 'фильм':
            print('https://kino.mail.ru/', end='')
            print(*get_film(), sep='\n')
        elif speech == 'факт':
            print(*get_fact())
        elif speech == 'кино':
            print(*get_kino())
        elif speech == 'тест':
            print(*get_test())
        elif speech == 'стих':
            print(*get_poem())
        elif speech == 'я тебя люблю':
            print('Я тебя тоже)')
        elif speech == 'спасибо':
            print('Всегда рад помочь')
        elif speech == 'пока':
            print('До скорого :)')
            print(f"Вы сказали: {speech}")
            break
        print(f"Вы сказали: {speech}")


def calculator(event):
    def calculate():
        global stack
        result = 0
        operand2 = Decimal(stack.pop())
        operation = stack.pop()
        operand1 = Decimal(stack.pop())
        if operation == '+':
            result = operand1 + operand2
        if operation == '-':
            result = operand1 - operand2
        if operation == '/':
            result = operand1 / operand2
        if operation == '*':
            result = operand1 * operand2
        if operation == '**':
            result = operand1 ** operand2
        label.configure(text=str(result))

    def click(text):
        global activeStr
        global stack
        if text == 'CE':
            stack.clear()
            activeStr = ''
            label.configure(text='0')
        elif '0' <= text <= '9':
            activeStr += text
            label.configure(text=activeStr)
        elif text == '.':
            if activeStr.find('.') == -1:
                activeStr += text
                label.configure(text=activeStr)
        else:
            if len(stack) >= 2:
                stack.append(label['text'])
                calculate()
                stack.clear()
                stack.append(label['text'])
                activeStr = ''
                if text != '=':
                    stack.append(text)
            else:
                if text != '=':
                    stack.append(label['text'])
                    stack.append(text)
                    activeStr = ''
                    label.configure(text='0')

    calcul = Tk()
    label = Label(calcul, text='0', width=35)
    label.grid(row=0, column=0, columnspan=4, sticky="nsew")
    calcul.title('Калькулятор')
    calcul.resizable(False, False)
    buttons = (('7', '8', '9', '/', '4'),
               ('4', '5', '6', '*', '4'),
               ('1', '2', '3', '-', '4'),
               ('0', '.', '=', '+', '4'))
    button = Button(calcul, text='CE', command=lambda text='CE': click(text))
    button.grid(row=1, column=3, sticky="nsew")
    for row1 in range(4):
        for col1 in range(4):
            button = Button(calcul, text=buttons[row1][col1], command=lambda row=row1,
                            col=col1: click(buttons[row][col]))
            button.grid(row=row1 + 2, column=col1, sticky="nsew")
    calcul.grid_rowconfigure(6, weight=1)
    calcul.grid_columnconfigure(4, weight=1)
    calcul.mainloop()


def ballgame(event):
    global window
    window.title('Отбей мяч')
    window.geometry('500x400')
    window.resizable(False, False)
    window.wm_attributes('-topmost', 1)
    canvass = Canvas(window, width=500, height=400)
    canvass.pack()
    platformm = Platform(canvass, 'green')
    ball = Ball(canvass, 'red', platformm)
    while not ball.get_end():
        ball.draw()
        platformm.draw()
        window.update()
        time.sleep(0.01)
    window.destroy()


def dragongame(event):
    global window
    window.title('Драконы')
    w = 600
    h = 600
    window.geometry(str(w) + 'x' + str(h))
    canvas = Canvas(window, width=h, height=h)
    canvas.place(in_=window, x=0, y=0)
    bg_photo = PhotoImage(file='bg_2.png')
    knight = Knight()
    dragons = []
    for i in range(3):
        dragons.append(Dragon())

    def game():
        global window
        canvas.delete('all')
        canvas.create_image(300, 300, image=bg_photo)
        canvas.create_image(knight.x, knight.y, image=knight.photo)
        # условие, чтобы рыцарь не вылетал за рамки
        if 100 > knight.y:
            knight.y = 100
        elif 500 < knight.y:
            knight.y = 500
        if 70 > knight.x:
            knight.x = 70
        elif 500 < knight.x:
            knight.x = 500
        current_dragon = 0
        dragon_to_kill = -1

        for dragon in dragons:
            global window
            dragon.x -= dragon.v
            canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
            # Проверка столкновений
            if (dragon.x - knight.x) ** 2 + (dragon.y - knight.y) ** 2 <= 96 ** 2:
                dragon_to_kill = current_dragon
            current_dragon += 1

            if dragon.x <= 0:
                canvas.delete('all')
                canvas.create_text(w // 2, h // 2, text="You lose!", font="Verdana 42", fill='red')
                break

        if dragon_to_kill >= 0:
            del dragons[dragon_to_kill]

        # Условие выигрыша
        if len(dragons) == 0:
            canvas.delete('all')
            canvas.create_text(w // 2, h // 2, text="You win!", font="Verdana 42", fill='red')
        else:
            window.after(5, game)

    game()
    window.bind('<Key-Up>', knight.up)
    window.bind('<Key-Down>', knight.down)
    window.bind('<Key-Left>', knight.left)
    window.bind('<Key-Right>', knight.right)
    window.bind('<KeyRelease>', knight.stop)
    window.mainloop()


def love(event):
    global heart
    new = Toplevel()
    new.title('Тебе')
    heart1 = PhotoImage(file='heart.png')
    heartlab = Label(new, image=heart1)
    heartlab.image = heart1
    heartlab.place(x=0, y=0)
    heartlab.pack()


window = Tk()
window.geometry('750x600')
window.resizable(width=False, height=False)
window.title('Project')
calend = PhotoImage(file='Calendar1.png')
label1 = Label(image=calend, bg='black')
label1.image = calend
label1.place(x=50, y=50)
label1.bind('<Button-1>', calendfunc)
voice = PhotoImage(file='Micro1.png')
label2 = Label(image=voice, bg='black')
label2.image = voice
label2.place(x=301, y=50)
label2.bind('<Button-1>', speech_rec)
calc = PhotoImage(file='Calculator1.png')
label3 = Label(image=calc, bg='black')
label3.image = calc
label3.place(x=552, y=50)
label3.bind('<Button-1>', calculator)
ballPlatform = PhotoImage(file='Ball1.png')
label4 = Label(image=ballPlatform, bg='black')
label4.image = ballPlatform
label4.place(x=50, y=382)
label4.bind('<Button-1>', ballgame)
sword = PhotoImage(file='Sword1.png')
label5 = Label(image=sword, bg='black')
label5.image = sword
label5.place(x=552, y=382)
label5.bind('<Button-1>', dragongame)
heart = PhotoImage(file='heart_1.png')
label5 = Label(image=heart, bg='black')
label5.image = heart
label5.place(x=301, y=382)
label5.bind('<Button-1>', love)
greet = Label(text='Привет! Здесь собрано несколько игр и приложений, ', font=['Courier Font', 18])
greet1 = Label(text=' которые могут тебе пригодиться.', font=['Courier Font', 18])
greet2 = Label(text=' Надеюсь, они будут тебе полезны =)', font=['Courier Font', 18])
greet.place(x=10, y=240, width=730, height=40)
greet1.place(x=10, y=280, width=730, height=40)
greet2.place(x=10, y=320, width=730, height=40)
window.mainloop()
