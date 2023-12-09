def setup():
    # Set the size of your sketch
    size(500, 500)
    background(136, 136, 136)
    pass

def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    s = 400
    r = 400
    for q in range(10):
        if q % 2 == 0:
            fill(0, 0, 0)
        else:
            fill(255, 255, 255)
        ellipse(250, 250, s, s)
        s = s - 40
        r = r - 40


    
    # Use an if statement and modulo to alternate the color of your rings
    
    
    pass
