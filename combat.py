import random as r

m = "Miss!"
h = "Hit!"
ph = "Perfect Hit!"
s1 = "-1 Stamina."
s2 = "-2 Stamina."
no_s = "No Stamina Lost."
blocker = "--------------------"


def sword_fighting():
    global sword_amount
    if sword_amount >= 1:
        while battle == True:
            global stamina
            print(blocker)
            print("You use your sword!")
            sword_battle_roll = r.randint(1,6)
            if sword_battle_roll <= 3:
                print(m)
                miss_stamina_loss = r.randint(1,2)
                if miss_stamina_loss == 1:
                    print(s1)
                    stamina = stamina - 1
                else:
                    print(no_s)
                return
            elif sword_battle_roll <= 5:
                print(h)
                print(s1)
                stamina = stamina - 1
                sword_amount = sword_amount - 1
                return
            else:                    
                print(ph)
                print(no_s)
                sword_amount = sword_amount - 1
                return
    else:
        print(blocker)
        print("You do not have any more swords.")
        return

def bow_fighting():
    global arrow_amount
    if arrow_amount >= 1:
        while battle == True:
            global stamina
            print(blocker)
            print("You use your bow!")
            if bow_level == 1:
                bow_battle_roll = r.randint(1,6)
                if bow_battle_roll <= 3:
                    print(m)
                    print(s2)
                    stamina = stamina - 2
                    return
                else:
                    print(ph)
                    print(no_s)
                    return
            else:
                print("You do not have a bow.")
                return
    else:
        print(blocker)
        print("You do not have any more arrows.")
    
def found_monster_actions():
    global battle_action
    print("You stumble upon a " + monster + "!")
    print(" 1 - Attack\n 2 - Use item\n 3 - Flee")
    battle_action = int(input("What do you do?\n: "))
    
def battle_attack_action():
    global battle
    while battle == True:
        print(blocker)
        print(" 1 - " + weapon1 + "\n 2 - " + weapon2 + "\n 5 - Back")
        battle_attack = int(input("What do you use?\n: "))
        if battle_attack == 1:
            sword_fighting()
        elif battle_attack == 2:
            bow_fighting()
        elif battle_attack == 5:
            return
        else:
            print(blocker)
            print("You do not have another weapon!")

def battle_inventory_action():
    global stamina
    global s_pot_num
    global sword_amount
    global arrow_amount
    print(blocker)
    print("Inventory: ")
    print(blocker)
    while battle == True:
        print(" 1 - Stamina Potion\n 2 - Sword\n 3 - Arrows\n 4 - Special Items\n 5 - Back")
        battle_inv = int(input("What do you use?\n: "))
        if battle_inv == 1:
            print(blocker)
            if s_pot_num >= 1:
                print("You used a stamina potion!")
                print(blocker)
                s_pot_num = s_pot_num - 1
                stamina = stamina + 25
            else:
                print("You do not have a stamina potion!")
                print(blocker)
        elif battle_inv == 2:
            print(blocker)
            print("You have " + sword_amount + "swords.")
            return
        elif battle_inv == 3:
            print(blocker)
            print("You have " + arrow_amount + "arrows.")
            return
        elif battle_inv == 4:
            print(blocker)
            
        elif battle_inv == 5:
            return
        else:
            print(blocker)
            print("That is not an option.")

def battle_flee_action():
    global stamina
    global battle
    print(blocker)
    print("You have fled the battle.")
    print("-5 stamina")
    stamina = stamina - 5
    battle = False


stamina = 100
battle = True  
monster = "Goblin"
battle_attack = 0


weapon1 = "Sword"
sword_amount = 5

weapon2 = "Bow"

inv1 = "Stamina Potion"
s_pot_num = 3


while battle == True:
    print(blocker)
    found_monster_actions()
    if battle_action == 1:
        battle_attack_action()
    elif battle_action == 2:
        battle_inventory_action()
    elif battle_action == 3:
        battle_flee_action()
    else:
        print(blocker)
        print("That is not an option!")
        
