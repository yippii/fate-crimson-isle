import time
import turtle

import combat
import methods
import constants
import values

# setup screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Fate: the crimson isle")
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
    title.write("The Crimson Isle:", align="center", font=("courier", 24, "normal"))

    # subtitle
    title.color("white")
    title.goto(0, -40)
    title.write("A terminal roguelike adventure", align="center", font=("arial", 14, "italic"))

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

def drawMapL1():
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
+----+    +---------+      |      +-------+
|         |         |      |      |   z   |
|    |    |    MH   |      |      +-------+
+----+----+  --------------+      |       |
|                                         |
|                                 +-------+
+-------------------+   ---------+
                    |            |
                    +------------+
"""
    parse_map(map_str, cell_size=18)

# def drawMap2():

#     map_str = """
# +----------+             +-----------+
# | L3       |             |           |
# |          |             |           |
# |          |             |           |
# |          +-------------+           |
# |                                    |
# +----+   +--------------- +          |
#      |             |      |          |
#      +---+         +------+          |
#          +---------+      |          |
#          |                |          |
#          |                |          +---+
# +--------------------   --+              |
# |                                        |
# |                                +-------+
# |                                |
# +-------------------+   ---------+
#                     |            |
#                     +------------+
# """
#     parse_map(map_str, cell_size=18)

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

    
def room1():
    drawMapL1()
    knight = turtle.Turtle()
    methods.setup_knight(knight)
    knight.goto(105, 98)

    methods.scroll_text("As you enter the dark hall, you hear chattering from all around you.")
    time.sleep(1.5)
    methods.scroll_text("")


    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "you have three options",
            "1. Enter the left room",
            "2. Enter the right room",
            "3. Continue exploring",
        ],
    )

    match choice:
        case "1":
            hm()
        case "2":
            methods.clear_screen()
            methods.scroll_text("you explore the ancient ruins and discover a hidden treasure.")
        case "3":
            methods.clear_screen()
            methods.scroll_text("you seek the wisdom of the old sage and gain great insight.")

def room2():
    drawMapL2()
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


def room3():
    drawMapL3()
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


def hm():
    methods.clear_screen()
    methods.scroll_text("you enter into the mess hall, where you encounter a fierce dragon.")
    combat.battle_menu()
    time.sleep(2)
    methods.scroll_text("you engage in a fierce battle and emerge victorious, earning the respect of the dragon.")

def game_init():
    methods.scroll_text("\033[1;31mFate: the crimson isle\033[0;0m\n")
    time.sleep(2)
    methods.scroll_text("You are a level 1 adventurer working for King Lebron inc., tasked with exploring the mysterious island, the Crimson Isle.")
    time.sleep(2)
    methods.scroll_text("You land amidst the crashing waves, peering back at the approaching vessel. It carries a team of experienced adventurers, the ones that you are meant to shadow on this expedition.")
    time.sleep(2)
    methods.scroll_text("However, you don't want to wait for them, so you run off to start exploring.")
    time.sleep(2)
    methods.scroll_text("Two")
    time.sleep(0.5)
    methods.scroll_text("Hours")
    time.sleep(0.5)
    methods.scroll_text("Later...")
    time.sleep(2)
    methods.scroll_text("Returning to the shore, you reach your team's camp.")
    time.sleep(2)
    methods.scroll_text("You enter your boss' tent, and start to regale them with your tales of glory from the past two hours.")
    time.sleep(2)
    methods.scroll_text("After a few moments, you notice that they have not responded, nor have they moved from their position on the cot.")
    time.sleep(2)
    methods.scroll_text("You walk up to them, and put your hand on their shoulder...")
    time.sleep(0.5)
    methods.scroll_text("...")
    time.sleep(1.5)
    methods.scroll_text("They fall dead at your feet.")
    time.sleep(2)
    methods.scroll_text("Returning outside, you know that the rest of your team has suffered the same fate.")                        
    methods.scroll_text("Consumed with a desire for revenge, you know that you must avenge them.")
    methods.scroll_text("Grabbing their swords, you leave the camp to begin your journey.")
    methods.scroll_text("Looking up, you see a forbidding castle high up on a towering mountain, glowing with crimson light.")
    methods.scroll_text("You know where you must go.")
    time.sleep(1.5)
    methods.clear_screen()


if __name__ == "__main__":
    title_screen()
