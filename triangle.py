import turtle

wn = turtle.Screen()
wn.bgcolor("white") 
wn.title("My Turtle equilateral triangle") 

my_turtle = turtle.Turtle()
my_turtle.pencolor("black") 
my_turtle.pensize(10) 
my_turtle.color("black")
my_turtle.fillcolor("violet")
my_turtle.begin_fill()


for _ in range(3): 
    my_turtle.forward(300) 
    my_turtle.left(120) 
my_turtle.end_fill()

my_turtle.penup()
my_turtle.backward(250)
my_turtle.pendown()
my_turtle.fillcolor("dark blue")
my_turtle.begin_fill()

for _ in range(3):
    my_turtle.forward(200)
    my_turtle.left(120)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.backward(150)
my_turtle.pendown()
my_turtle.fillcolor("blue")
my_turtle.begin_fill()

for _ in range(3):
    my_turtle.forward(100)
    my_turtle.left(120)
my_turtle.end_fill()

turtle.done()
