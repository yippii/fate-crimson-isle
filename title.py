import turtle

# Title screen
screen = turtle.Screen()
screen.bgcolor("black")
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(0, 0)
pen.write("The Quest of the Last DOOM", align="center", font=("Arial", 24, "bold"))
screen.onclick(lambda x, y: screen.bye())
screen.mainloop()