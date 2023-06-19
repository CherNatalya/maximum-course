from tkinter import*
window = Tk()
window.geometry('750x600+-10+0')
window.title('Computer virus')
window.config(bg='black')
window.resizable(width=False, height=False)


def on_close():
    if int(timer['text']) > 1:
        timer['text'] = int(timer['text']) - 1
        timer.place(x=350, y=90)
        window.after(1000, on_close)
    else:
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.geometry(str(width) + 'x' + str(height))
        photo = PhotoImage(file='скелет.png')
        label = Label(image=photo, bg='black')
        label.image = photo
        label.place(width=width, height=height, x=0, y=0)


text = Label(text='Your computer is infected!!1!!!1!1!!', fg='red', bg='black', font=['Ink Free', 40])
text.place(x=10, y=100, width=730, height=400)
window.protocol('WM_DELETE_WINDOW', on_close)
timer = Label(text='6', fg='red', bg='black', font=['Ink Free', 40])
window.mainloop()
