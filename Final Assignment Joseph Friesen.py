# Final Project
# Text Based Adventure Game
# ICS3C

# -------------------------
# Variables
# -------------------------

player_health = 100
enemy_health = 50
inventory = []

# -------------------------
# Functions
# -------------------------

def calculate_damage():
    """
    -------------------------------------------------------
    Calculates and returns the damage dealt in combat
    -------------------------------------------------------
    Returns:
        damage (int)
    -------------------------------------------------------
    """
    damage = 10
    return damage

# -------------------------
# Game Loop
# -------------------------

print("Welcome to the Adventure Game!")
print("You start with 100 health.")

game_running = True

while game_running:

    print("\nChoose an action:")
    print("1 Explore")
    print("2 Check inventory")
    print("3 Fight enemy")
    print("4 Quit game")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You explore the area and find a potion.")
        inventory.append("potion")

    elif choice == "2":
        print("Inventory:")
        if len(inventory) == 0:
            print("Your inventory is empty.")
        else:
            for item in inventory:
                print(item)

    elif choice == "3":
        print("You fight the enemy!")

        damage = calculate_damage()
        enemy_health = enemy_health - damage
        player_health = player_health - damage

        print("You deal", damage, "damage.")
        print("Enemy health:", enemy_health)
        print("Your health:", player_health)

        if enemy_health <= 0:
            print("You defeated the enemy!")
            game_running = False

        elif player_health <= 0:
            print("You have been defeated.")
            game_running = False

    elif choice == "4":
        print("Thanks for playing!")
        game_running = False

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
