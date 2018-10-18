import turtle

def draw_square():
   # window screen
    window = turtle.Screen()
    window.bgcolor("red")
    #turtle class and methods
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("Green")
    brad.speed(2)
    #size of the circle and instructiona
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
# Making a circle
    bingo = turtle.Turtle()
    bingo.shape("arrow")
    bingo.color("blue")
    bingo.circle(100)

    window.exitonclick()
draw_square()