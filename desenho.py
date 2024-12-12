import turtle 

def desenhar_steve(x=10, y=10, zoom=1.5):
    t = turtle.Turtle()
    t.speed(7)

    #cabeça 

    t.penup()
    t.goto(x + (-12 * zoom), y + (88+zoom))
    t.pendown()
    t.goto(x + (12 * zoom), y + (88*zoom))
    t.goto(x + (12 * zoom), y + (60*zoom))
    t.goto(x + (-12 * zoom), y + (60 * zoom))
    t.goto(x + (-12 * zoom), y + (88+zoom))

    #olho 1 

    t.penup()
    t.goto(x + (-8 * zoom), y + (78 * zoom))
    t.pendown()
    t.goto(x + (-8 + zoom), y + (75 * zoom))
    t.goto( x + (-5 * zoom), y + (75 * zoom))
    t.goto( x + (-5 * zoom), y + (78 * zoom))
    t.goto(x + (-8 * zoom), y + (78 * zoom))
    t.penup()
    t.goto(x + (-5 * zoom), y + (78 * zoom))
    t.pendown()
    t.goto(x + (-3 * zoom), y + (78 * zoom))
    t.goto(x + (-3 * zoom), y + (75 * zoom))
    t.goto(x + (-5 * zoom), y + (75 * zoom))

    #olho 2 
    t.penup()
    t.goto(x + 3 * zoom,y + 78 * zoom)
    t.pendown()
    t.goto(x + 3 * zoom,y + 75 * zoom)
    t.goto(x + 5 * zoom,y + 75 * zoom)
    t.goto(x + 5 * zoom,y + 78 * zoom)
    t.goto(x + 3 * zoom,y + 78 * zoom)
    t.penup()
    t.goto(x + 5 * zoom, y + 78 * zoom)
    t.pendown()
    t.goto(x + 8 * zoom, y + 78 * zoom)
    t.goto(x + 8 * zoom, y + 75 * zoom)
    t.goto(x + 5 * zoom, y + 75 * zoom)

    #corpo

    t.penup()
    t.goto(x + -20 * zoom, y + 60 * zoom)
    t.pendown()
    t.goto(x + 20 * zoom, y + 60 * zoom)
    t.goto(x + 20 * zoom, y + 0)
    t.goto(x + -20 * zoom, y + 0 * zoom)
    t.goto(x + -20 * zoom, y + 60 * zoom)

    #braços

    t.penup()
    t.goto(x + -35 * zoom, y *  35)
    t.pendown()
    t.goto(x + -35 * zoom, y + 60 * zoom)
    t.goto(x + -20 * zoom, y + 60 * zoom)
    t.goto(x + -20 * zoom, y + 35 * zoom)
    t.goto(x + -35 * zoom, y + 35 * zoom)
    t.goto(x + -35 * zoom, y + 0 * zoom)
    t.goto(x + -20 * zoom, y + 0 *zoom)
    t.goto(x + -20 * zoom, y + 35 * zoom)

    t.penup()
    t.goto(x + 20 * zoom,y + 35 * zoom)
    t.pendown()
    t.goto(x + 20 * zoom, y + 60 * zoom)
    t.goto(x + 35 * zoom, y + 60 * zoom)
    t.goto(x + 35 * zoom, y + 35 * zoom)
    t.goto(x + 20 * zoom, y + 35 * zoom)
    t.goto(x + 20 * zoom,y + 0 * zoom)
    t.goto(x + 35 * zoom,y + 0 * zoom)
    t.goto(x + 35 * zoom,y + 35 * zoom)

    #pernas

    t.penup()
    t.goto(x + -20 * zoom, y + 0 * zoom)
    t.pendown()
    t.goto(x + -20 * zoom, y -60 * zoom)
    t.goto(x + 0 * zoom,y -60 * zoom)
    t.goto(x + 0 * zoom,y -22 * zoom)
    t.penup()
    t.goto(x + 20 * zoom,y + 0 * zoom)
    t.pendown()
    t.goto(x + 20 * zoom,y -60 * zoom)
    t.goto(x + 0 * zoom,y -60 * zoom)


# O desenho não ficou exatamente como esperado
desenhar_steve(10, 10, 1.5)
# Deve ficar recuado
turtle.done()

 

