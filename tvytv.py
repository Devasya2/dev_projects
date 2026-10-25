import math
import random
import turtle

t = turtle.Turtle()
t.hideturtle()
ts = t.getscreen()


def draw_rec(x0, y0, x1, y1):
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.goto(x1, y1)


def draw_reca(x0, y0, len, hgt, clr):
    t.speed(0)
    t.fillcolor(clr)
    t.begin_fill()
    draw_rec(x0, y0, x0 + len, y0)
    draw_rec(x0 + len, y0, x0 + len, y0 + hgt)
    draw_rec(x0 + len, y0 + hgt, x0, y0 + hgt)
    draw_rec(x0, y0 + hgt, x0, y0)
    t.end_fill()


ts.tracer(0)

Pixel_Size = 15
Row = int(ts.window_height() // Pixel_Size)
Column = int(ts.window_width() // Pixel_Size)

Sx = -ts.window_width() / 2
Sy = ts.window_height() / 2

sun_row = Row // 3 
sun_col = Column // 2  
sun_radius = 5

for ky in range(Row):
    y_pos = Sy - (ky * Pixel_Size)

    for kx in range(Column):
        x_pos = Sx + (kx * Pixel_Size)  

        distance_to_sun = math.sqrt((ky - sun_row) ** 2 + (kx - sun_col) ** 2)

        if distance_to_sun <= sun_radius:
            clr = "yellow"
        elif ky < 3:
            clr = "#2b093d"
        elif ky < 7:
            clr = "#6a1b9a"
        elif ky < 12:
            clr = "#d81b60"
        elif ky < 16:
            clr = "#ff7043"
        elif ky < 19:
            clr = "#ffca28"
        elif ky == 19:
            clr = "#111111"
        else:
            if (ky + kx) % 2 == 0:
                clr = "#004d40"
            else:
                clr = "#00695c"

        draw_reca(x_pos, y_pos, Pixel_Size, Pixel_Size, clr)

ts.update()
ts.mainloop()