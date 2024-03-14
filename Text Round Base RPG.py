from weapons import *
from items import *
from enemy import *



# Variablen die für alles sichtbar sein müssen
weapon_list = [sword.name, fist.name]
item_list = []

enemy_typ = ""
enemy_health = 0
enemy_item = ""

# Intro
def tutorial():
    print("-->-------    o   -------<--")
    print("Herzlich willkommen in der Kluft von Ragnar")
    input("drücke enter um fortzufahren .....")
    if input("Willst du ein Tutorial?  ja/nein|") == "ja":
        first_encounter()
    else:
        main()

# Hauptmenü
def main():
    global weapon_list
    global item_list
    
    while True:
        main_menu = input("suchen/missionen/rucksack/kampf/?| ")

        if main_menu == "suchen":
            print("Du suchst und findest .....")
        
        elif main_menu == "missionen":
            print("Hier würdest du deine Missionen sehen")
        
        elif main_menu == "rucksack":
            frage = int(input("1. Waffen Rucksack/2. Item Rucksack| "))
            if frage == 1:
                print(weapon_list)
            elif frage == 2:
                print(item_list)
            else:
                print("Ungültige Auswahl!")
        
        elif main_menu == "kampf":
            battle_system()

        elif main_menu == "?":
            tutorial()

        else:
            print("Ungültige Eingabe!")

# Item Rucksack
def item_backpack():
    global item_list
    print(item_list)

# Gegner
def enemy():
    global enemy_typ
    global enemy_health 
    global enemy_item
    enemy_typ = "Wolf"
    enemy_health = 10
    enemy_item = toth.name

# Kampfsystem
def battle_system():
    global enemy_typ
    global enemy_health

    while True:
        aktion = input("angriff/flucht/items/reden| ")

        if aktion == "angriff":
            print(weapon_list)
            attack = input()

            if attack in weapon_list:
                enemy_health -= sword.damage if attack == "Schwert" else fist.damage
                print(f"Leben des Gegners {enemy_health}")

                if enemy_health <= 0:
                    print("--------------------------------")
                    print(f"Du hast den {enemy_typ} besiegt")
                    print(f"Du erhältst {enemy_item}")
                    item_list.append(enemy_item)
                    return main()
            else:
                print("Ungültige Waffe!")

        elif aktion == "flucht":
            print("Du bist entkommen.")
            return 

        elif aktion == "items":
            item_backpack()

        elif aktion == "reden":
            print(f"Der {enemy_typ} will nicht reden")

        else:
            print("Ungültige Aktion!")

# Die erste Begegnung/Tutorial
def first_encounter():
    frage = input("Hast du schon einmal gekämpft? ja/nein| ")
    if frage == "ja":
        print("Du scheinst dich ja gut auszukennen")
        main()
    elif frage == "nein":
        print(f"Du begegnest einem {enemy_typ}")
        battle_system()
    else:
        first_encounter()

# Gegner initialisieren
enemy()
# Tutorial starten
tutorial()
