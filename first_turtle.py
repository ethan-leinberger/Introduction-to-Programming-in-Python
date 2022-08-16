import turtle


turtle.setup(700, 600)
turtle.title('My First Turtle Drawing')

turtle.speed(10)

turtle.forward(200)
turtle.right(90)
turtle.forward(100)

turtle.pensize(4)
turtle.pencolor('red')
turtle.right(45)
turtle.forward(200)

turtle.setheading(90)
turtle.pencolor('green')
turtle.forward(400)

turtle.setheading(200)
turtle.pencolor('cyan')
turtle.forward(200)

turtle.setheading(-45)
turtle.pencolor('mediumaquamarine')
turtle.forward(200)

turtle.penup()
turtle.goto(-250, 150)
turtle.pendown()
turtle.forward(100)

turtle.penup()
turtle.goto(-200, -200)
turtle.setheading(45)
turtle.pencolor('blue')
turtle.pendown()
turtle.dot()
turtle.forward(100)
turtle.dot()

turtle.penup()
turtle.goto(-200, -100)
turtle.pendown()
turtle.circle(30)

turtle.penup()
turtle.goto(-100, 150)
turtle.pendown()
turtle.circle(70, extent=180)

turtle.penup()
turtle.goto(100, 250)
turtle.pendown()
turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()





turtle.done()