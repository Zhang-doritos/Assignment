from turtle import *

def draw_spiral():
  # from turtle import *
    from random import randint
    bgcolor('black')
    x = 1
    speed(0)
    while x < 400:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        colormode(255)
        pencolor(r, g, b)
        fd(60 + x)
        rt(40)
        x = x + 1

    exitonclick()


print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for spiral)\n"
              "Your selection is: ")
    try:
        a = eval(a)
        if a == 1:
            draw_spiral()
        else:
            print("Please input the value in [1]")
    except:
        print("Please input the value in [1 ]")


