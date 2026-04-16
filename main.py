import time
import turtle
import methods
import constants

# setup screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("fate: the crimson isle")
screen.setup(width=600, height=400, startx=-1, starty=0)
screen.cv._rootwindow.attributes("-topmost", True)
screen.cv._rootwindow.resizable(False, False)
screen.cv._rootwindow.overrideredirect(True)

# setup title
title = turtle.Turtle()
title.hideturtle()
title.speed(0)
title.penup()
title.color("crimson")

def title_screen():
    # draw title
    title.goto(0, 80)
    title.write("fate", align="center", font=("courier", 48, "bold"))

    title.goto(0, 30)
    title.write("the crimson isle", align="center", font=("courier", 24, "normal"))

    # subtitle
    title.color("white")
    title.goto(0, -40)
    title.write("a terminal roguelike adventure", align="center", font=("arial", 14, "italic"))

    # start instruction
    title.goto(0, -100)
    title.write("click anywhere to begin", align="center", font=("arial", 16, "bold"))

    #decorative line
    title.goto(-200, 10)
    title.pendown()
    title.color("crimson")
    title.pensize(3)
    title.forward(400)
    title.penup()

    screen.update()

    # click to exit
    def start_game(x, y):
        continueOnTerminal()
        game_init()
        drawMap()
        #level2()
        room1()

    screen.onclick(start_game)
    turtle.done()

def continueOnTerminal():
    methods.clear_gui(screen)
    # draw title
    title.goto(0, 0)
    title.write("Fate", align="center", font=("courier", 48, "bold"))

    title.goto(0, 30)
    title.write("the crimson isle", align="center", font=("courier", 24, "normal"))

    title.color("white")
    title.goto(0, -40)
    title.write("continue on terminal", align="center", font=("arial", 14, "italic"))
    screen.update()

def drawMap():
    methods.clear_gui(screen)
    pen = turtle.Turtle()
    pen.pensize(5)
    pen.hideturtle()
    pen.speed(100000)
    pen.penup()
    pen.color("white")
    pen.goto(-200, 180)
    pen.pendown()

    # map
    for i in range(len(constants.mapData)):
        if i % 2 == 0:
            pen.forward(constants.mapData[i])
        else:
            if constants.mapData[i] == "l":
                pen.left(90)
            elif constants.mapData[i] == "r":
                pen.right(90)

    pen.goto(-200, 180)
    screen.update()

def level2():
    methods.clear_gui(screen)
    pen = turtle.Turtle()
    pen.pensize(5)
    pen.hideturtle()
    pen.speed(100000)
    pen.penup()
    pen.color("white")
    pen.goto(-200, 180)
    pen.pendown()

    # map
    for i in range(len(constants.l2map)):
        if i % 2 == 0:
            pen.forward(constants.l2map[i])
        else:
            if constants.l2map[i] == "l":
                pen.left(90)
            else:
                pen.right(90)

    pen.goto(-200, 180)
    screen.update()

def level3():
    methods.clear_gui(screen)
    pen = turtle.Turtle()
    pen.pensize(5)
    pen.hideturtle()
    pen.speed(100000)
    pen.penup()
    pen.color("white")
    pen.goto(-200, 180)
    pen.pendown()

    # map
    for i in range(len(constants.mapData)):
        if i % 2 == 0:
            pen.forward(constants.mapData[i])
        else:
            if constants.mapData[i] == "l":
                pen.left(90)
            else:
                pen.right(90)

    pen.goto(-200, 180)
    screen.update()

def room1():
    knight = turtle.Turtle()
    methods.setup_knight(knight)
    knight.goto(150, 140)

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "you have three options",
            "1. venture into the dark forest",
            "2. explore the ancient ruins",
            "3. seek the wisdom of the old sage",
        ],
    )

    match choice:
        case "1":
            methods.clear_screen()
            methods.scroll_text("you venture into the dark forest, where you encounter a fierce dragon.")
            time.sleep(2)
            methods.scroll_text("you engage in a fierce battle and emerge victorious, earning the respect of the dragon.")
        case "2":
            methods.clear_screen()
            methods.scroll_text("you explore the ancient ruins and discover a hidden treasure.")
        case "3":
            methods.clear_screen()
            methods.scroll_text("you seek the wisdom of the old sage and gain great insight.")

def game_init():
    methods.scroll_text("\033[1;31mFate: the crimson isle\033[0;0m\n")
    time.sleep(2)
    methods.scroll_text("you are the explorer, tasked with exploring the single island called the crimson isle.")
    time.sleep(2)
    methods.clear_screen()

if __name__ == "__main__":
    title_screen()
