import turtle
import random
pen = turtle.Turtle()
pen.speed(0)

#draws a single point at the given coordinates
def draw(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.dot()

#makes the Sierpinski fractal
def Sierpinski():
    #the initial triangle and subsequent points
    tri = [(0,250),(-250,-125),(250,-125)]
    others = []
    
    #Draws the initial triangle
    for point in tri:
        draw(point[0],point[1])
    #Main loop that draws the sierpinski triangle with a given number of dots
    for i in range(0,10000):
        #If there are no other points, grab two points from the initial triangle. Got some W.E.T. code here
        if len(others)==0:
            firstPoint=random.randrange(0,3)
            secPoint=random.randrange(0,3)
            while secPoint == firstPoint:
                secPoint=random.randrange(0,3)

            midPoint=((tri[firstPoint][0]+tri[secPoint][0])/2,(tri[firstPoint][1]+tri[secPoint][1])/2)
            others.append(midPoint)

            draw(midPoint[0],midPoint[1])
        else:
            firstPoint = random.randrange(0,3)
            secPoint = others[-1]
            
            midPoint = ((tri[firstPoint][0]+secPoint[0])/2,(tri[firstPoint][1]+secPoint[1])/2)
            others.append(midPoint)

            draw(midPoint[0],midPoint[1])

Sierpinski()
