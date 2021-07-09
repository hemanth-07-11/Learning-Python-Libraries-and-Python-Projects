import random


from classes.game import Person, bcolors
from classes.inventory import Item
from classes.magic import Spell

fire = Spell("Fire", 25, 600, "Black")
thunder = Spell("Thunder", 25, 600, "Black")
blizzard = Spell("Blizzard", 25, 600, "Black")
meteor = Spell("Meteor", 40, 1200, "Black")
quake = Spell("Quake", 15, 150, "Black")


cure = Spell("Cure", 25, 640, "White")
restore = Spell("Restore", 36, 1200, "White")
maxheal = Spell("Restore", 40, 6000, "White")


potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restors HP/MP of one party member", 9999)
hielixer = Item("Mega-Elixer", "elixer", "Fully restors HP/MP of all party members", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, restore]
enemy_spells = [fire, meteor, maxheal]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

player1 = Person("Volos:", 3260, 165, 280, 34, player_spells, player_items)
player2 = Person("Signy:", 4160, 135, 340, 34, player_spells, player_items)
player3 = Person("Jarll:", 3800, 140, 360, 34, player_spells, player_items)

enemy1 = Person("Golem", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("Magna", 11200, 455, 525, 25, enemy_spells, [])
enemy3 = Person("Golem", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]


def input_num(self):
    while True:
        try:
            user_input = int(input(self))
        except ValueError:
            print(bcolors.FAIL + "\nChoose from available actions\n" + bcolors.ENDC)
        else:
            return user_input




running = True
i = 0

print("\n" + bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" "\n" + "" + bcolors.ENDC)

while running:

    if len(enemies) == 0:
        print(bcolors.OKGREEN + "All enemies have been defeated\n\n" + bcolors.BOLD +
            "-----------YOU WIN!-----------" + bcolors.ENDC)
        break

    elif len(players) == 0:
        print(bcolors.FAIL + "\n" + "All in party have been defeated\n\n" + bcolors.BOLD +
              "-----------YOU LOSE!-----------" + bcolors.ENDC)
        break

    print("====================")
    print("\n")
    print("NAME                 HP                                   MP")

    for player in players:
        player.get_stats()

    print("\n")
    print("ENEMY                HP")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        player.choose_action()
        choice = input_num("    Choose action:")

        index = int(choice) - 1


        if int(choice) == 0 or int(choice) > 3:
            print(bcolors.FAIL + "\nChoose from available actions" + bcolors.ENDC)
            player.choose_action()
            choice = input("    Choose action:")
            index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            if enemy == -1 or enemy > len(enemies) - 1:
                print(bcolors.FAIL + "\nChoose from available targets" + bcolors.ENDC)
                dmg = player.generate_damage()
                enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print("\n", bcolors.FAIL + player.name.replace(":", " ") + "attacked",
                  enemies[enemy].name, "causing", dmg, "points of damage." + bcolors.ENDC)

       
            if enemies[enemy].get_hp() == 0:
                print(bcolors.FAIL + enemies[enemy].name, "has died." + bcolors.ENDC)
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose spell:")) - 1


            if magic_choice == -1 or magic_choice > len(player_spells) - 1:
                print(bcolors.FAIL + "\nChoose from available spells" + bcolors.ENDC)
                player.choose_magic()
                magic_choice = int(input("    Choose spell:")) - 1

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                player.choose_action()
                choice = input("    Choose action:")
                index = int(choice) - 1

            player.reduce_mp(spell.cost)

            # Healing spells to restore hp
            if spell.kind == "White":
                player.heal(magic_dmg)
                print("\n" + bcolors.OKBLUE + player.name.replace(":", " ") + "cast", spell.name +
                      ", it heals", str(magic_dmg), "HP" + bcolors.ENDC)


            elif spell.kind == "Black":
                enemy = player.choose_target(enemies)
                # Avoid error for incorrect input
                if enemy == -1 or enemy > len(enemies) - 1:
                    print(bcolors.FAIL + "\nChoose from available targets" + bcolors.ENDC)
                    enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)
                print("\n" + bcolors.OKBLUE + player.name.replace(":", " ") + "cast", spell.name, "on",
                      enemies[enemy].name + ", it deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

                # Determine if enemy can be attacked
                if enemies[enemy].get_hp() == 0:
                    print(bcolors.FAIL + enemies[enemy].name, "has died." + bcolors.ENDC)
                    del enemies[enemy]


        # Use Items
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item:")) - 1

            if item_choice == -1 or item_choice > len(player_items) - 1:
                print(bcolors.FAIL + "\nChoose from available items" + bcolors.ENDC)
                player.choose_item()
                item_choice = int(input("    Choose item:")) - 1

            item = player.items[item_choice]["item"]

            # Determine if enough to use
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n", player.name.replace(":", " ") + "is out of", item.name + bcolors.ENDC)
                player.choose_item()
                item_choice = int(input("    Choose item:")) - 1

            player.items[item_choice]["quantity"] -= 1

            if item.kind == "potion":
                player.heal(item.prop)
                print("\n" + bcolors.OKBLUE + player.name.replace(":", " ") + "used",
                      item.name + ", it heals", str(item.prop), "HP" + bcolors.ENDC)

            elif item.kind == "elixer":

                if item.name == "Mega-Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp

                player.hp = player.maxhp
                player.mp = player.maxmp
                print("\n" + bcolors.OKBLUE + player.name.replace(":", " ") + "used", item.name +
                      ", it fully restores HP and MP" + bcolors.ENDC)

            elif item.kind == "attack":
                enemy = player.choose_target(enemies)
                # Avoid error for incorrect input
                if enemy == -1 or enemy > len(enemies) - 1:
                    print(bcolors.FAIL + "\nChoose from available targets" + bcolors.ENDC)
                    enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.prop)
                print("\n" + bcolors.FAIL + player.name.replace(":", " ") + "used", item.name,
                      "on", enemies[enemy].name + ", it causes", item.prop, "points of damage" + bcolors.ENDC)

                # Determine if enemy can be attacked
                if enemies[enemy].get_hp() == 0:
                    print(bcolors.FAIL + enemies[enemy].name, "has died." + bcolors.ENDC)
                    del enemies[enemy]

    print("\n")
    # Enemy attacks
    for enemy in enemies:
        enemy_choice = random.randrange(0, 3)

        # Use Attack
        if enemy_choice == 0:
            target = random.randrange(0, len(players))
            enemy_dmg = enemy.generate_damage()
            # Random index to chose what player is attacked, remove : from player names in print out
            players[target].take_damage(enemy_dmg)
            print(bcolors.FAIL + enemy.name, "attacks", players[target].name.replace(":", ","),
                  "causing", str(enemy_dmg), "points of damage" + bcolors.ENDC)

            # Determine if player can be attacked
            if players[target].get_hp() == 0:
                print(bcolors.FAIL + players[target].name.replace(":", ""), "has died." + bcolors.ENDC)
                del players[target]

        # Use Magic
        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            # Healing spells to restore hp
            if spell.kind == "White":
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + enemy.name, "cast", spell.name.replace(" ", ","),
                      "it heals", str(magic_dmg), "HP" + bcolors.ENDC)

            # Attack spells to cause damage
            elif spell.kind == "Black":
                target = random.randrange(0, len(players))
                players[target].take_damage(magic_dmg)

                print(bcolors.OKBLUE + enemy.name, "cast", spell.name, "on",
                      players[target].name.replace(":", ","),  "it deals", str(magic_dmg),
                      "points of damage" + bcolors.ENDC)

                # Determine if player can be attacked
                if players[target].get_hp() == 0:
                    print(bcolors.FAIL + players[target].name.replace(":", ""), "has died." + bcolors.ENDC)
                    del players[target]



