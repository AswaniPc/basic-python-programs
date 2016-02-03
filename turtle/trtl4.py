import turtle
t=turtle.Pen()
t.left(30)
for i in range(3):
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.left(120)
turtle.mainloop()
