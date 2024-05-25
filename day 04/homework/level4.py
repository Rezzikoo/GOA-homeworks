import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")

pen = turtle.Turtle()
pen.color("black")
pen.speed(40)


pen.penup()
pen.goto(-200, -100)
pen.pendown()
pen.begin_fill()
pen.color("gray")
for _ in range(2):
    pen.forward(400)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
pen.end_fill()


pen.penup()
pen.goto(-200, 100)
pen.pendown()
pen.begin_fill()
pen.color("gray")
for _ in range(2):
    pen.forward(80)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
pen.end_fill()


pen.penup()
pen.goto(120, 100)
pen.pendown()
pen.begin_fill()
pen.color("gray")
for _ in range(2):
    pen.forward(80)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
pen.end_fill()


pen.penup()
pen.goto(100, 100)
pen.pendown()
pen.begin_fill()
pen.color("red")
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(200)
pen.end_fill()


pen.penup()
pen.goto(-200, 300)
pen.pendown()
pen.begin_fill()
pen.color("red")
pen.goto(-160, 360)
pen.goto(-120, 300)
pen.goto(-200, 300)
pen.end_fill()


pen.penup()
pen.goto(120, 300)
pen.pendown()
pen.begin_fill()
pen.color("red")
pen.goto(160, 360)
pen.goto(200, 300)
pen.goto(120, 300)
pen.end_fill()


pen.begin_fill()
pen.color("green")


pen.penup()
pen.goto(-200, 300)
pen.pendown()
pen.forward(100)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(50)


pen.penup()
pen.goto(100, 100)
pen.pendown()
pen.begin_fill()
pen.color("pink")
pen.circle(19)
pen.end_fill()



pen.penup()
pen.goto(-100, 100)
pen.pendown()
pen.begin_fill()
pen.color("pink")
pen.circle(19)
pen.end_fill()



pen.hideturtle()
turtle.done()