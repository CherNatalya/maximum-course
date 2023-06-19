from tkinter import*
import random
import time
window = Tk()
window.config(bg='white')
window.geometry('850x600+-10+0')
window.title('Clicker')


def on_close():
    time.sleep(5)
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry(str(width) + 'x' + str(height))
    photo = PhotoImage(file='скелет.png')
    lab = Label(image=photo, bg='black')
    lab.image = photo
    lab.place(width=width, height=height, x=0, y=0)


def click():
    global points, b, b2
    b['bg'] = random.choice(['orange', 'red', 'black', 'blue', 'green', 'purple', 'yellow', 'deep pink', 'cyan'])
    points += 1
    label['text'] = points
    if points == 10:
        b['text'] = 'Зачем ты продолжаешь это делать?'
    elif points == 20:
        b['text'] = 'Ты точно хочешь продолжить?'
    elif points == 30:
        b['text'] = 'Ты ещё здесь?'
    elif points == 40:
        b2 = Button(text='Нажми меня =)', command=click2)
        b['text'] = 'Нажимай только на меня!'
        b2.place(x=300, y=260)
    elif points == 50:
        b['text'] = 'Ты почти у цели'
    elif points == 60:
        b['text'] = 'Ещё немного'
    elif points == 70:
        b['text'] = 'Вот и всё, теперь ты можешь закрыть это окно. Пока'
        b2.destroy()
        window.protocol('WM_DELETE_WINDOW', on_close)


def click2():
    global b, points, b2
    b['text'] = 'Я же говорила, теперь начинай заново'
    points = 0
    b2.destroy()


points = 0
answer = 0
b = Button(text='Нажми меня', font=('Arial', 20), fg='white', bg='black', command=click)
b2 = Button(text='Нажми меня =)')
b.place(x=100, y=130)
label = Label(text=points, font=('Arial', 15), fg='black')
label.place(x=10, y=10)
window.mainloop()
