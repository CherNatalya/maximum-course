from tkinter import *
window = Tk()
window.geometry('800x600')
# создаём холст
canvas = Canvas(window, width=800, height=600, bg='white')
# закрепляем
canvas.pack()
'''# квадрат
canvas.create_rectangle(30, 30, 110, 110, fill='yellow', outline='black')
# треугольник
canvas.create_polygon(30, 30, 70, 10, 110, 30)
canvas.create_rectangle(50, 60, 90, 80, fill='SkyBlue1')
canvas.create_line(70, 60, 70, 80)'''


'''class Car:
    # инициализатор - метод, который срабатывает сразу
    def __init__(self, speed, colour):
        self.speed = speed
        self.colour = colour
        print("Создал объект")
    # метод

    def bibi(self):
        print('beep')
# экземпляр класса


bmw = Car(210, 'red')
bmw.bibi()
audi = Car(220, 'black')
audi.bibi()'''


class House:
    def __init__(self, roof_colour, wall_colour, number):
        self.roof_colour = roof_colour
        self.wall_colour = wall_colour
        self.number = number
        self.height = 130
        self.width = 140
        self.wall = None
        self.roof = None

    def build_house(self, x, y):
        h = self.height
        w = self.width
        self.roof = canvas.create_polygon(x, y,
                                          x + w, y,
                                          x + w/2, h - 100,
                                          fill=self.roof_colour,
                                          outline='')
        self.wall = canvas.create_rectangle(x + 20, y,
                                            x + 120, y + 100,
                                            fill=self.wall_colour,
                                            outline='')

    def print_info(self):
        print(f'Номер дома: {self.number} \nЦвет крыши: {self.roof_colour} \nЦвет стен: {self.wall_colour}')


house1 = House('black', 'blue', 1)
house1.build_house(50, 80)
house1.print_info()
window.mainloop()
