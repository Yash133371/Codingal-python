import turtle


s = turtle.Screen()
s.title("Hexagon")

t = turtle.Turtle()
t.pensize(10)

t.begin_fill()
for i in range(6):
    t.forward(100)
    t.left(60)
t.end_fill()

turtle.done()