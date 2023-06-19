from tkinter import *
import random


class Knight:
    def __init__(self):
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
        self.y = random.randint(100, 500)
        self.v = random.randint(1, 3)
        self.photo = PhotoImage(file='dragon.png')


window = Tk()
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
        dragon.x -= dragon.v
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
        # Проверка столкновений
        if (dragon.x-knight.x)**2 + (dragon.y - knight.y)**2 <= 96**2:
            dragon_to_kill = current_dragon

        current_dragon += 1

        if dragon.x <= 0:
            canvas.delete('all')
            canvas.create_text(w//2, h//2, text="You lose!", font="Verdana 42", fill='red')
            break

    if dragon_to_kill >= 0:
        del dragons[dragon_to_kill]

    # Условие выигрыша
    if len(dragons) == 0:
        canvas.delete('all')
        canvas.create_text(w//2, h//2, text="You win!", font="Verdana 42", fill='red')
    else:
        window.after(5, game)


game()
# привязываем событие к функции
window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<Key-Left>', knight.left)
window.bind('<Key-Right>', knight.right)
window.bind('<KeyRelease>', knight.stop)

window.mainloop()
