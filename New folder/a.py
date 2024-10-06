import turtle

turtle.Screen().bgcolor("aqua")

turtle.Screen().setup(800,800)

square = turtle.Turtle()

square.pendown()

for i in range(5):
    square.forward(200)
    square.right(144)


turtle.done()
