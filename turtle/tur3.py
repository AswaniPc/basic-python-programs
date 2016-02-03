import turtle
t=turtle.Pen()
t.pensize(2)
t.begin_fill()
t.color ('blue')
a = 360/5
for iter in range (4):
    t.forward (150)
    t.left(a)
t.end_fill()
t.hideturtle()
turtle.mainloop()
