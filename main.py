import subprocess
import time
import sys
import shutil
import turtle
import rich.prompt as prompt

import title

def scroll_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def clear_screen():
    subprocess.call('cls' if sys.platform == 'win32' else 'clear', shell=True)
    time.sleep(0.5)

def ask_fixed_bottom(question, choices, lines_above):
    height = shutil.get_terminal_size().lines
    blank_lines = max(0, height - len(lines_above) - 2)
    for line in lines_above:
        scroll_text(line)
    print("\n" * blank_lines, end='')
    return prompt.Prompt.ask(question, choices=choices)

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
    scroll_text("The Quest of the Last DOOM")
    time.sleep(2)
    scroll_text("You are the last dragon knight, tasked with protecting the realm from evil forces.")
    time.sleep(2)
    clear_screen()

if __name__ == "__main__":
    game_init()