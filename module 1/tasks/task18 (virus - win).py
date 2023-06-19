from tkinter import*
window = Tk()
window.config(bg='white')
window.geometry('750x600')
window.title('Выигрыш')


def on_close():
    pass


def win():
    button['text'] = 'Чтобы забрать выйгрыш необходимо внести 1000руб.'


text = Label(text='ВЫ ВЫИГРАЛИ В ЛОТЕРЕЕ!', fg='red', bg='white', font=['Arial', 39])
text.place(x=20, y=50, width=710, height=300)
button = Button(text='ПОЛУЧИТЬ ВЫИГРЫШ!', fg='white', bg='orange', font=['Monaco', 16], command=win)
button.place(x=50, y=300, width=650, height=100)
window.protocol('WM_DELETE_WINDOW', on_close)
window.mainloop()
