import turtle

scr=turtle.Screen()
scr.setup(width=420, height=400)
pen=turtle.Turtle()

def heart(): 
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)

    for _ in range(20): #first curve
        pen.right(10)
        pen.forward(10)
    
    pen.left(114)
    for _ in range(20): #second curve
        pen.forward(10)
        pen.right(10)
    
    pen.forward(113)
    pen.end_fill()

def text(): #text inside
    pen.up()
    pen.setpos(-40, 83)
    pen.down()
    pen.color('white')
    pen.write("I love You", font=("Verdana", 14, "bold"))
    pen.up()

pen.ht()

heart()
text()

turtle.done()
