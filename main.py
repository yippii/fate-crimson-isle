import subprocess
import time
import sys
import shutil
import turtle
import rich.prompt as prompt

# Setup screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Fate: The Crimson Isle")
screen.setup(width=600, height=400, startx=-1, starty=0)
screen.getcanvas().winfo_toplevel().call('wm', 'attributes', '.', '-topmost', '1')

def scroll_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def clear_screen():
    subprocess.call('cls' if sys.platform == 'win32' else 'clear', shell=True)
    time.sleep(0.5)

def clear_gui():
    screen.clearscreen()
    screen.bgcolor("black")

def ask_fixed_bottom(question, choices, lines_above):
    height = shutil.get_terminal_size().lines
    blank_lines = max(0, height - len(lines_above) - 2)
    for line in lines_above:
        scroll_text(line)
    print("\n" * blank_lines, end='')
    return prompt.Prompt.ask(question, choices=choices)

def title_screen():
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
        continueOnTerminal()
        game_init()
        drawMap()
        room1()


    screen.onclick(start_game)

    # Keep window open
    turtle.done()

def continueOnTerminal():
    clear_gui()

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
    pen.write("Continue on terminal", align="center", font=("Arial", 14, "italic"))

def drawMap():
    clear_gui()

    pen = turtle.Turtle()
    pen.pensize(5)
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.color("white")
    pen.goto(-200, 200)
    pen.pendown()
    pen.forward(400)
    pen.right(90)
    pen.forward(400)
    pen.right(90)
    pen.forward(400)
    pen.right(90)
    pen.forward(400)
    pen.penup()

def room1():
    choice = ask_fixed_bottom(
        "What will you do?",
        choices=["1", "2", "3"],
        lines_above=[
            "You have three options",
            "1. Venture into the Dark Forest",
            "2. Explore the Ancient Ruins",
            "3. Seek the Wisdom of the Old Sage",
        ],
    )

    match choice:
        case "1":
            clear_screen()
            scroll_text("You venture into the Dark Forest, where you encounter a fierce dragon.")
            time.sleep(2)
            scroll_text("You engage in a fierce battle and emerge victorious, earning the respect of the dragon.")
        case "2":
            clear_screen()
            scroll_text("You explore the Ancient Ruins and discover a hidden treasure.")
        case "3":
            clear_screen()
            scroll_text("You seek the Wisdom of the Old Sage and gain great insight.")

def game_init():
    scroll_text("Fate: The Crimson Isle")
    time.sleep(2)
    scroll_text("You are the explorer, tasked with exploring the single island called the Crimson Isle.")
    time.sleep(2)
    clear_screen()

if __name__ == "__main__":
    title_screen()