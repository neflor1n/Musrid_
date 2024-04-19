from tkinter import *
from tkinter import font # vajalik teksti fondi miitmiseks


raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width= 600, height = 600, background = 'white')
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

raam.mainloop()