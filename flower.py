import turtle
def draw_petal(t, radius, arc_angle):
    for _ in range(2):
        t.circle(radius, arc_angle)
        t.left(180 - arc_angle)
n=int(input("Enter no of petals:"))
t = turtle.Turtle()
t.pensize(2)
t.color("black")
t.up()
t.goto(0, 0)
t.down()
petals = n
radius = 60
arc_angle = 60
for _ in range(petals):
    draw_petal(t, radius, arc_angle)
    t.left(360 / petals)
turtle.done()

