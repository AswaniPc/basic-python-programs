import turtle
t=turtle.Pen()
a=360/10
t.begin_fill()
t.color ('blue')
for i in range(10):
    t.right(a)
    for j in range(4):
        t.forward(150)
        t.right(90)
t.end_fill()
turtle.mainloop()

  
