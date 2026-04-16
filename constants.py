m = "Miss!"
h = "Hit!"
ph = "Perfect Hit!"

no_s = "No Stamina Lost."
sw1 = "You used a sword!."
no_sw = "Your sword remains strong!"
a1 = "You used an arrow!"
tno = "That is not an option!"
wyd = "What do you do?\n: "
nowe = "You do not have this weapon!"
blocker = 15*"-"

# Stamina system
MAX_STAMINA = 100
STARTING_STAMINA = 50

# Actions (stamina costs)
PICKUP_COIN_COST = -1
ENTER_ROOM_COST = -5
KILL_GOBLIN_SWORD_COST = -2
KILL_GOBLIN_BOW_COST = -3
KILL_GOBLIN_CROSSBOW_COST = -4

# Rewards
STAMINA_POTION_GAIN = +25

PICKUP_COIN_DESC = "Pick up coin (-1 stamina)"
ENTER_ROOM_DESC = "Enter room (-5 stamina)"
KILL_GOBLIN_SWORD_DESC = "Kill goblin with sword (-2 stamina)"
KILL_GOBLIN_BOW_DESC = "Kill goblin with bow (-3 stamina)"
KILL_GOBLIN_CROSSBOW_DESC = "Kill goblin with crossbow (-4 stamina)"
STAMINA_POTION_DESC = "Stamina potion (+25 stamina)"

mapData = [
    # Outer rectangle
    400, "r",
    200, "r",
    400, "r",
    200, "r",

    # Move inside (left corridor entrance)
    25, "l",
    150, "l",

    # Inner rectangle (hallway loop)
    150, "r",
    50, "r",
    150, "r",
    50, "r",

    # Small room branch (top middle)
    50, "l",
    25, "l",
    50, "r",
    25, "r",

    # Continue hallway
    100, "r",

    # Right side branch
    50, "l",
    25, "l",
    50, "r",
    25, "r"
]

l2map = [ 400, "r",
            80, "r",
            50, "l",
            200, "l",
            50, "r",
            60, "r",
            400, "r",
            150, "r",
            50, "l",
            100, "l",
            50, "r"
          ]
