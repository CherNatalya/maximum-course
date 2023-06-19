from tkinter import*
import random
import emoji
window = Tk()
window.geometry('700x500')
window.title('Кликер')
points1 = 0
points2 = 0


def check1():
    global points1
    b1.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points1 += 1
    label1['text'] = points1
    if points1 >= 10 and points2 == 0:
        b2['text'] = str('Ну пожалуйста' + emoji.emojize(':slightly_frowning_face:'))
    else:
        b2['text'] = 'нажми меня'
        b1['text'] = 'нажми меня'


def check2():
    global points2
    b2.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points2 += 1
    label2['text'] = points2
    if points2 >= 10 and points1 == 0:
        b1['text'] = str('Ну пожалуйста' + emoji.emojize(':slightly_frowning_face:'))
    else:
        b1['text'] = 'нажми меня'
        b2['text'] = 'нажми меня'


b1 = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check1)
b2 = Button(text='нажми меня', font=('Arial', 20), fg='medium blue', command=check2)
b1.place(x=100, y=130)
b2.place(x=300, y=260)
label1 = Label(text=points1, font=('Arial', 15), fg='black')
label2 = Label(text=points2, font=('Arial', 15), fg='medium blue')
label1.place(x=10, y=10)
label2.place(x=600, y=10)
window.mainloop()
