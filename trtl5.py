import turtle
s=turtle.Screen()
s.bgcolor("yellow")
t=turtle.Pen()
t.shape("turtle")
t.color("red")
t.speed(2)
a=360/10
for i in range(10):
    t.right(a)
    for j in range(2):
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)
turtle.mainloop()
