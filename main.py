import time
import turtle
import methods
import constants
import values

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
    title.write("Fate", align="center", font=("courier", 48, "bold"))

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
        drawMap1()
        #level2()
        room1()

    screen.onclick(start_game)
    turtle.done()

def continueOnTerminal():
    methods.clear_gui(screen)
    # draw title
    title.goto(0, 80)
    title.write("Fate", align="center", font=("courier", 48, "bold"))

    title.goto(0, 30)
    title.write("the crimson isle", align="center", font=("courier", 24, "normal"))

    title.color("white")
    title.goto(0, -40)
    title.write("continue on terminal", align="center", font=("arial", 14, "italic"))
    screen.update()

def drawMap1():
    methods.clear_gui(screen)

    map_str = """
                           +--------+
                           |        |
           +---------------+        |
           |               |        |
     +-----+------+        +    ----+
     |                            |
     |                            |
+----+    +  --------------+      |
|         |            S   |      |
|    |    |   P     +------+      |
+----+    +---------+      |      |
|         |         |      |      |
|    |    |    MH   |      |      +-------+
+----+----+  --------------+      |       |
|                                         |
|                                 +-------+
+-------------------+   ---------+
                    |            |
                    +------------+
"""
    parse_map(map_str, cell_size=18)

def drawMap2():
    methods.clear_gui(screen)

    map_str = """
+----------+             +-----------+
| L3       |             |           |
|          |             |           |
|          |             |           |
|          +-------------+           |
|                                    |
+----+   +--------------- +          |
     |             |      |          |
     +---+         +------+          |
         +---------+      |          |
         |                |          |
         |                |          +---+
+--------------------   --+              |
|                                        |
|                                +-------+
|                                |
+-------------------+   ---------+
                    |            |
                    +------------+
"""
    parse_map(map_str, cell_size=18)

def parse_map(map_str, cell_size=20):
    lines = map_str.strip('\n').split('\n')
    
    max_width = max(len(line) for line in lines)

    lines = [line.ljust(max_width) for line in lines]
    
    rows = len(lines)
    cols = max_width

    start_x = -(cols * cell_size) // 2
    start_y = (rows * cell_size) // 2

    pen = turtle.Turtle()
    pen.pensize(2)
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.color("white")

    # Draw horizontal walls (-)
    for r, line in enumerate(lines):
        c = 0
        while c < len(line):
            if line[c] == '-':
                # Find run length
                start = c
                while c < len(line) and line[c] == '-':
                    c += 1
                length = (c - start) * cell_size
                x = start_x + start * cell_size
                y = start_y - r * cell_size
                pen.goto(x, y)
                pen.pendown()
                pen.goto(x + length, y)
                pen.penup()
            else:
                c += 1

    # Draw vertical walls (|)
    for c in range(cols):
        r = 0
        while r < rows:
            if r < len(lines) and c < len(lines[r]) and lines[r][c] == '|':
                start = r
                while r < rows and c < len(lines[r]) and lines[r][c] == '|':
                    r += 1
                length = (r - start) * cell_size
                x = start_x + c * cell_size
                y = start_y - start * cell_size
                pen.goto(x, y)
                pen.pendown()
                pen.goto(x, y - length)
                pen.penup()
            else:
                r += 1

    # Draw corners (+)
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == '+':
                x = start_x + c * cell_size
                y = start_y - r * cell_size
                pen.goto(x, y)
                pen.dot(4, "white")

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
