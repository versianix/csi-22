import turtle as tt

def draw_spiral(t, n, angle):
    t.pendown()
    t.left(180)
    for i in range(n):
        size = 2*(i+1)
        t.forward(size)
        t.right(angle)
        
wn = tt.Screen()
wn.bgcolor("lightgreen")
tess = tt.Turtle()
tess.penup()
tess.goto(-150, 0)
draw_spiral(tess, 100, 90)
tess.penup()
tess.goto(150, 0)
tess.left(180)
draw_spiral(tess, 100, 89)
wn.mainloop()