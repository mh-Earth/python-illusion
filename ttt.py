import turtle
root=turtle.Turtle()
root.pensize()
screen=turtle.Screen()
screen.bgcolor('black')
root.speed(0)
root.ht()
color = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
color = ['white','black']

for x in range(500):
    # root.pencolor(color[x%6])
    root.pencolor(color[x%2])
    root.width(x/100 + 1)
    root.forward(x)
    root.left(59)
turtle.done()


