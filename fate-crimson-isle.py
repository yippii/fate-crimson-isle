import time
import turtle
import argparse
import rich.console as console

import combat
import methods
import constants
import values

#F4T3 (music)
import threading
import pygame

# setup screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Fate: The Crimson Isle")
screen.setup(width=600, height=600, startx=-1, starty=0)
screen.cv._rootwindow.attributes("-topmost", True)
screen.cv._rootwindow.resizable(False, False)

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
    title.write("Click anywhere to begin", align="center", font=("arial", 16, "bold"))

    #decorative line
    title.goto(-200, 10)
    title.pendown()
    title.color("crimson")
    title.pensize(3)
    title.forward(400)
    title.penup()

    screen.update()

    parser = argparse.ArgumentParser(description="Fate: The Crimson Isle")
    parser.add_argument("-s", "--skip", action="store_true", help="Skip Game" )

    # click to exit
    def start_game(x, y):
        if parser.parse_args().skip:
            continueOnTerminal()
            room1()
        else:
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
    title.write("The Crimson Isle", align="center", font=("courier", 24, "normal"))

    title.color("white")
    title.goto(0, -40)
    title.write("Continue on terminal", align="center", font=("arial", 14, "italic"))
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
        |                 |          |      |
        |                 |          |      |
        |     +---+       +----------+      |
        |     |   |                         |
        |     |   |                         | 
        |     |   +-----+---   ---+    -----+
        |     |         |         |         |
    +---+  -  +------+  +---------+         |
    |      |         |            |         |
    |      |         |            +---------+
    +--   ------   --------------+
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
            "You have three options",
            "1. Enter the mess hall",
            "2. Enter the armory",
            "3. Continue exploring",
        ],
    )

    match choice:
        case "1":
            methods.clear_screen()
            hm(knight)
            room2(knight)
        case "2":
            methods.clear_screen()
            armory(knight)
            room2(knight)
        case "3":
            methods.clear_screen()
            room2(knight)

# TODO: Update gotos
def room2(knight):
    knight.goto(-110, 130)
    methods.clear_screen()
    methods.scroll_text("You turn to a new hallway. The first thing you see is a door on your left, and then two doors at the end, hinting at a mystery.")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "You have three options",
            "1. Venture through the left door",
            "2. Explore the War Chest room",
            "3. Enter the Alchemy Lab",
        ],
    )

    match choice:
        case "1":
            closet()
            room3(knight)
        case "2":
            warChest(knight)
            room3(knight)
        case "3":
            lab()
            room3(knight)

def room3(knight):
    methods.clear_screen()
    knight.goto(110, -70)
    methods.scroll_text("As you turn, the next hallway reveals only two doors: The Elixir Vault and a Blade Vault.")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2"],
        [
            "You have two options",
            "1. Explore the Elixir Vault",
            "2. Venture into the Blade vault",
        ],
    )

    match choice:
        case "1":
            elixirVault(knight)
            room4(knight)
        case "2":
            bladeVault(knight)
            room4(knight)
        case "le bron":
            methods.clear_screen()
            methods.scroll_text("You seek the wisdom of the King LeBron James")
            endLEBRON()
            

# TODO: Update gotos
def room4(knight):
    knight.goto(-40, -145)
    methods.scroll_text("As you turn, the next hallway reveals only two doors: an Archery Range and a staircase delving deeper into the castle.")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2"],
        [
            "You have two options",
            "1. Explore the archery range",
            "2. Explore into a staircase.",
        ],
    )

    match choice:
        case "1":
            archeryRange(knight)
            L2()
        case "2":
            L2()

#--------------- LEVEL 2 -------------------------------------------------------------------------------------------------------------------------------

def L2():
    methods.clear_screen()
    methods.clear_gui(screen)
    knightL2 = turtle.Turtle()
    cell_w, cell_h, start_x, start_y = drawMapL2()
    methods.setup_knight(knightL2)
    knightL2.goto(195, 200)

    methods.scroll_text("As you venture down into the dungeon, you reach the lowest level. You can hear the screams of the Necromancer's Experiments.")
    time.sleep(1.5)
    methods.scroll_text("")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3"],
        [
            "You have three options",
            "1. Enter the Herbalist's Den",
            "2. Enter the The Forgemaster's Vault",
            "3. Continue exploring",
        ],
    )

    match choice:
        case "1":
            methods.clear_screen()
            Herbalist(knightL2)
            L2room2(knightL2)
        case "2":
            methods.clear_screen()
            Forgemaster(knightL2)
            L2room2(knightL2)
        case "3":
            methods.clear_screen()
            L2room2(knightL2)

# TODO: Update gotos

def L2room2(knight):
    knight.goto(-130, 167)
    methods.scroll_text("The hallway continues, and you find yourself facing a doorway before you: a room pulsing with unsettling activity, and a faint, desperate scream suggesting something terrible is happening within.")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2"],
        [
            "You have two options",
            "1. Explore the Quiver Room",
            "2. Explore into Kings Hoard.",
        ],
    )

    match choice:
        case "1":
            quiverRoom(knight)
        case "2":
            kingsHoard(knight)

def boss_fight(knight):
    knight.goto(-150, -140)
    methods.scroll_text("Dooming testament of Avril, You made it all the way here, but you will never take me down.")
    methods.scroll_text("Let the games begin")
    methods.scroll_text("HAHAHAHA")

    if(values.kingsHoard_ROOM == False):
        win1()
    elif(values.kingsHoard_ROOM == True):
        end2()

#------------------------ ROOMS -------------------------------------------------------------------------------------------------------------

def hm(knight):
    knight.goto(0, 120)
    methods.clear_screen()
    methods.scroll_text("You enter into the mess hall, where you encounter a Goblin eating pizza.")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2"],
        [
            "You have two options",
            "1. Attack the goblin",
            "2. Continue exploring",
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
            methods.scroll_text("You have "+ str(values.potion_num) + " potions left!")

            values.room_cleared = values.room_cleared + 1
        case "2":
            methods.scroll_text("You back away slowly and leave the mess hall.")
    # combat.battle_menu()
    # time.sleep(2)

def armory(knight):
    knight.goto(-230, 25)
    methods.clear_screen()
    methods.scroll_text("You enter the Armory. You find a goblin trying on different pieces of armor.")
    
    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2"],
        [
            "You have two options",
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
            methods.scroll_text("You have " + str(values.sword_amount) + " swords left!")
            values.room_cleared = values.room_cleared + 1
        case "2":
            methods.scroll_text("You back away slowly and leave the armory.")

def closet(knight):
    knight.goto(190, -50)
    methods.clear_screen()
    methods.scroll_text(".")
    #Puzzle room...
    time.sleep(1.5)
    values.room_cleared = values.room_cleared + 1

def warChest(knight):
    knight.goto(190, -50)
    methods.clear_screen()
    methods.scroll_text("You enter the War Chest room. You find a goblin cleaning his sword.")
    
    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2"],
        [
            "You have two options",
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
            methods.scroll_text("You have " + str(values.sword_amount) + " swords left!")

            values.room_cleared = values.room_cleared + 1
        case "2":
            methods.scroll_text("You backed away slowly and left the war chest room.")


def lab():
    methods.clear_screen()
    methods.scroll_text("As you enter the alchemy lab, you find a bunch of documents explaining how to make a stamina potion.")
    # + Potion
    values.potion_num += 1
    methods.scroll_text("You have " + str(values.potion_num) + " potions left!")
    time.sleep(1.5)
    values.room_cleared = values.room_cleared + 1

def elixirVault(knight):
    knight.goto(190, -120)
    methods.clear_screen()
    methods.scroll_text("As you enter The Elixir Vault, you find a bunch potions lying around. You take two of them.")
    # + Potion
    values.potion_num += 2
    methods.scroll_text("You have " + str(values.potion_num) + " potions left!")
    time.sleep(1.5)
    values.room_cleared = values.room_cleared + 1

def bladeVault(knight):
    knight.goto(20, -50)
    methods.clear_screen()
    methods.scroll_text("You enter the blade vault. You find a goblin cleaning his sword.")
    
    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2"],
        [
            "You have two options",
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
            methods.scroll_text("You have " + str(values.sword_amount) + " swords left!")
            values.room_cleared = values.room_cleared + 1
        case "2":
            methods.scroll_text("You back away slowly and leave the blade vault.")


def archeryRange(knight):
    knight.goto(-80, -55)
    methods.clear_screen()
    methods.scroll_text("You enter the archery range. You find a goblin restringing his bow.")
    
    
    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2"],
        [
            "You have two options",
            "1. Attack the goblin",
            "2. Leave",
        ],
    )
    match choice:
        case "1":
            combat.battle_menu()
            time.sleep(2)
            methods.scroll_text("You defeated the goblin! You took his bow.")
            values.room_cleared = values.room_cleared + 1

            values.have_bow = True 
            values.arrow_amount += constants.ARROW_GAIN
            methods.scroll_text("You have " + str(values.arrow_amount) + " arrows left!")
        case "2":
            methods.scroll_text("You back away slowly and leave the archery range.")

def Herbalist(knight):
    knight.goto(67, 50)
    methods.clear_screen()
    methods.scroll_text("As you enter the alchemy lab, you find a bunch of documents explaining how to make a stamina potion.")
    # + Potion
    values.potion_num += 1
    methods.scroll_text("You have " + str(values.potion_num) + " potions left!")
    time.sleep(1.5)
    values.room_cleared = values.room_cleared + 1

def Forgemaster(knight):
    knight.goto(150, 50)
    methods.clear_screen()
    methods.scroll_text("You enter the forgemaster's room. You find a goblin cleaning his sword.")
    
    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2"],
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
            values.room_cleared = values.room_cleared + 1
        case "2":
            methods.scroll_text("You back away slowly and leave the forgemaster's room.")

def quiverRoom(knight):
    knight.goto(-170, -25)
    methods.clear_screen()
    methods.scroll_text("You enter the Quiver Room. You find a crossbow")
    values.have_crossbow = True
    values.arrow_amount = values.arrow_amount + 2 * constants.ARROW_GAIN
    values.room_cleared = values.room_cleared + 1
    boss_fight(knight)


def kingsHoard(knight):
    knight.goto(-100, -25)
    methods.clear_screen()
    methods.scroll_text("You enter the Quiver Room. You find a crossbow")
    values.have_crossbow = True
    values.arrow_amount = values.arrow_amount + 2 * constants.ARROW_GAIN
    values.room_cleared = values.room_cleared + 1
    kingsHoard_ROOM = True
    boss_fight(knight)

#------------------------------------- ENDINGS ----------------------------------------------------------------------------------------
def end1():

    if values.have_bow or values.have_crossbow:
        methods.scroll_text("You raise your " + ("crossbow" if values.have_crossbow else "bow") + " and fire.")
        time.sleep(1)
        methods.scroll_text("The bolt strikes true... but the Necromancer laughs.")
        time.sleep(1)
        methods.scroll_text("'You found the weapon, but you lack the power to wield it properly.'")
        time.sleep(1)
    else:
        methods.scroll_text("You charge in with only your sword.")
        time.sleep(1)
        methods.scroll_text("The Necromancer smiles. 'A blade? Against ME?'")
        time.sleep(1)

    methods.scroll_text("You fought bravely, but the path you walked was not enough to prepare you.")
    time.sleep(1)
    methods.scroll_text("The Necromancer raises his hand. A bolt of crimson energy strikes you down.")
    time.sleep(1.5)
    methods.scroll_text("Rooms cleared: " + str(values.room_cleared) + " — So close, yet so far.")
    time.sleep(1)
    methods.scroll_text("GAME OVER. The Crimson Isle claims another soul.")


def end2():

    methods.scroll_text("Your fate is cruel.")
    time.sleep(1)
    methods.scroll_text("A misstep. A moment of hesitation.")
    time.sleep(1)
    methods.scroll_text("The Necromancer seizes the opening and drives a cursed blade through your chest.")
    time.sleep(1.5)

    if values.potion_num < 5:
        methods.scroll_text("You had " + str(values.potion_num) + " potions left... you just never got the chance to use them.")
        time.sleep(1)

    methods.scroll_text("GAME OVER. You were the right warrior. Just the wrong moment.")

def end3():

    methods.scroll_text("Your fate is cruel.")
    time.sleep(1)
    methods.scroll_text("A misstep. A moment of hesitation.")
    time.sleep(1)

    if values.potion_num < 5:
        methods.scroll_text("You had " + str(values.potion_num) + " potions left... you just never got the chance to use them.")
        time.sleep(1)

    methods.scroll_text("GAME OVER. You were the right warrior. Just the wrong moment.")


def endLEBRON():
    methods.scroll_text("You stand in the final chamber.")
    time.sleep(1)
    methods.scroll_text("But instead of a Necromancer, you find a throne.")
    time.sleep(1)
    methods.scroll_text("And on that throne... sits King LeBron.")
    time.sleep(1.5)
    methods.scroll_text("'I've been watching you this whole time,' he says, spinning a basketball on one finger.")
    time.sleep(1)
    methods.scroll_text("'You work for King LeBron Inc. You always have.'")
    time.sleep(1)
    methods.scroll_text("'The Necromancer? That was me. The dead teammates? Paid actors.'")
    time.sleep(1.5)
    methods.scroll_text("'This was all... a job interview.'")
    time.sleep(1)
    methods.scroll_text("He stands, extends his hand, and offers you a contract.")
    time.sleep(1)

    if values.room_cleared >= 8:
        methods.scroll_text("'You cleared " + str(values.room_cleared) + " rooms. You're hired. Welcome to the inner circle.'")
        time.sleep(1)
        methods.scroll_text("ENDING: THE LEBRON CHRONICLES. You are now employee of the month.")
    else:
        methods.scroll_text("'Only " + str(values.room_cleared) + " rooms? You're on probation.'")
        time.sleep(1)
        methods.scroll_text("ENDING: THE LEBRON CHRONICLES. You get a participation trophy and a mediocre benefits package.")


def win1():
    # methods.scroll_text("You enter the final chamber.")
    # time.sleep(1)
    # methods.scroll_text("The Necromancer towers before you, wreathed in crimson flame.")
    # time.sleep(1)
    # methods.scroll_text("'You made it this far. Impressive. But it ends HERE.'")
    # time.sleep(1.5)

    if values.room_cleared >= 8:
        methods.scroll_text("But you are not the same adventurer who stepped off that boat.")
        time.sleep(1)
        methods.scroll_text("You cleared " + str(values.room_cleared) + " rooms. You bled for every one of them.")
        time.sleep(1)
    else:
        methods.scroll_text("You are battered, but unbroken.")
        time.sleep(1)

    if values.have_crossbow:
        methods.scroll_text("You raise your crossbow and fire two bolts in quick succession.")
        time.sleep(1)
        methods.scroll_text("The Necromancer staggers. 'Impossible...'")
    elif values.have_bow and values.arrow_amount > 0:
        methods.scroll_text("You draw your bow and loose your last arrow.")
        time.sleep(1)
        methods.scroll_text("It strikes the Necromancer square in the chest, shattering his amulet.")
        end2()

    else:
        methods.scroll_text("You charge, sword raised, screaming the names of your fallen teammates.")
        time.sleep(1)
        methods.scroll_text("Blade meets curse. The Necromancer did not expect sheer will.")

        end2()

    time.sleep(1.5)
    methods.scroll_text("He collapses. The crimson light fades.")
    time.sleep(1)
    methods.scroll_text("The castle shudders. Then silence.")
    time.sleep(1.5)
    methods.scroll_text("You walk out into the cold morning air.")
    time.sleep(1)
    methods.scroll_text("The Crimson Isle is free.")
    time.sleep(1)

    if values.potion_num > 0:
        methods.scroll_text("You still have " + str(values.potion_num) + " potions left. You didn't even need them.")
        time.sleep(1)

    methods.scroll_text("Swords: " + str(values.sword_amount) + "  |  Arrows: " + str(values.arrow_amount) + "  |  Rooms cleared: " + str(values.room_cleared))
    time.sleep(1)
    methods.scroll_text("YOU WIN. The legend of the Crimson Isle will be told for generations.")

#-------------------------------------GAME START----------------------------------------------------------------------------------------
def game_init():
    console.Console().print("Fate: The Crimson Isle", style="red")
    time.sleep(2)
    methods.scroll_text("You are a level 1 adventurer working for King LeBron inc., tasked with exploring the mysterious island, the Crimson Isle.\n")
    time.sleep(1)
    methods.scroll_text("You land amidst the crashing waves, peering back at the approaching vessel. It carries a team of experienced adventurers, the ones that you are meant to shadow on this expedition.\n")
    time.sleep(1)
    methods.scroll_text("However, you don't want to wait for them, so you run off to start exploring.\n")
    time.sleep(1)
    methods.scroll_text("Two...")
    time.sleep(0.5)
    methods.scroll_text("Hours...")
    time.sleep(0.5)
    methods.scroll_text("Later...\n")
    time.sleep(1)
    methods.scroll_text("Returning to the shore, you reach your team's camp.\n")
    time.sleep(1)
    methods.scroll_text("You enter your boss' tent, and start to regale them with your tales of glory from the past two hours.\n")
    time.sleep(1)
    methods.scroll_text("After a few moments, you notice that they have not responded, nor have they moved from their position on the cot.\n")
    time.sleep(1)
    methods.scroll_text("You walk up to them, and put your hand on their shoulder...")
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
    time.sleep(1)
    methods.clear_screen()
    #time.sleep(1)
    play_music("F4T3.mp3")

if __name__ == "__main__":
    title_screen()
