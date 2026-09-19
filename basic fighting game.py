import random

difficulty=input("choose your difficulty level: [1]easy, [2]medium, [3]hard>>>")
if difficulty=="1":
    player_hp=50
    goblin_hp=30
elif difficulty=="2":
    player_hp=40
    goblin_hp=40
elif difficulty=="3":
    player_hp=30
    goblin_hp=50
inventory=["potion","potion"]
def show_stats():
    print(f"\n--HERO HP:{player_hp},GOBLIN HP:{goblin_hp}")
    print("potion left",len(inventory))

def use_potion():
    global player_hp
    if len(inventory)>0:
        player_hp+=10
        inventory.remove("potion")
        print("You used a potion and restored 10 HP!")
    else:
        print("opssss You have no potions left!")

def player_attack():
    global goblin_hp
    damage=random.randint(3,8)
    if damage==8:
        print("***********CRITICAL HIT!**************")
        goblin_hp-=damage+2
    
    else:
        goblin_hp-=damage
        print(f"You attacked the goblin and dealt{damage} damage!")

def goblin_attack():
    global player_hp
    damage=random.randint(2,6)
    player_hp-=damage
    print(f"The goblin attacked you and dealt{damage} damage!")

def start_battle():

    print("""    
                 /-__/\
                (  o.o  ) 
                (   =   )
                /   |   i  
               /|   |   |   
              { |___|___| }
                /     /\
               /_   /__\
            /                         /

     |       /       /       |
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
  
  -------------------------------------

  | WILD GOBLIN appeared!             |  
  -------------------------------------""")

    while player_hp > 0 and goblin_hp > 0: 
        show_stats()
        print("actions:[1]ATTACK,[2]USE POTION,[3]RUN")
        choice=input("enter you action my boy>>>")
        if choice=="1":
            player_attack()
            if goblin_hp>0:
                goblin_attack()
        elif choice=="2":
            use_potion()
            if goblin_hp>0:
                goblin_attack()
        elif choice=="3":
            print("you ran away from the goblin")
            break
        else:
            print("invalid choice")
            print("you lose your turn bhaii")
            goblin_attack()
    if player_hp<=0:
        print("you have been defeated by the goblin")
        print("""/__/\
                (  >.<  )  <-- Angry/Laughing Goblin
                (   V   )
                /   |   \
               /|   |   |   
              { |___|___| }
                / /     /\
               /__   /__\
            /                          /
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  -------------------------------------

  | Player fainted!                   |
  | WILD GOBLIN stole your gold...    |
  -------------------------------------

  | [ You whited out! ]               |
  -------------------------------------""")
    elif goblin_hp<=0:
        print("you have defeated the goblin")
        print("""/999__/\
                (  x.x  )  <-- Fainted Goblin (Knocked Out)
                (   ~   )
                /   |    
               /|   |   |  
              { |___|___| }
                ______/  <-- Slumped down
    /                         /
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  -------------------------------------

  | WILD GOBLIN fainted!              |
  | You gained 150 EXP Points!        |
  -------------------------------------

  | Found 85 Gold Coins!              |
  -------------------------------------""")

#start the game
start_battle()


    

    
