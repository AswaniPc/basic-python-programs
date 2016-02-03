import turtle
t=turtle.Pen()
t.pensize(2)
t.begin_fill()
t.color ('purple')
for i in range(360):
    t.forward(1)
    t.right(1)
t.end_fill()
t.hideturtle()
turtle.mainloop()

