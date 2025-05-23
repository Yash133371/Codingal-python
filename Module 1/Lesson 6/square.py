import turtle

s = turtle.Screen()
s.title("Hello Turtle!")

t = turtle.Turtle()
t.pencolor("blue")
t.pensize(10)

for i in range(1, 5):
    t.forward(100)
    t.left(90)

turtle.done()