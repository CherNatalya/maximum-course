from tkinter import *
from random import randint
window = Tk()
window.geometry('800x600')
canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()


class Spruce:
    def __init__(self, needles_colour, number):
        self.needles_colour = needles_colour
        self.width = 140
        self.height = 170
        self.number = number
        self.needles1 = None
        self.needles2 = None
        self.needles3 = None
        self.trunk = None
        self.x = None
        self.y = None

    def create_spruce(self, x, y):
        h = self.height
        w = self.width
        self.needles1 = canvas.create_polygon(x, y + h - 110,
                                              x + w, y + h - 110,
                                              x + w/2, y,
                                              fill=self.needles_colour,
                                              outline='')
        self.needles2 = canvas.create_polygon(x, y + h - 80,
                                              x + w, y + h - 80,
                                              x + w / 2, y + h - 140,
                                              fill=self.needles_colour,
                                              outline='')
        self.needles3 = canvas.create_polygon(x, y + h - 50,
                                              x + w, y + h - 50,
                                              x + w / 2, y + h - 110,
                                              fill=self.needles_colour,
                                              outline='')
        self.trunk = canvas.create_rectangle(x + 50, y + h - 50,
                                             x + 90, y + h,
                                             fill='brown',
                                             outline='')
        self.x = x
        self.y = y

    def hang_ball(self, colour):
        ball_x = randint(self.x, self.x + self.width)
        ball_y = randint(self.y + 40, self.y + self.height - 50)
        canvas.create_rectangle(ball_x, ball_y, ball_x + 20, ball_y + 20, fill=colour, outline='')

    def print_info(self):
        print(f'Номер дерева: {self.number} \nЦвет хвои: {self.needles_colour}')


spruce1 = Spruce('green', 1)
spruce1.create_spruce(50, 80)
spruce1.hang_ball('yellow')
spruce1.hang_ball('blue')
spruce1.hang_ball('purple')
spruce1.print_info()
window.mainloop()
