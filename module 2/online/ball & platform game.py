from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, color, platforma):
        self.__canvas = canvas
        self.__platforma = platforma
        self.__oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.__v_x = random.choice([-3, -2, -1, 1, 2, 3])
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


window = Tk()
window.title('Pong')
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
