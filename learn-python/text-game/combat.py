from random import randint
import sys

test_enemies = {"Skeleton" : 15, "Ghost" : 12, "Slime" : 0, "Red Slime" : -3}

#for i in enemies:
#    print(i+":", enemies[i])

def combat(player_health, potions, enemies):
    """Runs through the combat sequence while player and total enemy health is greater than 0"""
    """Iterates once per player attack(players can use one health potion per turn)"""

    while player_health > 0:

        total_enemy_health = 0
        for enemy in enemies:
            if enemies[enemy] <= 0:
                enemies[enemy] = 0
            total_enemy_health += enemies[enemy]

        if total_enemy_health <= 0:
            return "victory"

        """Prints player health if this is the first turn"""
        print("You have %d health\n" % player_health)
        
        """Prints health of all enemies with greater than 0 health"""
        print("Enemy Health:")
        for enemy in enemies:
            if enemies[enemy] > 0:
                print(enemy+": ", enemies[enemy], "HP", sep='')
        print("")

        """Ask the player what they want to do and record their answer in the variable 'action'"""
        print("What would you like to do?")
        action = input('> ')


        """Let the player use a health potion if they have any in their inventory""" 
        if action == "use potion":
            used_potion = 0 
            player_health += 50
            print("Your health is now %d" % player_health) 
            potions -= 1
            print("You have %d health potions remaining" % potions)
            used_potion = 1

            """Ask player what they want to do again"""
            """If they try and use another potion, do not let them otherwise continue with combat"""
            action = input('> ')
            if action == "use potion":
                print("You have already used a potion this turn")
                print("What would you like to do?")
                action = input('> ')


        """Lets player attack enemies, one at a time"""
        """player has a 5\% miss chance"""
        target = action.replace("attack ", "")
        target_health = enemies[target]
        if randint(0, 99) < 5:
            print("Your attack missed")
        else:
            damage = randint(10, 20)
            print("You attacked %s and did %d damage" % (target, damage))
            enemies[target] -= damage
            if enemies[target] <= 0:
                print("You have slain %s" % target)

        """Enemy attacks"""
        for enemy in enemies:
            if enemies[enemy] > 0:
                if randint(0, 99) < 5:
                    print("The %s's attack missed" % enemy)
                else:
                    damage = randint(10, 20)
                    print("%s attacked you and did %d damage" % (enemy, damage))
                    player_health -= damage
                    if player_health <= 0:
                        print("You have been slain")
                        exit(1)


















#result = combat(100, 0, test_enemies)
#print(result)
