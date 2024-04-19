from tkinter import *
from tkinter import font # vajalik teksti fondi miitmiseks
from random import *
import tkinter as tk
import time
import random

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width= 1000, height = 1000, background = 'white')
tahvel.grid()

# Üksik kriips (x0, y0, x1, y1)
tahvel.create_line(30, 40, 300, 40)

# Ühendatud kriipsud (Suvaline arv koordinaatide paare)
tahvel.create_line(30,60,  300,6,   300,100,    60,100)

tahvel.create_line(30, 150, 300, 150, width=5, dash=(5,1,2,1), arrow=LAST)

tahvel.create_line(30,160, 300, 160, 300, 200, 60, 200, fill="red")

tahvel.create_polygon(30, 160, 300, 160, 300, 200, 60, 200, fill="green")

tahvel.create_rectangle(30, 260, 300,300)

tahvel.create_oval(30, 260, 300,300, width= 2, outline = 'red', fill = 'wheat')

tahvel.create_oval(330, 330, 400,400, fill="gray", activefill="pink")

suur_font = font.Font(family='Helvetica', size=32, weight='bold')
tahvel.create_text(30, 500, text='Tere!', font=suur_font, anchor = NW)

colors = ['red', 'green', 'blue', 'gold', 'orange', 'purple', 'lightgreen', 'lightblue']

def rainbow_oval():


    root = tk.Tk()
    root.title("Rainbow Oval")
    root.geometry("800x800")
    canvas = tk.Canvas(root, width=800, height=800, bg="white")
    canvas.pack()
    x0 = 0
    y0 = 0
    x1 = 600
    y1 = 600
    p = 5
    for i in range(55):
        x0 += p
        y0 += p
        x1 -= p
        y1 -= p
        canvas.create_oval(x0, y0, x1, y1, fill=choice(colors))

    root.mainloop()

def circle_in_square():
    """ Draw a circle in the square

    :return:
    """
    root = tk.Tk()
    root.title("Круг в квадрате")
    root.geometry("1000x1000")
    canvas = tk.Canvas(root, width=800, height=800, bg="white")
    canvas.pack()
    x0 = 0
    y0 = 0
    x1 = 600
    y1 = 600
    p = 0
    x_ = 600
    y_ = 600
    for i in range(20):
        x0 += p
        y0 += p
        x1 -= p
        y1 -= p
        canvas.create_rectangle(x0, y0, x1, y1, fill=choice(colors))
        canvas.create_oval(x0, y0, x1, y1, fill=choice(colors))
        x_ -= 2 * p
        y_ -= 2 * p
        p = int(((x_ ** 2+y_ ** 2) **(1/2) - x_)/2)
        p = int(((p**2) / 2) ** (1/2))


    root.mainloop()

def Estonian_flag():
    """ Estonian flag

    :return:
    """
    root = tk.Tk()
    root.title("Estonian Flag")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack()

    width = 300
    height = 200
    stripe_height = height // 3

    # Верхняя синяя полоса
    canvas.create_rectangle(0, 0, width, stripe_height, fill="#0072CE", outline="")

    # Средняя черная полоса
    canvas.create_rectangle(0, stripe_height, width, 2 * stripe_height, fill="#000000", outline="")

    # Нижняя белая полоса
    canvas.create_rectangle(0, 2 * stripe_height, width, height, fill="#FFFFFF", outline="")

    root.mainloop()


def bahama_flag():
    """ bahama flag

    """

    root = tk.Tk()
    root.title("Bahama Flag")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack()

    width = 300
    height = 200
    stripe_height = height // 3

    canvas.create_rectangle(0, 0, width, stripe_height, fill = "#00CED1", outline="")
    canvas.create_rectangle(0, stripe_height, width, 2 * stripe_height, fill = "gold", outline="")
    canvas.create_rectangle(0, 2 * stripe_height, width, height, fill = "#00CED1", outline="")
    points = [0, 0, width - 140, height / 2, 0, height]
    canvas.create_polygon(points, outline="",
                     fill='black', width=3)


    root.mainloop()


def belgian_flag():
    """ Belgian Flag

    :return:
    """
    root = tk.Tk()
    root.title("Belgian Flag")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack()

    width = 300
    height = 200
    stripe_width = width // 3

    # Черная полоса
    canvas.create_rectangle(0, 0, stripe_width, height, fill="#000000", outline="")

    # Желтая полоса
    canvas.create_rectangle(stripe_width, 0, 2 * stripe_width, height, fill="#FFD700", outline="")

    # Красная полоса
    canvas.create_rectangle(2 * stripe_width, 0, width, height, fill="#FF0000", outline="")

    root.mainloop()




def english_flag():
    """ English flag

    :return:
    """
    root = tk.Tk()
    root.title("English Flag")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack()

    width = 300
    height = 200


    canvas.create_rectangle(0, 0, width, height, fill="white", outline="")

    # Размеры креста
    cross_width = width // 5
    cross_height = height // 15

    # Вертикальная полоса креста
    canvas.create_rectangle((width - cross_width) // 2, 0, (width + cross_width) // 2, height, fill="red", outline="")

    # Горизонтальная полоса креста
    canvas.create_rectangle(0, (height - cross_height) // 2, width, (height + cross_height) // 1.7, fill="red", outline="")

    root.mainloop()



def valgusfoor():
    """Valgusfoor"""

    root = tk.Tk()
    root.title("ValgusFoor")
    root.geometry("300x600")
    canvas = tk.Canvas(root, width=300, height=600, bg="white")
    canvas.pack()

    def blink():
        nonlocal red_light, yellow_light, green_light
        if canvas.itemcget(red_light, "fill") == "grey":
            canvas.itemconfig(red_light, fill="red")
            canvas.itemconfig(yellow_light, fill="grey")
            canvas.itemconfig(green_light, fill="grey")
        elif canvas.itemcget(yellow_light, "fill") == "grey":
            canvas.itemconfig(red_light, fill="grey")
            canvas.itemconfig(yellow_light, fill="yellow")
            canvas.itemconfig(green_light, fill="grey")
        else:
            canvas.itemconfig(red_light, fill="grey")
            canvas.itemconfig(yellow_light, fill="grey")
            canvas.itemconfig(green_light, fill="green")

        root.after(1000, blink)

        root.after(1000, blink)

    root.after(1000, blink)


    square_side = 80
    square_x1 = (300 - square_side) / 2
    square_y1 = (100 - square_side) / 2
    square_x2 = square_x1 + square_side
    square_y2 = square_y1 + square_side
    red_light = canvas.create_oval(square_x1, square_y1, square_x2, square_y2, fill="grey")

    square2_side = 80
    square2_x1 = (300 - square_side) / 2
    square2_y1 = (285 - square_side) / 2
    square2_x2 = square2_x1 + square2_side
    square2_y2 = square2_y1 + square2_side
    yellow_light = canvas.create_oval(square2_x1, square2_y1, square2_x2, square2_y2, fill="grey")

    square3_side = 80
    square3_x1 = (300 - square_side) / 2
    square3_y1 = (470 - square_side) / 2
    square3_x2 = square3_x1 + square3_side
    square3_y2 = square3_y1 + square3_side
    green_light = canvas.create_oval(square3_x1, square3_y1, square3_x2, square3_y2, fill="grey")

    stick_side = 10

    stick_x1 = (300 - stick_side) / 2
    stick_y1 = (600 - stick_side) / 2
    stick_x2 = stick_x1 + stick_side
    stick_y2 = stick_y1 + stick_side * 20
    stick = canvas.create_rectangle(stick_x1, stick_y1, stick_x2, stick_y2, fill="black")

    horizontal_stick_side = 10
    horizontal_stick_x1 = (50 - horizontal_stick_side) / 2
    horizontal_stick_y1 = (1060 - horizontal_stick_side) / 2
    horizontal_stick_x2 = horizontal_stick_x1 + horizontal_stick_side * 25
    horizontal_stick_y2 = horizontal_stick_y1 + horizontal_stick_side
    horizontal_stick = canvas.create_rectangle(horizontal_stick_x1, horizontal_stick_y1, horizontal_stick_x2,
                                               horizontal_stick_y2, fill="black")
    current_light = "red"
    blink()
    root.mainloop()




def chess():

    root = tk.Tk()
    root.title("Chess")
    canvas = tk.Canvas(root, width=800, height=800, bg="white")
    canvas.pack()

    canvas.delete("all")
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = "#FFFFFF"
            else:
                color = "#000000"
            canvas.create_rectangle(j * 25, i * 25, (j + 1) * 25, (i + 1) * 25, fill=color)


    root.mainloop()


var = IntVar()
ovall = Radiobutton(raam, text='Ovall', variable = var, value = 1,font = suur_font, command= rainbow_oval)
square = Radiobutton(raam, text='Square', variable = var, value = 2, font = suur_font, command=circle_in_square)
estonia = Radiobutton(raam, text='Estonian Flag', variable = var, value = 3, font = suur_font, command=Estonian_flag)
belgia = Radiobutton(raam, text='Belgian Flag', variable = var, value = 4, font = suur_font, command=belgian_flag)
english = Radiobutton(raam, text='English Flag', variable = var, value = 5, font = suur_font, command=english_flag)
valgusfoor = Radiobutton(raam, text='Valgusfoor', variable = var, value =6, font = suur_font, command=valgusfoor)
bahama = Radiobutton(raam, text='Bahama', variable=var, value = 7, font = suur_font, command=bahama_flag)
chess = Radiobutton(raam, text='Chess', variable=var, value = 8, font = suur_font, command=chess)

ovall.place(x = 400, y = 450)
square.place(x = 400, y = 520)
estonia.place(x = 400, y = 380)
belgia.place(x = 400, y = 590)
english.place(x = 400, y = 660)
valgusfoor.place(x = 400, y = 720)
bahama.place(x = 400, y = 790)
chess.place(x = 400, y = 860)

raam.mainloop()