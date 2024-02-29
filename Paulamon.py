from ASCII import *
import random


print(" .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. .-----------------.".center(200))
print("| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |".center(200))
print("| |   ______     | | |      __      | | | _____  _____ | | |   _____      | | |      __      | | | ____    ____ | | |     ____     | | | ____  _____  | |".center(200))
print("| |  |_   __ \   | | |     /  \     | | ||_   _||_   _|| | |  |_   _|     | | |     /  \     | | ||_   \  /   _|| | |   .'    `.   | | ||_   \|_   _| | |".center(200))
print("| |    | |__) |  | | |    / /\ \    | | |  | |    | |  | | |    | |       | | |    / /\ \    | | |  |   \/   |  | | |  /  .--.  \  | | |  |   \ | |   | |".center(200))
print("| |    |  ___/   | | |   / ____ \   | | |  | '    ' |  | | |    | |   _   | | |   / ____ \   | | |  | |\  /| |  | | |  | |    | |  | | |  | |\ \| |   | |".center(200))
print("| |   _| |_      | | | _/ /    \ \_ | | |   \ `--' /   | | |   _| |__/ |  | | | _/ /    \ \_ | | | _| |_\/_| |_ | | |  \  `--'  /  | | | _| |_\   |_  | |".center(200))
print("| |  |_____|     | | ||____|  |____|| | |    `.__.'    | | |  |________|  | | ||____|  |____|| | ||_____||_____|| | |   `.____.'   | | ||_____|\____| | |".center(200))
print("| |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | |".center(200))
print("| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |".center(200))
print(" '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' ".center(200))


#print(f"{"Hello World":-^20}")

input("Press Enter to begin".center(200))

while True:
    starter_choice = input("Choose your starting Pokemon: Squirtle, Charmander, Bulbasaur")

    if starter_choice.lower() == "squirtle" or starter_choice == "s" :
        starter = "Squirtle"
        starter_health = 12
        squirtle()
        break

    elif starter_choice.lower == "charmander" or starter_choice == "c":
        starter = "Charmander"
        starter_health = 12
        charmander()
        break

    elif starter_choice.lower == starter_choice == "bulbasaur" or starter_choice == "b":
        starter = "Bulbasaur"
        starter_health = 12
        bulbasaur()
        break

    elif starter_choice.lower == starter_choice == "pikachu" or starter_choice == "p":
        starter = "Pikachu"
        starter_health = 14
        pikachu()
        break

    elif starter_choice.lower == "upupdowndownleftrightleftrightbastart":
        starter = "Mew"
        starter_health = 99
        mew()
        break

    else:
        print("Please make a valid choice")
        continue

print(" ")
print(" ")
input("Press enter to begin your adventure with " + starter + "!!")
print(" ")
print(" ")
input("As you and " + starter + " exit the professors workshop you are faced with a choice: Do you set off on your journey to become a Pokemon master, or go back to bed and try again tomorrow?")

while True:
    the_choice = input("So, what will it be? Are you ready?")

    if the_choice.lower == "yes" or the_choice == "y":
        input("You step forward, feeling inspired by the seemingly limitless posibilities that await you and " + starter + ".")
        break

    else:
        print(starter + " looks up at you with sadness in its eyes, imploring you to rethink your decision. " + starter + " knows you are ready.")
        continue

input("You begin walking at first, which quickly turns into a jog, and then a full blown sprint!")
input("This is the moment you've been waiting for, for what feels like your entire life.")
input("You run until you see it...\033[1mTALL GRASS\033[0m...and then you run straight into it!")
input("Not long after setting foot in the grass you hear a shuffle...")
input("You look around...")
input("You keep looking...")
input("!!!!!!!!!!!")

enemies = ("Pidgey" , "Ratata" , "Caterpie")
battle_enemy = random.choice(enemies)
enemy_health = 12

if battle_enemy == "Pidgey" and starter == "Squirtle" :
    squirtle_vs_pidgey()
    input("A wild Pidgey appeared!")
elif battle_enemy == "Ratata" and starter == "Squirtle" : 
    squirtle_vs_pidgey()
    input("A wild Ratata appeared!")
elif battle_enemy == "Caterpie" and starter == "Squirtle" :
    squirtle_vs_pidgey()
    input("A wild Caterpie appeared!")
elif battle_enemy == "Pidgey" and starter == "Charmander" :
    squirtle_vs_pidgey()
    input("A wild Pidgey appeared!")
elif battle_enemy == "Ratata" and starter == "Charmander" :
    squirtle_vs_pidgey()
    input("A wild Ratata appeared!")
elif battle_enemy == "Caterpie" and starter == "Charmander" :
    squirtle_vs_pidgey()
    input("A wild Caterpie appeared!")
elif battle_enemy == "Pidgey" and starter == "Bulbasaur" : 
    squirtle_vs_pidgey()
    input("A wild Pidgey appeared!")
elif battle_enemy == "Ratata" and starter == "Bulbasaur" :
    squirtle_vs_pidgey()
    input("A wild Ratata appeared!")
elif battle_enemy == "Caterpie" and starter == "Bulbasaur" :
    squirtle_vs_pidgey()
    input("A wild Caterpie appeared!")
elif battle_enemy == "Pidgey" and starter == "Pikachu" : 
    squirtle_vs_pidgey()
    input("A wild Pidgey appeared!")
elif battle_enemy == "Ratata" and starter == "Pikachu" :
    squirtle_vs_pidgey()
    input("A wild Ratata appeared!")
elif battle_enemy == "Caterpie" and starter == "Pikachu" :
    squirtle_vs_pidgey()
    input("A wild Caterpie appeared!")
elif battle_enemy == "Pidgey" and starter == "Mew" : 
    squirtle_vs_pidgey()
    input("A wild Pidgey appeared!")
elif battle_enemy == "Ratata" and starter == "Mew" :
    squirtle_vs_pidgey()
    input("A wild Ratata appeared!")
elif battle_enemy == "Caterpie" and starter == "Mew" :
    squirtle_vs_pidgey()
    input("A wild Caterpie appeared!")

while True : 
     
    input("Their Turn!")

    if battle_enemy == "Pidgey" :
            p_a = ("Tackle" , "Sand Attack")
            tackle_dmg = (1,2,3,4)
            attack = random.choice(p_a)
            if attack == "Tackle" :
                input("Pidgey used Tackle!")
                hit = int(random.choice(tackle_dmg))
                input("It hits for " + str(hit) + " damage!")
                if hit == 4 :
                     print("A CRITICAL HIT!!")
                starter_health = starter_health - hit
                input(starter + " has " + str(starter_health) + "HP left.")

            elif attack == "Sand Attack" :
                input("Pidgey used Sand Attack!")
                input(starter + " took no damage!? Who uses Sand Attack anyway?")


    elif battle_enemy == "Ratata" :
            p_a = ("Quick Attack" , "Tail Whip")
            quick_dmg = (1,2,3,4)
            attack = random.choice(p_a)
            if attack == "Quick Attack" :
                input("Ratata used Quick Attack!")
                hit = int(random.choice(quick_dmg))
                input("It hits for " + str(hit) + " damage!")
                starter_health = starter_health - hit
                input(starter + " has " + str(starter_health) + "HP left.")

            elif attack == "Tail Whip" :
                input("Ratata used Tail Whip!")
                input(starter + " took no damage!? Who uses Tail Whip anyway?")


    elif battle_enemy == "Caterpie" :
            p_a = ("Tackle" , "String Shot" , "Bug Bite")
            tackle_dmg = (1,2,3,4)
            bite_dmg = (2,3,4,5,6)
            attack = random.choice(p_a)
            if attack == "Tackle" :
                input("Caterpie used Tackle!")
                hit = int(random.choice(tackle_dmg))
                input("It hits for " + str(hit) + " damage!")
                starter_health = starter_health - hit
                input(starter + " has " + str(starter_health) + "HP left.")

            elif attack == "String Shot" :
                input("Caterpie used String Shot!")
                input(starter + " took no damage!? Who uses String Shot anyway?")

            elif attack == "Bug Bite" :
                input("Caterpie used Bug Bite!")
                hit = int(random.choice(bite_dmg))
                input("It hits for " + str(hit) + " damage!")
                starter_health = starter_health - hit
                input(starter + " has " + str(starter_health) + "HP left.")

    input("Your turn!")

    if starter == "Bulbasaur" :
            player_attack = input("Which attack will you use? Tackle or Vine Whip: ")
            tackle_dmg = (1,2,3,4)
            vine_dmg = (3,4,5,6)
            if player_attack == "Tackle" or player_attack == "tackle" :
                input("Bulbasaur used Tackle!")
                en_hit = int(random.choice(tackle_dmg))
                input("It hits for " + str(en_hit) + " damage!")
                enemy_health = enemy_health - en_hit
                input(battle_enemy + " has " + str(enemy_health) + "HP left.")

            elif player_attack == "Vine Whip" or player_attack == "vine whip" :
                input("Bulbasaur used Vine Whip!")
                en_hit = int(random.choice(vine_dmg))
                input("It hits for " + str(en_hit) + " damage!")
                enemy_health = enemy_health - en_hit
                input(battle_enemy + " has " + str(enemy_health) + "HP left.")

    elif starter == "Squirtle" :
            player_attack = input("Which attack will you use? Tackle or Water Gun: ")
            tackle_dmg = (1,2,3,4)
            water_dmg = (3,4,5,6)
            if player_attack == "Tackle" or player_attack == "tackle" :
                input("Squirtle used Tackle!")
                en_hit = int(random.choice(tackle_dmg))
                input("It hits for " + str(en_hit) + " damage!")
                enemy_health = enemy_health - en_hit
                input(battle_enemy + " has " + str(enemy_health) + "HP left.")

            elif player_attack == "Water Gun" or player_attack == "water gun" :
                input("Squirtle used Water Gun!")
                en_hit = int(random.choice(water_dmg))
                input("It hits for " + str(en_hit) + " damage!")
                enemy_health = enemy_health - en_hit
                input(battle_enemy + " has " + str(enemy_health) + "HP left.")

    elif starter == "Charmander" :
            player_attack = input("Which attack will you use? Tackle or Flamethrower: ")
            tackle_dmg = (1,2,3,4)
            flame_dmg = (3,4,5,6)
            if player_attack == "Tackle" or player_attack == "tackle" :
                input("Charmander used Tackle!")
                en_hit = int(random.choice(tackle_dmg))
                input("It hits for " + str(en_hit) + " damage!")
                enemy_health = enemy_health - en_hit
                input(battle_enemy + " has " + str(enemy_health) + "HP left.")

            elif player_attack == "Flamethrower" or player_attack == "flamethrower" :
                input("Charmander used Flamethrower!")
                en_hit = int(random.choice(flame_dmg))
                input("It hits for " + str(en_hit) + " damage!")
                enemy_health = enemy_health - en_hit
                input(battle_enemy + " has " + str(enemy_health) + "HP left.")

    elif starter == "Pikachu" :
            player_attack = input("Which attack will you use? Tackle or Thunderbolt: ")
            tackle_dmg = (1,2,3,4)
            shock_dmg = (3,4,5,6)
            if player_attack == "Tackle" or player_attack == "tackle" :
                input("Pikachu used Tackle!")
                en_hit = int(random.choice(tackle_dmg))
                input("It hits for " + str(en_hit) + " damage!")
                enemy_health = enemy_health - en_hit
                input(battle_enemy + " has " + str(enemy_health) + "HP left.")

            elif player_attack == "Thunderbolt" or player_attack == "thunderbolt" :
                input("Pikachu used Thunderbolt!")
                en_hit = int(random.choice(shock_dmg))
                input("It hits for " + str(en_hit) + " damage!")
                enemy_health = enemy_health - en_hit
                input(battle_enemy + " has " + str(enemy_health) + "HP left.")

    elif starter == "Mew" :
            player_attack = input("Which attack will you use? Pound or Psychic: ")
            pound_dmg = (4,5,6)
            psy_dmg = (97,98,99)
            if player_attack == "Pound" or player_attack == "pound" :
                input("Mew used Pound!")
                en_hit = int(random.choice(pound_dmg))
                input("It hits for " + str(en_hit) + " damage!")
                enemy_health = enemy_health - en_hit
                input(battle_enemy + " has " + str(enemy_health) + "HP left.")

            elif player_attack == "Psychic" or player_attack == "psychic" :
                input("Mew used Psychic! Its overkill!!")
                en_hit = int(random.choice(psy_dmg))
                input("It hits for " + str(en_hit) + " damage!")
                enemy_health = enemy_health - en_hit
                input(battle_enemy + " has " + str(enemy_health) + "HP left.")

    if enemy_health > 0 and starter_health > 0 :
         continue
    elif enemy_health < 1 and starter_health > 0 :
         input("You won!!")
         input(starter + " looks up to you, as proud as can be. You tell them how amazing they did as you scoop them up onto your shoulder and start running once again!")
         input("You are ready to begin your journey to become a pokemon master.")
         break
    elif enemy_health > 0 and starter_health < 1 :
         print("You lost!? But thats ok, it was just your first battle.")
         break

print("End.")