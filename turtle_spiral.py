import turtle
import colorsys

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🌈 Hypnotic Turtle Spiral")

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Color palette
n = 36
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.forward(i * 2)
    t.left(59)
    h += 1/n
    if h > 1:
        h = 0

turtle.done()
