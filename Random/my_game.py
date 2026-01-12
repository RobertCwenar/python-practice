'''You have two sides:
Player
Opponent

Each has:
health points (HP)
hit chance / dodge
damage range

And:

a while loop that runs as long as someone has HP > 0

random, żeby było losowo

Game logic (step by step)

Start:
Player has 100 HP
Opponent has 100 HP

Round:
Player attacks
you roll: hit / miss
if hit → you roll damage
subtract opponent's HP

Opponent attacks (same)

Display:
damage
current HP of both sides
Loop ends when:
Player's HP ≤ 0 or
Opponent's HP ≤ 0'''


import random

#HP gamer
player_hp = 500
enemy_hp = 500

#Damage gamer 

player_damage = (5, 15)
enemy_damage = (7, 20)

player_hit_chance = 70
enemy_hit_chance = 60

add_weapons = {
    "Weapon Bow": (30, 60),
    "Weapon Sword": (25, 75),
    "Weapon Dagger": (20, 50),
    "Weapon Axe": (15, 35),
    "Weapon Magic Staff": (20, 25),
}

def attack(player_base_damage, weapon_range, hit_chance):
    if random.randint(1,100) <= hit_chance:
        base_dmg = random.randint(*player_base_damage)
        weapon_dmg = random.randint(*weapon_range)
        total_dmg = base_dmg + weapon_dmg
        return total_dmg
    else:
        return 0
                          
round_number = 1

dmg_player = 0
dmg_enemy = 0

# Start Game

while player_hp > 0 and enemy_hp > 0:
    if round_number == 1:
        print(f"Start Game")
    else:
        print(f"You survived we went to the next round. Round: {round_number}")

#Player Attack

    chosen_weapons = random.choice(list(add_weapons.keys()))
    weapon_range = (add_weapons[chosen_weapons])
    dmg_player = attack(player_damage, weapon_range, player_hit_chance)
    enemy_hp -= dmg_player
    if dmg_player > 0:
        print(f"Player hits with {chosen_weapons} for {dmg_player} damage")
    else:
        print("Player misses and deals 0 damage.")
    
        

    if enemy_hp <= 0:
        print("Enemy is dead. You win!")
        break

#Enemy attack 

 
    chosen_weapons = random.choice(list(add_weapons.keys()))
    weapon_range = (add_weapons[chosen_weapons])
    dmg_enemy = attack(enemy_damage, weapon_range, enemy_hit_chance)
    player_hp -= dmg_enemy
    if dmg_enemy > 0:
        print(f"Enemy hits with {chosen_weapons} for {dmg_enemy} damage.")
    else:
        print("Enemy misses and deals 0 damage.")
  
    if player_hp <= 0:
        print("You lose.")
        break     

    round_number += 1
    
# Output HP
    print(f"Player HP: {max(0, player_hp)}")
    print(f"Enemy HP: {max(0, enemy_hp)}")
    print(f"Last Player Damage: {dmg_player}")
    print(f"Last Enemy Damage: {dmg_enemy}")

#Ask player if they want to continue
    choice = input("Continue to next round? (y/n): ").lower()
    if choice != 'y': 
        print("Game stopped player escape.")
        break

print("Game over")
