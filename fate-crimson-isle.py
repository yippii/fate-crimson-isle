import time
import turtle

import combat
import methods
import constants
import values

# setup screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Fate: the crimson isle")
screen.setup(width=600, height=600, startx=-1, starty=0)
screen.cv._rootwindow.attributes("-topmost", True)
screen.cv._rootwindow.resizable(False, False)
screen.cv._rootwindow.overrideredirect(True)

#F4T3 (music)
import threading
import pygame

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

def play_music(filepath: str):
    def _play():
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play(-1)

    thread = threading.Thread(target=_play, daemon=True)
    thread.start()

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
     |                            |
+----+    +  --------------+      |
|         |                |      |
|         |                |      |
|    |    |         +------+      |
+----+    +---------+      |      +-------+
|         |         |      |      |       |
|         |         |      |      |       |
|    |    |         |      |      +-------+
+----+----+  --------------+      |       |
|                                         |
|                                         |
|                                 +-------+
+-------------------+   ---------+
                    |            |
                    +------------+
"""
    return parse_map(map_str)

def drawMapL2():

    map_str = """
        +-----------------+          +------+
        |                 +--+       |      |
        |                 |  |       |      |
        |     +---+       +  +-------+      |
        |     |   |                         |
        |     |   |                         | 
        |     |   +-----+---   ---+    -----+
        |     |         |         |         |
    +---+  -  +------+  +---------+         |
    |                |            |         |
    |                |            +---------+
    +----------------------------+
    |                            |
    |                            |
    |                            |
    |                            |
    |                            |
    +----------------------------+
"""
    return parse_map(map_str)

def parse_map(map_str, padding=40):
    lines = map_str.strip('\n').split('\n')
    max_width = max(len(line) for line in lines)
    lines = [line.ljust(max_width) for line in lines]
    rows = len(lines)
    cols = max_width

    usable_width = 600 - padding * 2
    usable_height = 600 - padding * 2

    # Separate horizontal and vertical cell sizes
    cell_w = usable_width // cols
    cell_h = usable_height // rows
    cell_w = max(cell_w, 4)
    cell_h = max(cell_h, 4)

    start_x = -(cols * cell_w) // 2
    start_y = (rows * cell_h) // 2

    pen = turtle.Turtle()
    pen.pensize(1)
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.color("white")
    screen.tracer(0)

    # Draw horizontal walls (-)
    for r, line in enumerate(lines):
        c = 0
        while c < len(line):
            if line[c] == '-':
                start = c
                while c < len(line) and line[c] == '-':
                    c += 1
                length = (c - start) * cell_w      # uses cell_w
                x = start_x + start * cell_w
                y = start_y - r * cell_h            # uses cell_h
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
                length = (r - start) * cell_h      # uses cell_h
                x = start_x + c * cell_w
                y = start_y - start * cell_h
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
                x = start_x + c * cell_w
                y = start_y - r * cell_h
                pen.goto(x, y)
                pen.dot(4, "white")

    screen.tracer(1)
    screen.update()

    return cell_w, cell_h, start_x, start_y

def room1():
    cell_w, cell_h, start_x, start_y = drawMapL1()
    knight = turtle.Turtle()
    methods.setup_knight(knight)
    #knight.goto(105, 98)
    knight.goto(start_x + 8 * cell_w, start_y - 10 * cell_h)

    methods.scroll_text("As you enter the dark hall, you hear chattering from all around you.")
    time.sleep(1.5)
    methods.scroll_text("")


    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "you have three options",
            "1. Enter the mess hall",
            "2. Enter the armory",
            "3. Continue exploring",
        ],
    )

    match choice:
        case "1":
            methods.clear_screen()
            hm()
            room2(knight)
        case "2":
            methods.clear_screen()
            armory()
            room2(knight)
        case "3":
            methods.clear_screen()
            room2(knight)

def room2(knight):
    knight.goto(140, 170)
    methods.clear_screen()
    methods.scroll_text("You turn to a new hallway, and the first thing you see is a right door, a left door, and a door at the end, hinting at a mystery.")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "you have three options",
            "1. venture into the right door",
            "2. explore the War Chest room",
            "3. enter the Alchemy Lab",
        ],
    )

    match choice:
        case "1":
            closet()
            room3(knight)
        case "2":
            warChest()
            room3(knight)
        case "3":
            lab()
            room3(knight)


def room3(knight):
    knight.goto(150, 140)
    methods.scroll_text("As you turn, the next hallway reveals only two doors: an archery range and a blade vault.")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2"],
        [
            "you have two options",
            "1. explore The Elixir Vault",
            "2. venture into the blade vault",
        ],
    )

    match choice:
        case "1":
            elixirVault()
            room4(knight)
        case "2":
            bladeVault()
            room4(knight)
        case "le bron":
            methods.clear_screen()
            methods.scroll_text("you seek the wisdom of the king le bron james")

def room4(knight):
    knight.goto(150, 140)
    methods.scroll_text("As you turn, the next hallway reveals only two doors: an archery range and a blade vault.")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "you have three options",
            "1. explore the archery range",
            "2. Explore into a staircase.",
        ],
    )

    match choice:
        case "1":
            archeryRange()
        case "2":
            L2(knight)

def L2(knight):
    methods.clear_screen()
    methods.clear_gui(screen)
    knightL2 = turtle.Turtle()
    cell_w, cell_h, start_x, start_y = drawMapL2()
    methods.setup_knight(knightL2)
    knightL2.goto(start_x + 8 * cell_w, start_y - 10 * cell_h)

    methods.scroll_text("As you venture down into the dungeon, you reach the lowest level. You can hear the screams of the Necromancer's Experiments.")
    time.sleep(1.5)
    methods.scroll_text("")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "you have three options",
            "1. Enter the Herbalist's Den",
            "2. Enter the The Forgemaster's Vault",
            "3. Continue exploring",
        ],
    )

    match choice:
        case "1":
            methods.clear_screen()
            Herbalist()
            # TODO: This is broken, you can't just go back to level 1
            # room3(knightL2)
            L2room2(knightL2)
        case "2":
            methods.clear_screen()
            Forgemaster()
            # TODO: Removed references from L1 room 4, again, map will break
            L2room2(knightL2)
        case "3":
            methods.clear_screen()
            L2room2(knightL2)

# TODO: Duplicated room (this is boss fight right)
def L2room2(knight):
    knight.goto(150, 140)
    methods.scroll_text("The hallway continues, and you find yourself facing a doorway before you: a room pulsing with unsettling activity, and a faint, desperate scream suggesting something terrible is happening within.")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2"],
        [
            "you have two options",
            "1. explore the archery range",
            "2. Explore into a staircase.",
        ],
    )

    match choice:
        case "1":
            # TODO: This is broken, you can't just go back to level 1
            # also, the game currently ends here, we have to design the final boss
            archeryRange()
            #room4(knight)
        case "2":
            L2(knight)


#------------------------ ROOMS -------------------------------------------------------------------------------------------------------------
def hm():
    methods.clear_screen()
    methods.scroll_text("you enter into the mess hall, where you encounter Goblin eating pizza.")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "you have two options",
            "1. Attack the goblin",
            "2. Leave",
        ],
    )
    match choice:
        case "1":
            combat.battle_menu()
            time.sleep(2)
            methods.scroll_text("You defeated the goblin! You found a blue key and a stamina potion.")
            
            # Add blue key and stamina potion to inventory here
            values.blue_key1 = True
            values.potion_num += 1
            methods.scroll_text("You have"+ str(values.potion_num) + " potions left!")
        case "2":
            methods.scroll_text("You back away slowly and leave the mess hall.")
        case _:
            methods.scroll_text("You hesitate, unsure of what to do.")
    # combat.battle_menu()
    # time.sleep(2)

def armory():
    methods.clear_screen()
    methods.scroll_text("You enter the Armory. You find a goblin trying on different pieces of armor.")
    
    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "you have two options",
            "1. Attack the goblin",
            "2. Leave",
        ],
    )
    match choice:
        case "1":
            combat.battle_menu()
            time.sleep(2)
            methods.scroll_text("You defeated the goblin! You found 3 swords.\n")
            values.sword_amount += constants.SWORDS_GAIN
            methods.scroll_text("You Have " + str(values.sword_amount) + " swords left!")
        case "2":
            methods.scroll_text("You back away slowly and leave the mess hall.")
        case _:
            methods.scroll_text("You hesitate, unsure of what to do.")

# def hallway():
#     methods.clear_screen()
#     methods.scroll_text("You enter the Armory. You find a goblin trying on different pieces of armor.")
#     combat.battle_menu()
#     time.sleep(2)

def closet():
    methods.clear_screen()
    methods.scroll_text(".")
    #Puzzle room...
    time.sleep(1.5)

def warChest():
    methods.clear_screen()
    methods.scroll_text("You enter the War Chest room. You find a goblin cleaning his sword.")
    
    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "you have two options",
            "1. Attack the goblin",
            "2. Leave",
        ],
    )
    match choice:
        case "1":
            combat.battle_menu()
            time.sleep(2)
            methods.scroll_text("You defeated the goblin! You found 3 swords.")

            values.sword_amount += constants.SWORDS_GAIN
            methods.scroll_text("You Have" + str(values.sword_amount) + "swords left!")
        case "2":
            methods.scroll_text("You back away slowly and leave the mess hall.")
        case _:
            methods.scroll_text("You hesitate, unsure of what to do.")

def lab():
    methods.clear_screen()
    methods.scroll_text("As you enter the alchemy lab, you find a bunch of documents explaining how to make a stamina potion.")
    # + Potion
    values.potion_num += 1
    methods.scroll_text("You have" + str(values.potion_num) + "potions left!")
    time.sleep(1.5)

def elixirVault():
    methods.clear_screen()
    methods.scroll_text("As you enter the alchemy lab, you find a bunch of documents explaining how to make a stamina potion.")
    # + Potion
    values.potion_num += 1
    methods.scroll_text("You have " + str(values.potion_num) + " potions left!")
    time.sleep(1.5)

def bladeVault():
    methods.clear_screen()
    methods.scroll_text("You enter the blade vault room. You find a goblin cleaning his sword.")
    
    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "you have two options",
            "1. Attack the goblin",
            "2. Leave",
        ],
    )
    match choice:
        case "1":
            combat.battle_menu()
            time.sleep(2)
            methods.scroll_text("You defeated the goblin! You found 3 swords.")

            values.sword_amount += constants.SWORDS_GAIN
            methods.scroll_text("You Have " + str(values.sword_amount) + " swords left!")
        case "2":
            methods.scroll_text("You back away slowly and leave the mess hall.")
        case _:
            methods.scroll_text("You hesitate, unsure of what to do.")

def archeryRange():
    methods.clear_screen()
    methods.scroll_text("You enter the archery range. You find a goblin restringing his bow.")
    
    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "you have two options",
            "1. Attack the goblin",
            "2. Leave",
        ],
    )
    match choice:
        case "1":
            combat.battle_menu()
            time.sleep(2)
            methods.scroll_text("You defeated the goblin! You took his bow.")

            values.have_bow = True 
            values.arrow_amount += constants.ARROW_GAIN
            methods.scroll_text("You Have " + str(values.arrow_amount) + " arrows left!")
        case "2":
            methods.scroll_text("You back away slowly and leave the archery range.")
        case _:
            methods.scroll_text("You hesitate, unsure of what to do.")

def Herbalist():
    methods.clear_screen()
    methods.scroll_text("As you enter the alchemy lab, you find a bunch of documents explaining how to make a stamina potion.")
    # + Potion
    values.potion_num += 1
    methods.scroll_text("You have " + str(values.potion_num) + " potions left!")
    time.sleep(1.5)

def Forgemaster():
    methods.clear_screen()
    methods.scroll_text("You enter the blade vault room. You find a goblin cleaning his sword.")
    
    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "you have two options",
            "1. Attack the goblin",
            "2. Leave",
        ],
    )
    match choice:
        case "1":
            combat.battle_menu()
            time.sleep(2)
            methods.scroll_text("You defeated the goblin! You found 3 swords.")
            values.sword_amount += constants.SWORDS_GAIN
            methods.scroll_text("You Have" + str(values.sword_amount) + " swords left!")
        case "2":
            methods.scroll_text("You back away slowly and leave the mess hall.")
        case _:
            methods.scroll_text("You hesitate, unsure of what to do.")

def end1():
    methods.scroll_text("")

def end2():
    methods.scroll_text("")

def end3():
    methods.scroll_text("")

def endLEBRON():
    methods.scroll_text("")

def win1():
    methods.scroll_text("")


def game_init():
    methods.scroll_text("\033[1;31mFate: the crimson isle\033[0;0m\n")
    time.sleep(2)
    methods.scroll_text("You are a level 1 adventurer working for King Lebron inc., tasked with exploring the mysterious island, the Crimson Isle.\n")
    time.sleep(2)
    methods.scroll_text("You land amidst the crashing waves, peering back at the approaching vessel. It carries a team of experienced adventurers, the ones that you are meant to shadow on this expedition.\n")
    time.sleep(2)
    methods.scroll_text("However, you don't want to wait for them, so you run off to start exploring.\n")
    time.sleep(2)
    methods.scroll_text("Two...")
    time.sleep(0.5)
    methods.scroll_text("Hours...")
    time.sleep(0.5)
    methods.scroll_text("Later...\n")
    time.sleep(2)
    methods.scroll_text("Returning to the shore, you reach your team's camp.\n")
    time.sleep(2)
    methods.scroll_text("You enter your boss' tent, and start to regale them with your tales of glory from the past two hours.\n")
    time.sleep(2)
    methods.scroll_text("After a few moments, you notice that they have not responded, nor have they moved from their position on the cot.\n")
    time.sleep(2)
    methods.scroll_text("You walk up to them, and put your hand on their shoulder...\n")
    time.sleep(0.5)
    methods.scroll_text("...")
    time.sleep(1.5)
    methods.scroll_text("They fall dead at your feet.\n")
    time.sleep(2)
    methods.scroll_text("Returning outside, you know that the rest of your team has suffered the same fate.")                        
    methods.scroll_text("Consumed with a desire for revenge, you know that you must avenge them.")
    methods.scroll_text("Grabbing their swords, you leave the camp to begin your journey.")
    methods.scroll_text("Looking up, you see a forbidding castle high up on a towering mountain, glowing with crimson light.")
    methods.scroll_text("You know where you must go.")
    time.sleep(1.5)
    methods.clear_screen()
    #time.sleep(1)
    play_music("F4T3.mp3")

if __name__ == "__main__":
    title_screen()











#67