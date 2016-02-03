import turtle
t=turtle.Pen()
t.pensize(2)
t.begin_fill()
t.color ('red')
a = 360/3
for iter in range (3):
    t.forward (150)
    t.left(a)
t.end_fill()
t.hideturtle()
turtle.mainloop()
