#Text Round Based RPG
#dies ist mein erster versuch ein Roundbased RPG zu erstellen
from weapons import sword

#intro
def tutorial():
    print("""-->-------    o   -------<--
          """)
    print("Herzlich willkommen in der Kluft von Ragnar")
    input("drücke enter um fortzufaheren .....")
    if input("Willst du ein Tutorial?  ja/nein|") == "ja":
        item_backpack()  # Rucksack nur einmal initialisieren
        first_encounter()
    else:
        main_menu()


#Hauptmenü ist in arbeit
def main_menu():
    global item_list
    main_menu = input("suchen/missionen/rucksack/kampf/?|")

    #man sollte etwas finden
    if main_menu == "suchen":
        print("Du suchst und findest .....")
        return main_menu()
    
    #zeigt später einmal die Missionen
    elif main_menu == "missionen":
        print("Hier würdest du deine Missionen sehen")
        return main_menu()
    
    #Items usw.
    elif main_menu == "rucksack":
        frage = int(input("1. Waffen Rucksack/2. Item Rucksack"))
        if frage == 1:
            print(weapon_list)
            return main_menu()
        elif frage == 2:
            print(item_list)
            return main_menu()
        else:
            return main_menu()
        
    #kämpft mit battle_system    
    elif main_menu == "kampf":
        battle_system()

    #leitet einen ins Tutorial
    elif main_menu == "?":
        tutorial()

#Item Rucksack
def item_backpack():
    global item_list
    global weapon_list
    item_list = []
    weapon_list = ["Schwert", "Faust"]

#Gegner 
def enemy():
    global enemy_typ
    global enemy_health 
    global enemy_item
    #der Gegner
    enemy_typ = "Wolf"
    enemy_health = 10
    enemy_item = "Zahn"
  

def battle_system():
    global weapon_list
    global enemy_typ
    global enemy_health

    aktion = input("angriff/flucht/items/reden|")

    if aktion == "angriff":
        attack = input(weapon_list)
        if attack == "Schwert":
            enemy_health -= sword.damage
            print(f"Leben des Gegners {enemy_health}")
            #wenn der Gegner O health Erreicht hat der Spieler gewonnen 
            if enemy_health <= 0:
                print("--------------------------------")
                print(f"Du hast den {enemy_typ} besiegt")
                print(f"Du erhältst {enemy_item}")
                #fügt den Item_Rucksack das enemy_item hinzu
                item_list.append(enemy_item)
                main_menu()

            else:
                battle_system()
        else:
            print("Ungültige Waffe!")
            battle_system()
    
    elif aktion == "flucht":
        print("Du bist entkommen.")
        main_menu()

    elif aktion == "items":
        item_backpack()

    elif aktion == "reden":
        print(f"Der {enemy_typ} will nicht reden")
        battle_system()

    else:
        print("Ungültige Aktion!")
        battle_system()


#die Erste begegnung/Tutorial
def first_encounter():
    frage = input("Hast du schon einmal Gekämpft?    ja/nein|")
    if frage == "ja":
        print("Du scheinst dich ja gut auszukennen")
        main_menu()
    elif frage == "nein":
        print("du begegnest einen Wolf")
        battle_system()
    else:
        return first_encounter()


enemy()
main_menu()


#testen von classen
#print (sword.damage)
