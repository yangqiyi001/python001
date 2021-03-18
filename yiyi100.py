import turtle
t=turtle.Pen()
turtle.bgcolor("blue")
sides=5
colors=["red","yellow","black","orange","green","purple"]
for x in range(270):
    t.pencolor(colors[x%sides])
    t.forward(x*2)
    t.left(360/sides+1)
    t.width(x*sides/150)
