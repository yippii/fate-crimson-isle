import turtle

# Setup screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Fate: The Crimson Isle")

# Create pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.color("crimson")

# Draw title
pen.goto(0, 80)
pen.write("FATE", align="center", font=("Courier", 48, "bold"))

pen.goto(0, 30)
pen.write("THE CRIMSON ISLE", align="center", font=("Courier", 24, "normal"))

# Subtitle
pen.color("white")
pen.goto(0, -40)
pen.write("A Terminal Roguelike Adventure", align="center", font=("Arial", 14, "italic"))

# Start instruction
pen.goto(0, -100)
pen.write("Click Anywhere to Begin", align="center", font=("Arial", 16, "bold"))

# Decorative line
pen.goto(-200, 10)
pen.pendown()
pen.color("crimson")
pen.pensize(3)
pen.forward(400)
pen.penup()

# Click to exit
def start_game(x, y):
    screen.bye()

screen.onclick(start_game)

# Keep window open
screen.mainloop()