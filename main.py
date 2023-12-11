import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("turtle")
turtle_instance = turtle.Turtle()
def turtle_forward():
    turtle_instance.forward(10)
def turtle_loca():
    turtle_instance.setheading(turtle_instance.heading()-5)
def turtle_local():
    turtle_instance.setheading(turtle_instance.heading()+5)
def clear_screen():
    turtle_instance.clear()
def turtle_return_home():
    turtle_instance.home()
def turtle_pen_up():
    turtle_instance.penup()
def turtle_pen_down():
    turtle_instance.pendown()
def turtle_circle():
    turtle_instance.circle(-20)
def turtle_circl():
    turtle_instance.circle(20)

drawing_board.listen()
drawing_board.onkeypress(fun=turtle_forward, key="space")
drawing_board.onkeypress(fun=turtle_loca, key="A")
drawing_board.onkeypress(fun=turtle_local, key="D")
drawing_board.onkeypress(fun=clear_screen, key="C")
drawing_board.onkeypress(fun=turtle_return_home, key="H")
drawing_board.onkey(fun=turtle_pen_up,key="G")
drawing_board.onkey(fun=turtle_pen_down,key="F")
drawing_board.onkey(fun=turtle_circle,key="O")
drawing_board.onkey(fun=turtle_circl,key="P")

turtle.mainloop()
