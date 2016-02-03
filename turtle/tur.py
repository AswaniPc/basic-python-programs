import turtle
t=turtle.Pen()
t.begin_fill()
t.color("yellow")
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()
t.hideturtle()
turtle.mainloop()



