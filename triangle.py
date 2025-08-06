import turtle

def draw_triangle(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

turtle.bgcolor("white")
turtle.title("Equilateral Triangles")

t = turtle.Turtle()
t.pensize(5)
t.pencolor("black")

draw_triangle(t, 200, "yellow")

t.penup()
t.backward(200)
t.pendown()
draw_triangle(t, 150, "orange")

t.penup()
t.backward(200)
t.pendown()
draw_triangle(t, 100, "red")

turtle.done()
