import sys
import time
import subprocess
import rich.prompt as prompt
import shutil

def scroll_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def clear_screen():
    # check if Windows is used instead of *nix
    subprocess.call('cls' if sys.platform == 'win32' else 'clear', shell=True)
    time.sleep(0.5)

def clear_gui(screen):
    screen.clearscreen()
    screen.bgcolor("black")

def ask_fixed_bottom(question, choices, lines_above):
    height = shutil.get_terminal_size().lines
    blank_lines = max(0, height - len(lines_above) - 2)
    for line in lines_above:
        scroll_text(line)
    print("\n" * blank_lines, end='')
    return prompt.Prompt.ask(question, choices=choices)

def setup_knight(knight):
    knight.shape("square")
    knight.shapesize(2, 2)
    knight.color("crimson")
    knight.penup()
