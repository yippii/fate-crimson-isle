import time
import turtle
import argparse
import rich.console as console
import sys

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
    title.color("#FF2200")
    title.goto(0, 80)
    title.write("FATE:", align="center", font=("Impact", 67, "bold"))
    title.goto(0, 30)
    title.write("The Crimson Isle", align="center", font=("Impact", 24, "bold"))
    # subtitle
    title.color("#FF6600")
    title.goto(0, -40)
    title.write("A terminal roguelike adventure", align="center", font=("Impact", 16, "bold"))
    # start instruction
    title.color("#FF2200")
    title.goto(0, -100)
    title.write("Click anywhere to begin", align="center", font=("Impact", 16, "bold"))
    # decorative line
    title.goto(-200, 10)
    title.pendown()
    title.color("#FF2200")
    title.pensize(3)
    title.forward(400)
    title.penup()
    screen.update()

    try:
        parser = argparse.ArgumentParser(description="Fate: The Crimson Isle", exit_on_error=False)
        parser.add_argument("-s", "--skip", action="store_true", help="Skip Game")
        args = parser.parse_args()

        # click to exit
        def start_game(x, y):
            if args.skip:
                continueOnTerminal()
                room1()
            else:
                continueOnTerminal()
                game_init()
                room1()
    except argparse.ArgumentError:
        def start_game(x, y):
            continueOnTerminal()
            game_init()
            room1()

    screen.onclick(start_game)
    turtle.done()


def continueOnTerminal():
    methods.clear_gui(screen)
        # draw title
    title.color("#FF2200")
    title.goto(0, 80)
    title.write("Fate:", align="center", font=("Impact", 48, "bold"))
    title.goto(0, 30)
    title.write("The Crimson Isle", align="center", font=("Impact", 24, "bold"))
    title.color("#FF6600")
    title.goto(0, -40)
    title.write("Continue on terminal", align="center", font=("Impact", 14, "bold"))
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
|    |    |         |             +-------+
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
    +---+  -  +-----+   +---------+         |
    |      |        |             |         |
    |      |        |             +---------+
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
            mh(knight)
            room2(knight)
        case "2":
            methods.clear_screen()
            armory(knight)
            room2(knight)
        case "3":
            methods.clear_screen()
            room2(knight)

def room2(knight):
    knight.goto(110, 130)
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
            closet(knight)
            room3(knight)
        case "2":
            warChest(knight)
            room3(knight)
        case "3":
            lab(knight)
            room3(knight)

def room3(knight):
    methods.clear_screen()
    knight.goto(110, -70)
    methods.scroll_text("As you turn, the next hallway reveals only two doors: The Elixir Vault and a Blade Vault.")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2", "3", "le bron"],
        [
            "You have two options",
            "1. Explore the Elixir Vault",
            "2. Venture into the Blade vault",
            "3. Inspect the Rune Door",
            "3. ???"
        ],
    )

    match choice:
        case "1":
            elixirVault(knight)
            room4(knight)
        case "2":
            bladeVault(knight)
            room4(knight)
        case "3":
            runeRoom(knight)
            room4(knight)
        case "le bron":
            methods.clear_screen()
            methods.scroll_text("You seek the wisdom of the King LeBron James")
            endLEBRON()
            

def room4(knight):
    methods.clear_screen()
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

def L2room2(knight):
    knight.goto(-130, 167)
    methods.scroll_text("The hallway continues, and you find yourself facing two doorways before you: one pulsing with unsettling activity, and a faint, desperate scream suggesting something terrible is happening within.")

    choice = methods.ask_fixed_bottom(
        "what will you do?",
        ["1", "2"],
        [
            "You have two options",
            "1. Explore the Quiver Room",
            "2. Explore the Kings Hoard.",
        ],
    )

    match choice:
        case "1":
            quiverRoom(knight)
        case "2":
            kingsHoard(knight)

def boss_fight(knight):
    knight.goto(-150, -140)
    methods.scroll_text("The chamber doors slam shut behind you.")
    time.sleep(1)
    methods.scroll_text("A figure emerges from the shadows, robes bleeding crimson light.")
    time.sleep(1)
    methods.scroll_text("'So... you actually made it.'")
    time.sleep(1)
    methods.scroll_text("'I watched you cut through my goblins like they were nothing.'")
    time.sleep(1)
    methods.scroll_text("'Impressive. Truly. But also... deeply annoying.'")
    time.sleep(1.5)
    methods.scroll_text("He steps forward. The temperature drops. The torches flicker and die.")
    time.sleep(1)
    methods.scroll_text("'Do you know how long I spent building this army? Years. YEARS.'")
    time.sleep(1)
    methods.scroll_text("'And you just... waltzed through it in an afternoon.'")
    time.sleep(1.5)
    methods.scroll_text("'Dooming testament of Avril — you made it all the way here.'")
    time.sleep(1)
    methods.scroll_text("'But this is where your story ends.'")
    time.sleep(1)
    methods.scroll_text("He raises his staff. Crackling energy coils around his hands.")
    time.sleep(1)
    methods.scroll_text("'I am the Necromancer of the Crimson Isle. I have felled kingdoms.'")
    time.sleep(1)
    methods.scroll_text("'I killed your teammates without even leaving this chamber.'")
    time.sleep(1.5)
    methods.scroll_text("'And I will do the same to you.'")
    time.sleep(1)
    methods.scroll_text("Let the games begin.")
    time.sleep(0.5)
    methods.scroll_text("HAHAHAHA...")

    if not values.kingsHoard_ROOM:
        win1()
    else:
        end2()

#------------------------ ROOMS -------------------------------------------------------------------------------------------------------------

def mh(knight):
    knight.goto(0, 80)
    methods.clear_screen()
    methods.scroll_text("You enter into the mess hall, where you encounter a Goblin eating raw fish.")

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
            methods.scroll_text("You have gained 1 stamina potions!")
            methods.scroll_text("You have "+ str(values.potion_num) + " potions left!")

            values.room_cleared = values.room_cleared + 1

            #Letter
            methods.clear_screen()
            methods.scroll_text("The goblin drops a torn letter, drenched in spoiled wine.")
            methods.scroll_text("You can barely make out the gist of the letter thanks to some bolded words.\n")

            methods.scroll_text("If uyo ___ tish ___, knwo taht a ___ ftae hsa blefalen me.")

            methods.scroll_text("Stradned on ___ fergotton isle, I ___ my dyas hdiing form teh herrific ___ taht ___ tish desoltea ___.")

            methods.scroll_text("Threough mnay nrarow ___ form ___ dinezens of tish hantedu ___, I hvae uncevered ___" + "\033[1m" + "sretce droo." + "\033[0m")

            methods.scroll_text("Tshee lade to untdol ___, btu to ensrue taht no ___ gets thier grudby ___ on tmeh, I hvae lckoed ___, adn \033[1m" + "hiddne tis kyse" + "\033[0m" + "___ teh ___.")

            methods.scroll_text("Godo lkcu, felolw advanturer.")
            time.sleep(3)
        case "2":
            methods.scroll_text("You back away slowly and leave the mess hall.")

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
    knight.goto(110, 200)
    methods.clear_screen()
    riddle_question = "How many letters are in the alphabet?"
    riddle = True

    methods.scroll_text("You find a locked chest with a riddle on it.")
    methods.scroll_text("You presume that you must solve the riddle to open the chest:")
    methods.scroll_text('(You can also give up by typing, "I give up")\n')

    while riddle:
        methods.clear_screen()
        methods.scroll_text(riddle_question)
        riddle_guess = (input("-> "))
        if riddle_guess == str(len(riddle_question.strip()[-13:-2])):
            methods.scroll_text("\nThe chest opens, and reveals a key.\n")
            values.blue_key2 = True
            riddle = False
        elif riddle_guess == "I give up":
            methods.scroll_text("\nThe chest remains stagnant.\n")
            riddle = False
        else:
            methods.scroll_text("Wrong answer.\n")

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


def lab(knight):
    knight.goto(30, 160)
    methods.clear_screen()
    methods.scroll_text("As you enter the alchemy lab, you find a bunch of documents explaining how to make a stamina potion.")
    # + Potion
    values.potion_num += 1
    methods.scroll_text("You have gained 1 stamina potions!")
    methods.scroll_text("You have " + str(values.potion_num) + " potions left!")
    time.sleep(1.5)
    values.room_cleared = values.room_cleared + 1

def elixirVault(knight):
    knight.goto(190, -120)
    methods.clear_screen()
    methods.scroll_text("As you enter The Elixir Vault, you find a bunch potions lying around. You take two of them.")
    # + Potion
    values.potion_num += 2
    methods.scroll_text("You have gained 2 stamina potions!")
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

def runeRoom(knight):
    knight.goto(110, -120)
    methods.clear_screen()
    methods.scroll_text("You press your hand against the rune door. It groans open, revealing a dim chamber.")
    time.sleep(1)
    methods.scroll_text("In the centre of the room stands a stone pedestal. On it, four symbols are carved:")
    time.sleep(1)
    methods.scroll_text("  MOON   —   SUN   —   STAR   —   VOID")
    time.sleep(1)
    methods.scroll_text("Below them, an inscription reads:")
    time.sleep(1)
    methods.scroll_text("'I have cities, but no houses live there.")
    time.sleep(0.5)
    methods.scroll_text(" I have mountains, but no trees grow there.")
    time.sleep(0.5)
    methods.scroll_text(" I have water, but no fish swim there.")
    time.sleep(0.5)
    methods.scroll_text(" I have roads, but no one travels them.'")
    time.sleep(1.5)
    methods.scroll_text("You must press one of the four symbols to unseal the chest behind the pedestal.")
    methods.scroll_text('(Type your answer, or "I give up" to leave empty-handed)\n')

    solved = False
    attempts = 0
    max_attempts = 3

    while not solved and attempts < max_attempts:
        methods.scroll_text("MOON  /  SUN  /  STAR  /  VOID")
        guess = input("-> ").strip().upper()

        if guess == "I GIVE UP":
            methods.scroll_text("\nYou back away from the pedestal. The runes dim. The chest stays sealed.")
            time.sleep(1)
            break
        elif guess in ["MAP", "A MAP"]:
            methods.scroll_text("\nThe pedestal shudders. The chest flies open.")
            time.sleep(1)
            methods.scroll_text("Inside: a vial of shimmering liquid and a torn journal page.")
            time.sleep(1)
            methods.scroll_text("The journal reads: 'The Necromancer fears only one thing — his own name spoken aloud.'")
            time.sleep(1)
            values.potion_num += 2
            methods.scroll_text("You gained 2 stamina potions!")
            methods.scroll_text("You have " + str(values.potion_num) + " potions left!")
            values.room_cleared += 1
            solved = True
        elif guess in ["MOON", "SUN", "STAR", "VOID"]:
            attempts += 1
            methods.scroll_text("\nThe runes flash red. A surge of energy knocks you back.")
            time.sleep(1)
            if attempts < max_attempts:
                methods.scroll_text("Wrong symbol. Attempts remaining: " + str(max_attempts - attempts))
            else:
                methods.scroll_text("The chamber locks. You've exhausted the pedestal's patience.")
                time.sleep(1)
                methods.scroll_text("You leave with nothing but singed fingertips.")
                time.sleep(1)
        else:
            attempts += 1
            methods.scroll_text("\nNothing happens. The symbols stare back at you.")
            if attempts < max_attempts:
                methods.scroll_text("Attempts remaining: " + str(max_attempts - attempts))
            else:
                methods.scroll_text("The runes go dark. The room seals itself. You leave empty-handed.")
                time.sleep(1)

    time.sleep(1.5)

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
    methods.scroll_text("You have gained 1 stamina potions!")
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
            methods.scroll_text("You Have " + str(values.sword_amount) + " swords left!")
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
    methods.scroll_text("You enter the Kings Hoard. You find a crossbow")
    values.have_crossbow = True
    values.arrow_amount = values.arrow_amount + 2 * constants.ARROW_GAIN
    values.room_cleared = values.room_cleared + 1
    if values.blue_key1 == True and values.blue_key2 == True:
        values.kingsHoard_ROOM = False
        methods.scroll_text("Peering behind a mountain of gold, you spot a gilded diamond chest with two keyholes.")
        time.sleep(1)
        methods.scroll_text("You use the two blue keys you found to open the chest, but only a glimmering blue gemstone is inside.")
        time.sleep(1)
        methods.scroll_text("Instinctively, you reach out towards the gemstone, and as your fingers brush against it, a surge of energy courses through your body.")
        time.sleep(1)
        methods.scroll_text("Without a doubt, you know that you can overcome whatever challenge lies ahead of you now.")
    else:
        values.kingsHoard_ROOM = True

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
    input("Press enter to end...")
    sys.exit()

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
    methods.scroll_text("Swords: " + str(values.sword_amount) + "  |  Arrows: " + str(values.arrow_amount) + "  |  Rooms cleared: " + str(values.room_cleared))
    input("Press enter to end...")
    sys.exit()

def end3():

    methods.scroll_text("Your fate is cruel.")
    time.sleep(1)
    methods.scroll_text("A misstep. A moment of hesitation.")
    time.sleep(1)

    if values.potion_num < 5:
        methods.scroll_text("You had " + str(values.potion_num) + " potions left... you just never got the chance to use them.")
        time.sleep(1)

    methods.scroll_text("GAME OVER. You were the right warrior. Just the wrong moment.")
    methods.scroll_text("Swords: " + str(values.sword_amount) + "  |  Arrows: " + str(values.arrow_amount) + "  |  Rooms cleared: " + str(values.room_cleared))
    input("Press enter to end...")
    sys.exit()


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

    if values.room_cleared >= 2:
        methods.scroll_text("'You fought your way through. You're hired. Welcome to the inner circle.'")
        time.sleep(1)
        methods.scroll_text("ENDING: THE LEBRON CHRONICLES. You are now employee of the month.")
        input("Press enter to end...")
        sys.exit()
    else:
        methods.scroll_text("'Only " + str(values.room_cleared) + " rooms? You're on probation.'")
        time.sleep(1)
        methods.scroll_text("ENDING: THE LEBRON CHRONICLES. You get a participation trophy and a mediocre benefits package.")
        input("Press enter to end...")
        sys.exit()

def end_stamina():
    methods.scroll_text("Your legs give out beneath you.")
    time.sleep(1)
    methods.scroll_text("The potions are gone. The wounds are too many.")
    time.sleep(1)
    methods.scroll_text("You slump against the cold stone wall, sword slipping from your fingers.")
    time.sleep(1.5)
    methods.scroll_text("The Necromancer steps over you without even glancing down.")
    time.sleep(1)
    methods.scroll_text("'Pathetic,' he murmurs. 'I expected more from LeBron's errand boy.'")
    time.sleep(1.5)
    methods.scroll_text("The torches go dark. The cold creeps in.")
    time.sleep(1)
    methods.scroll_text("GAME OVER — Drained dry. The Crimson Isle does not forgive the weak.")
    methods.scroll_text("Potions used: all of them  |  Rooms cleared: " + str(values.room_cleared))
    input("Press enter to end...")
    sys.exit()

def win1():

    if values.room_cleared >= 2:
        end2()

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
    methods.scroll_text("You walk out into the cold morning breeze.")
    time.sleep(1)
    methods.scroll_text("The Crimson Isle is free.")
    time.sleep(1)

    if values.potion_num > 0:
        methods.scroll_text("You still have " + str(values.potion_num) + " potions left. You didn't even need them.")
        time.sleep(1)

    methods.scroll_text("Swords: " + str(values.sword_amount) + "  |  Arrows: " + str(values.arrow_amount) + "  |  Rooms cleared: " + str(values.room_cleared))
    time.sleep(1)
    methods.scroll_text("YOU WIN. The legend of The Crimson Isle will be told for generations.")
    input("Press enter to end...")
    sys.exit()

#-------------------------------------GAME START----------------------------------------------------------------------------------------
def game_init():
    time.sleep(0.3)
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
    time.sleep(1)                   
    methods.scroll_text("Consumed with a desire for revenge, you know that you must avenge them.")
    time.sleep(1)
    methods.scroll_text("Grabbing their swords, you leave the camp to begin your journey.")
    time.sleep(1)
    methods.scroll_text("Looking up, you see a forbidding castle high up on a towering mountain, glowing with crimson light.")
    time.sleep(1)
    methods.scroll_text("You know where you must go.")
    time.sleep(2)
    methods.clear_screen()
    #time.sleep(1)
    play_music("F4T3.mp3")

if __name__ == "__main__":
    title_screen()