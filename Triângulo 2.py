import turtle
turtle.speed(0)
def triângulo(posx, posy,lado):
    turtle.showturtle()
    turtle.penup()
    turtle.goto(posx,posy)
    turtle.pendown()

    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)
        turtle.hideturtle()
    turtle.end_fill()

turtle.color('black', 'blue')
turtle.begin_fill()
triângulo(-650,200,150)

turtle.color('gray', 'purple')
turtle.begin_fill()
triângulo(-475,200,150)

turtle.color('blue', 'red')
turtle.begin_fill()
triângulo(-300,200,150)

turtle.color('red', 'green')
turtle.begin_fill()
triângulo(-125,200,150)

turtle.color('black', 'cyan')
turtle.begin_fill()
triângulo(50,200,150)

turtle.color('gray', 'yellow')
turtle.begin_fill()
triângulo(225,200,150)

turtle.color('purple', 'violet')
turtle.begin_fill()
triângulo(400,200,150)

turtle.color('yellow', 'magenta')
turtle.begin_fill()
triângulo(-650,25,150)

turtle.color('blue', 'gray')
turtle.begin_fill()
triângulo(-475,25,150)

turtle.color('blue', 'black')
turtle.begin_fill()
triângulo(-300,25,150)

turtle.color('gray', 'pink')
turtle.begin_fill()
triângulo(-125,25,150)

turtle.color('black', 'darkgreen')
turtle.begin_fill()
triângulo(50,25,150)

turtle.color('red', 'darkblue')
turtle.begin_fill()
triângulo(225,25,150)

turtle.color('yellow', 'darkgray')
turtle.begin_fill()
triângulo(400,25,150)

turtle.color('red', 'lightblue')
turtle.begin_fill()
triângulo(-650,-150,150)

turtle.color('lightblue', 'darkred')
turtle.begin_fill()
triângulo(-475,-150,150)

turtle.color('yellow', 'orange')
turtle.begin_fill()
triângulo(-300,-150,150)

turtle.color('black', 'lightgray')
turtle.begin_fill()
triângulo(-125,-150,150)

turtle.color('blue', 'darkcyan')
turtle.begin_fill()
triângulo(50,-150,150)

turtle.color('yellow', 'lightgreen')
turtle.begin_fill()
triângulo(225,-150,150)

turtle.color('green', 'darkorange')
turtle.begin_fill()
triângulo(400,-150,150)

turtle.done()