import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    import turtle
    q = turtle
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    for e in range(120):
        q.speed(9)
        q.forward(200)
        q.right(90)
        q.forward(200)
        q.right(90)
        q.forward(200)
        q.right(90)
        q.forward(200)
        q.right(90)
    #      3) Set the pen width to 10
        q.pensize(10)
    #      4) Ask the user what color pen they would like to draw with
        w = simpledialog.askstring(title=None, prompt="what color pen you want?(red, yellow, green, or blue)")
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
        if w == "red":
            r = 1
        if w == "yellow":
            r = 2
        if w == "green":
            r = 3
        if w == "blue":
            r = 4
        elif w == "":
            r = random.randint(1, 4)
    #      6) If the user doesn't enter anything, choose a random color

        if r == 1:
            q.pencolor('red')
        if r == 2:
            q.pencolor('yellow')
        if r == 3:
            q.pencolor('green')
        if r == 4:
            q.pencolor('blue')
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
