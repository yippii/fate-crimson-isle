missed = "Miss!"
hit = "Hit!"
perfect_hit = "Perfect Hit!"

stamina_lost0 = "No Stamina Lost."
stamina_lost1 = "You lost a stamina."
stamina_lost2 = "You lost two stamina."

sword_no_sword_wear = "Your sword remains strong!"
sword_sword_wear1 = "You used a sword!."

bow_arrow_used = "You used an arrow!"
bow_arrow_used_up = "You do not have any more arrows!"

wyd = "What will you do?"

no_weapon = "You do not have this weapon!"

blocker = 15*"-"

# Actions (stamina costs)
PICKUP_COIN_COST = -1
ENTER_ROOM_COST = -5
KILL_GOBLIN_SWORD_COST = -2
KILL_GOBLIN_BOW_COST = -3
KILL_GOBLIN_CROSSBOW_COST = -4

# Rewards
STAMINA_POTION_GAIN = 25

PICKUP_COIN_DESC = "Pick up coin (-1 stamina)"
ENTER_ROOM_DESC = "Enter room (-5 stamina)"
KILL_GOBLIN_SWORD_DESC = "Kill goblin with sword (-2 stamina)"
KILL_GOBLIN_BOW_DESC = "Kill goblin with bow (-3 stamina)"
KILL_GOBLIN_CROSSBOW_DESC = "Kill goblin with crossbow (-4 stamina)"
STAMINA_POTION_DESC = "Stamina potion (+25 stamina)"

old_mapData = [
    # Outer rectangle 
    100, "r",
    75, "r",
    100, "r",
    750, "r",
    # Left arm room
    50, "l",
    40, "r",
    80, "r",
    40, "r",
    80, "l",
    # Top-left room
    40, "l",
    25, "l",
    50, "r",
    25, "r",
    50, "l",
    # Top-center room
    30, "r",
    50, "l",
    25, "l",
    50, "r",
    25, "r",
    # Interior horizontal wall
    100, "r",
    60, "l",
    # Interior sub-room
    80, "r",
    70, "r",
    80, "r",
    70, "r",
]

old_l2map = [ 400, "r",
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


MAP1 = """
+------------------------+-------+
|                        |       |
|          +------+      |  L2   |
|          |      |      |       |
|    MH    +------+      +-------+
|                                |
+----+  +----------------+       |
     |  |         |  S   |       |
     |  |   P     +------+       |
 Arm |  +---------+      |       |
     |                   |       |
     |                   |       +-------+
+----+------------------+        |       |
|                                |       |
|    X                           +-------+
|                                |
+--------+----------+------------+
         |          |            |
         +----------+------------+
"""