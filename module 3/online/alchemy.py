from tkinter import *
from random import randint
window = Tk()
window.geometry('600x600')


class Clay:
    image = PhotoImage(file='free-icon-pottery-7942410.png').subsample(4, 4)


class Dust:
    image = PhotoImage(file='free-icon-dust-2396941.png').subsample(4, 4)


class Aroma:
    image = PhotoImage(file='aroma.png').subsample(4, 4)


class Plant:
    image = PhotoImage(file='plant.png').subsample(4, 4)


class Lightning:
    image = PhotoImage(file='lightning.png').subsample(4, 4)


class Coal:
    image = PhotoImage(file='coal.png').subsample(4, 4)


class Cloud:
    image = PhotoImage(file='cloud.png').subsample(4, 4)


class Rain:
    image = PhotoImage(file='rain.png').subsample(4, 4)


class Fire:
    image = PhotoImage(file='free-icon-fire-9509865.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay()
        elif isinstance(other, Water):
            return Aroma()
        elif isinstance(other, Plant):
            return Coal()
        elif isinstance(other, Rain):
            return Lightning()


class Water:
    image = PhotoImage(file='free-icon-water-drop-4246703.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Cloud):
            return Rain()


class Wind:
    image = PhotoImage(file='wind.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Cloud()


class Earth:
    image = PhotoImage(file='ground.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust()
        elif isinstance(other, Water):
            return Plant()


canvas = Canvas(window, width=600, height=600)
canvas.pack()
elements = [Fire(), Earth(), Wind(), Water()]
for elem in elements:
    img = canvas.create_image(randint(50, 550), randint(50, 550), image=elem.image)


def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(images_id) == 2:
        elem_id1, elem_id2 = images_id[0], images_id[1]
        elememt1 = elements[elem_id1-1]
        elememt2 = elements[elem_id2-1]
        new_element = elememt1 + elememt2
        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x, event.y, image=new_element.image)
                elements.append(new_element)
                print(elements)
    canvas.coords(images_id, event.x, event.y)


window.bind('<B1-Motion>', move)
window.mainloop()
