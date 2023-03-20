import turtle as tt

def draw_squares(t, repeat):
    t.left(90)
    for i in range (repeat):
        side = 20*(i+1)
        t.penup()
        t.goto(side/2, side/2)
        t.pendown()
        for j in range(4):
            t.left(90)
            t.forward(side)

wn = tt.Screen()
wn.bgcolor("lightgreen")
alex = tt.Turtle() 
draw_squares(alex, 5) 
wn.mainloop()