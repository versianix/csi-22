import turtle as tt

def draw_poly(t, n, sz):
    t.penup()
    t.goto(sz/2, 0)
    t.pendown()
    for i in range (n):
        t.left(360/n)
        t.forward(sz)
        

wn = tt.Screen() 
wn.bgcolor("lightgreen")
tess = tt.Turtle() 
draw_poly(tess, 8, 50)
wn.mainloop()