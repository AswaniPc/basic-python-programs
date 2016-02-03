import turtle
t=turtle.Pen()
t.pensize(2)
t.begin_fill()
t.color ('navy')
a = 360/6
for iter in range (6):
    t.forward (150)
    t.left(a)
t.end_fill()
t.hideturtle()
turtle.mainloop()
