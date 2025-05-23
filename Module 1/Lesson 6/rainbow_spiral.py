import turtle

colors = ("red", "orange", "yellow", "blue", "cyan", "purple")

s = turtle.Screen()
s.title("Rainbow spiral")
s.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.pensize(10)

for i in range(1, 100):
    t.pencolor(colors[i % len(colors)])
    t.forward(i)
    t.left(15)

turtle.done()