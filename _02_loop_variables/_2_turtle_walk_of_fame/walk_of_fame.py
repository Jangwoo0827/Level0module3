import turtle
q = turtle
if __name__ == '__main__':

    q = turtle.Turtle()
    q.shape('turtle')
    q.color('blue', 'green')
    q.speed(100)
    x = -400
    # TODO 1) Set the X position of the turtle so that it starts on the left.
    q.penup()
    q.goto(x, 0)
    q.pendown()
    # TODO 2) Make the turtle draw a star shape. Hint: angle=144.
    for i in range(9):
        q.forward(30)
        q.right(144)
        q.forward(30)
        q.right(144)
        q.forward(30)
        q.right(144)
        q.forward(30)
        q.right(144)
        q.forward(30)
        q.right(144)
        q.forward(30)
        q.right(144)
        q.forward(30)
        q.right(144)
        q.forward(30)
        q.right(144)
        q.left(90)
        q.penup()
        x = x + 50
        q.goto(x, 0)
        q.pendown()

    # TODO 3) Set the length of each line in the star to 30

    # TODO: CHALLENGE
    #       Make the turtle draw a line of stars like the image in
    #       this folder.
    #       Hint: The distance between stars is 50.

# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
