import random as r
import methods
import constants
import values
import time

monster = "Goblin"


#This function controls the basic combat, allowing the user to choose their actions, and returns it as a number
def battle_menu():
    print(constants.blocker)
    print("You stumble upon a " + monster + "!")
    choice = methods.ask_fixed_bottom(
        constants.wyd,
        ["1", "2", "3"],
        [
            "1 - Attack",
            "2 - Inventory",
            "3 - Hide"
        ]
    )

    if choice == "1":
        battle_fight()
    elif choice == "2":
        battle_inventory_action()
    elif choice == "3":
        battle_flee_action()


#This weapon checks if weapons have been discovered. If discovered, it shares their name
def weapon_checker():
    if values.have_sword:
        values.weapon1 = "Sword"
    else:
        values.weapon1 = "???"
    if values.have_bow:
        values.weapon2 = "Bow"
    else:
        values.weapon2 = "???"
    if values.have_crossbow:
        values.weapon3 = "Crossbow"
    else:
        values.weapon3 = "???"


#This function controls which attack function is called based on the user's choice
def battle_fight():
    weapon_checker()

    print(constants.blocker)
    print("Attack")
    print(constants.blocker)

    choice = methods.ask_fixed_bottom(
        constants.wyd,
        ["1", "2", "3", "5"],
        [
            " 1 - " + values.weapon1,
            "\n 2 - " + values.weapon2,
            "\n 3 - " + values.weapon3,
            "\n 5 - Back"
        ]
    )

    if choice == "1":
        sword_fighting()
    elif choice == "2":
        bow_fighting()
    elif choice == "3":
        # TODO: Add crossbow
        # crossbow_fighting(stamina, have_crossbow)
        battle_menu()
    elif choice == "5":
        battle_menu()


#This function controls the sword fighting process, using swords and stamina
def sword_fighting():

    if values.sword_amount >= 1:
        print(constants.blocker)
        print("You use your sword!")
        time.sleep(0.5)

        sword_battle_roll = r.randint(1,6)

        # Missed
        if sword_battle_roll <= 2:
            print(constants.missed)
            miss_stamina_loss_rng = r.randint(1,2)
            if miss_stamina_loss_rng == 1:
                print(constants.stamina_lost1)
                print(constants.sword_no_sword_wear)
                values.stamina -= 1
            else:
                print(constants.stamina_lost0)
                print(constants.sword_no_sword_wear)

        # Great hit
        elif sword_battle_roll <= 4:
            print(constants.hit)
            print(constants.stamina_lost1)
            print(constants.sword_sword_wear1)
            values.stamina -= 1
            values.sword_amount -= 1
            print(values.win_message)
            return

        # Perfect hit
        else:
            print(constants.perfect_hit)
            print(constants.stamina_lost0)
            print(constants.sword_sword_wear1)
            values.sword_amount -= 1
            print(values.win_message)
            return
    else:
        print(constants.blocker)
        print(constants.no_weapon)


#This function controls the bow fighting process, using arrows and stamina
def bow_fighting():
    if values.have_bow:
        if values.arrow_amount >= 1:
            print(constants.blocker)
            print("You use your bow!")

            bow_battle_roll = r.randint(1,6)

            # Missed
            if bow_battle_roll <= 3:
                print(constants.missed)
                print(constants.stamina_lost2)
                print(constants.bow_arrow_used)
                values.stamina -= 2
                values.arrow_amount -= 1

            # Perfect hit
            else:
                print(constants.perfect_hit)
                print(constants.stamina_lost0)
                print(constants.bow_arrow_used)
                values.arrow_amount -= 1

        else:
            print(constants.blocker)
            print(constants.bow_arrow_used_up)

    else:
        print(constants.blocker)
        print(constants.no_weapon)


#This function controls which function and process is called based ont the user's choice
def battle_inventory_action():
    print(constants.blocker)
    print("Inventory: ")
    print(constants.blocker)

    choice = methods.ask_fixed_bottom(
        constants.wyd,
        [ "1", "2", "3", "4", "5" ],
        [ "1 - Stamina Potion",
            "2 - Swords",
            "3 - Arrows",
            "4 - Special Items",
            "5 - Back"
          ]
    )

    if choice == 1:
        potion()
    elif choice == 2:
        print(constants.blocker)
        print("You have " + str(values.sword_amount) + " swords.")
    elif choice == 3:
        print(constants.blocker)
        print("You have " + str(values.arrow_amount) + " arrows.")
    elif choice == 4:
        print(constants.blocker)
        print("You have " + str(values.keys_amount) + " keys")
    elif choice == 5:
        return

#This function controls the usage of stamina potions
def potion():
    print(constants.blocker)
    print("You have " + str(values.potion_num) + " Stamina Potions")


    print(" 1 - Yes\n 2 - No")
    choice = methods.ask_fixed_bottom(
        "Would you like to use a stamina potion?",
        [ "1", "2" ],
        [
            "1 - Yes",
            "2 - No"
        ]
    )

    if choice == 1:
        if values.potion_num >= 1:
            print(constants.blocker)
            print("You used a stamina potion!")
            values.potion_num -= 1
            values.stamina += 25
        else:
            print(constants.blocker)
            print("You do not have a stamina potion!")
    elif choice == 2:
        battle_inventory_action()

#This function allows the user to flee the battle, ending it prematurely
def battle_flee_action():
    print(constants.blocker)
    print("You have fled the battle.")
    print("-5 stamina")
    values.stamina -= 5