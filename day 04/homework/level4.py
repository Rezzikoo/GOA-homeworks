import turtle

# Initialize the screen and turtle
screen = turtle.Screen()
screen.title("Palace with GOA Flag")
screen.bgcolor("skyblue")

# Create the turtle for drawing
pen = turtle.Turtle()
pen.speed(10)

# Function to draw a rectangle (used for the palace structure)
def draw_rectangle(t, width, height, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw a window
def draw_window(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    draw_rectangle(pen, 30, 30, "lightblue")
    # Draw window panes
    pen.color("black")
    pen.penup()
    pen.goto(x + 15, y)
    pen.pendown()
    pen.goto(x + 15, y + 30)
    pen.penup()
    pen.goto(x, y + 15)
    pen.pendown()
    pen.goto(x + 30, y + 15)

# Function to draw the palace
def draw_palace():
    pen.penup()
    pen.goto(-150, -100)
    pen.pendown()
    draw_rectangle(pen, 300, 200, "lightgray")
    
    # Draw the left tower
    pen.penup()
    pen.goto(-200, 100)
    pen.pendown()
    draw_rectangle(pen, 50, 150, "gray")
    
    # Draw the right tower
    pen.penup()
    pen.goto(150, 100)
    pen.pendown()
    draw_rectangle(pen, 50, 150, "gray")
    
    # Draw the main roof
    pen.penup()
    pen.goto(-200, 100)
    pen.pendown()
    pen.color("red")
    pen.begin_fill()
    pen.goto(0, 200)
    pen.goto(200, 100)
    pen.goto(-200, 100)
    pen.end_fill()
    
    # Draw tower roofs
    pen.penup()
    pen.goto(-225, 250)
    pen.pendown()
    pen.color("darkred")
    pen.begin_fill()
    pen.goto(-175, 300)
    pen.goto(-125, 250)
    pen.goto(-225, 250)
    pen.end_fill()
    
    pen.penup()
    pen.goto(175, 250)
    pen.pendown()
    pen.begin_fill()
    pen.goto(225, 300)
    pen.goto(275, 250)
    pen.goto(175, 250)
    pen.end_fill()

    # Draw windows on the main palace
    for i in range(-120, 140, 80):
        draw_window(i, 20)
    
    for i in range(-120, 140, 80):
        draw_window(i, -40)
    
    # Draw windows on the left tower
    draw_window(-185, 180)
    draw_window(-185, 120)
    
    # Draw windows on the right tower
    draw_window(165, 180)
    draw_window(165, 120)

# Function to draw the flag
def draw_flag():
    pen.penup()
    pen.goto(175, 300)
    pen.pendown()
    pen.color("black")
    pen.left(90)
    pen.forward(60)
    pen.right(90)
    draw_rectangle(pen, 40, 30, "green")

    # Draw GOA text on flag (simplified)
    pen.penup()
    pen.goto(180, 310)
    pen.pendown()
    pen.color("white")
    pen.write("GOA", font=("Arial", 12, "bold"))

# Function to draw a simple king and queen
def draw_king_queen():
    # Draw the king
    pen.penup()
    pen.goto(-50, -100)
    pen.pendown()
    pen.color("blue")
    pen.circle(10)  # King head
    pen.penup()
    pen.goto(-50, -110)
    pen.pendown()
    draw_rectangle(pen, 20, 40, "blue")  # King body
    pen.penup()
    pen.goto(-55, -70)
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    pen.goto(-50, -60)  # King crown
    pen.goto(-45, -70)
    pen.goto(-55, -70)
    pen.end_fill()
    
    # Draw the queen
    pen.penup()
    pen.goto(50, -100)
    pen.pendown()
    pen.color("purple")
    pen.circle(10)  # Queen head
    pen.penup()
    pen.goto(50, -110)
    pen.pendown()
    draw_rectangle(pen, 20, 40, "purple")  # Queen body
    pen.penup()
    pen.goto(45, -70)
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    pen.goto(50, -60)  # Queen crown
    pen.goto(55, -70)
    pen.goto(45, -70)
    pen.end_fill()

# Draw the palace, flag, and king & queen
draw_palace()
draw_flag()
draw_king_queen()

# Hide the turtle and display the window
pen.hideturtle()
turtle.done()