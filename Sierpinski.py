import turtle
import random
pen = turtle.Turtle()
pen.speed(0)


def draw(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.dot()

def Sierpinski():
    tri = [(0,250),(-250,-125),(250,-125)]
    others = []

    for point in tri:
        print(point[0])
        print(point[1])
        draw(point[0],point[1])

    for i in range(0,10000):
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
