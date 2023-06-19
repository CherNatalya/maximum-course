from tkinter import*
window = Tk()
window.geometry('700x500')
window.title('Quiz')
facts = [
    {'text': 'Первый персональный компьютер появился в 1981 году', 'right': 1},
    {'text': 'Среднестатистический пользователь моргает 5 раз в минуту', 'right': 0},
    {'text': 'Первое электронное письмо было отправлено в 1971 году', 'right': 1}
]
num = 0
points = 0


def check():
    global num, points
    answer = var.get()
    if bool(answer) == facts[num]['right']:
        points += 1
    if num < len(facts) - 1:
        num += 1
        fact['text'] = facts[num]['text']
    else:
        points_label = Label(text=('Вы набрали ' + str(points) + ' балл(а)'),  font=('Times New Roman', 16))
        points_label.place(x=10, y=260)


label_title = Label(text='Тестирование по IT', font=('Times New Roman', 24), fg='white', bg='DeepSkyBlue2')
label_title.place(width=700, height=100, x=0, y=0)
fact = Message(text=facts[num]['text'], font=('Times New Roman', 16), width=680)
fact.place(x=10, y=130)
var = IntVar()
true = Radiobutton(text='Правда', variable=var, value=1)
true.place(x=10, y=170)
false = Radiobutton(text='Ложь', variable=var, value=0)
false.place(x=10, y=190)
button = Button(text='Ответить', font=('Times New Roman', 16), fg='white', bg='SeaGreen1', command=check)
button.place(x=10, y=220)
window.mainloop()
