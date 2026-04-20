import random as r
import methods
import constants
import values
import time

monster = "Goblin"


# Battle main menu, called from main during enemy rooms
def battle_menu():
    methods.clear_screen()
    print(constants.blocker)
    methods.scroll_text("You stumble upon a " + monster + "!")
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
        battle_inventory()
    elif choice == "3":
        battle_flee()


# Post-battle report, initiated from sword_fighting() and bow_fighting()
def battle_ending(mode, missed):
    # Sword
    if mode == 1:
        if not missed:
            print(f"Stamina left: {values.stamina}\nSword left: {values.sword_amount}")
            time.sleep(0.5)
        else:
            print(f"Stamina left: {values.stamina}")
            time.sleep(0.5)
    # Bow
    elif mode == 2:
        print(f"Stamina left: {values.stamina}\nArrows left: {values.arrow_amount}")
        time.sleep(0.5)


# Check if weapon is owned, if not, make it "???"
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


# Fight menu, initiated from battle_menu()
def battle_fight():
    weapon_checker()

    methods.clear_screen()

    print(constants.blocker)
    print("Attack")
    print(constants.blocker)
    print()

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


# Sword fighting, initiated from battle_fight()
def sword_fighting():
    methods.clear_screen()
    if values.sword_amount >= 1:
        print(constants.blocker)
        print("You used your sword!")
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
                battle_ending(1, True)
                battle_fight()
            else:
                print(constants.stamina_lost0)
                print(constants.sword_no_sword_wear)
                battle_fight()

        # Great hit
        elif sword_battle_roll <= 4:
            print(constants.hit)
            print(constants.stamina_lost1)
            print(constants.sword_sword_wear1)
            values.stamina -= 1
            values.sword_amount -= 1
            battle_ending(1, False)
            return

        # Perfect hit
        else:
            print(constants.perfect_hit)
            print(constants.stamina_lost0)
            print(constants.sword_sword_wear1)
            values.sword_amount -= 1
            battle_ending(1, False)
            return

    # No swords left
    else:
        print(constants.blocker)
        print(constants.no_weapon)
        time.sleep(0.5)
        battle_fight()


# Bow fighting, initiated from battle_fight()
def bow_fighting():
    methods.clear_screen()
    if values.have_bow:
        if values.arrow_amount >= 1:
            print(constants.blocker)
            print("You used your bow!")

            bow_battle_roll = r.randint(1,6)

            # Missed
            if bow_battle_roll <= 3:
                print(constants.missed)
                print(constants.stamina_lost2)
                print(constants.bow_arrow_used)
                values.stamina -= 2
                values.arrow_amount -= 1
                battle_ending(2, True)

            # Perfect hit
            else:
                print(constants.perfect_hit)
                print(constants.stamina_lost0)
                print(constants.bow_arrow_used)
                values.arrow_amount -= 1
                battle_ending(2, False)

        # No arrows
        else:
            print(constants.blocker)
            print(constants.bow_arrow_used_up)
            time.sleep(0.5)
            battle_fight()

    # No bow
    else:
        print(constants.blocker)
        print(constants.no_weapon)
        time.sleep(0.5)
        battle_fight()


# Inventory system, initiated from battle_menu()
def battle_inventory():
    methods.clear_screen()
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

    if choice == "1":
        potion()
    elif choice == "2":
        print(constants.blocker)
        print("You have " + str(values.sword_amount) + " swords.")
        time.sleep(0.5)
        battle_inventory()
    elif choice == "3":
        print(constants.blocker)
        print("You have " + str(values.arrow_amount) + " arrows.")
        time.sleep(0.5)
        battle_inventory()
    elif choice == "4":
        print(constants.blocker)
        print("You have " + str(values.keys_amount) + " keys")
        time.sleep(0.5)
        battle_inventory()
    elif choice == "5":
        battle_menu()

# Initiated from battle_inventory_action()
def potion():
    print(constants.blocker)
    print("You have " + str(values.potion_num) + " Stamina Potions")

    choice = methods.ask_fixed_bottom(
        "Would you like to use a stamina potion?",
        [ "1", "2" ],
        [
            "1 - Use a stamina potion",
            "2 - Maybe later"
        ]
    )

    if choice == "1":
        if values.potion_num >= 1:
            print(constants.blocker)
            print("You used a stamina potion!")
            values.potion_num -= 1
            values.stamina += 25
        else:
            print(constants.blocker)
            print("You do not have a stamina potion!")
    elif choice == 2:
        battle_inventory()

# This function allows the user to flee the battle, ending it prematurely
def battle_flee():
    methods.clear_screen()
    print(constants.blocker)
    print("You have fled the battle.")
    print("-5 stamina")
    values.stamina -= 5
    print(f"Stamina left: {values.stamina}")
    return