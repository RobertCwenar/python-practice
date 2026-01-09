'''
random = z ang. losowy 

random () 0<= x <1

uniform(a, b) a <= x <= b - zwraca liczby zmiennoprzecinkowe

randint(a, b) a <= x <= b - zwraca liczby całkowite

randrange(10) 0 <= x < 10

randrange (0, 15, 2) 0 <= x < 15 co 2 parzyste z puli (0, 2, 4, 6...14)


import random

def will_weapon_hit (weapon_chance_to_hit_percentage):
    hit_chance = random.uniform(0,100)
    if hit_chance <= weapon_chance_to_hit_percentage:
        return "Hit"
    else:
        return "not hit"
    


x = 0 

listHit = []

while x < 1000:
    x = x+1 
    listHit.append(will_weapon_hit(50))

from collections import Counter

dicttionaryHit = Counter(listHit)

print(dicttionaryHit)
x = 0

while x < 10:
    x = x + 1
    print((random.randint(0,100)))


# exercise 16.1 
# Napisz program, który symuluje rzuty kostką.
# Kostka ma 6 ścian.
# Funkcja roll_dice(chance_to_win):
# Losuje liczbę od 1 do 6 (jak kostka).
# Jeśli wylosowana liczba jest mniejsza lub równa chance_to_win → zwraca "Win".
# W przeciwnym razie → zwraca "Lose".
# Symuluj 15 rzutów i zlicz ile było "Win", a ile "Lose".

import random
from collections import Counter

def roll_dice(chance_to_win):
    dice_roll = random.uniform(1, 6)
    if dice_roll <= chance_to_win:
        return "Win"
    else:
        return "Lose"

relut = 0

listResults = []

while relut <= 15:
    relut = relut + 1
    listResults.append(roll_dice(3))

dictionaryResults = Counter(listResults)
print(dictionaryResults)

# exercise 16.2
# Napisz program, który symuluje strzały z łuku.

def shoot_arrow(chance_to_hit):
    hit_chance = random.uniform(0, 100)
    if hit_chance <= chance_to_hit:
        return "Hit"
    else:
        return "Miss"

arrow_shoots = 0

listShoots = []

while arrow_shoots < 500:
    arrow_shoots = arrow_shoots + 1
    listShoots.append(shoot_arrow(60))

dictionaryShoots = Counter(listShoots)
print(dictionaryShoots)
'''
# exercise 16.3

"""Symulacja rzutu kilku broni

Masz 3 bronie, każda z inną szansą trafienia:
Broń A → 60% szansy na trafienie
Broń B → 75% szansy na trafienie
Broń C → 50% szansy na trafienie

Napisz funkcję weapon_hit(chance) podobną do Twojej wcześniejszej funkcji:
Losuje czy broń trafi (Hit) czy nie (Miss).
Symuluj 5 ataków każdą bronią i zapisz wyniki w liście.
Zlicz ile było trafień i pudł dla każdej broni (np. używając Counter).

Dodatkowo oblicz procent trafień dla każdej broni i wypisz w czytelnej formie, np.:
Broń A: 6 trafień, 4 pudła, 60%
Broń B: 8 trafień, 2 pudła, 80%
Broń C: 5 trafień, 5 pudła, 50%
Wylosuj  pojedyńczą broń z której został oddany strzal i wypisz wynik tego strzału."""

import random
from collections import Counter

def weapon_hit(chance):
    hit_chance = random.uniform(0, 100)
    if hit_chance <= chance:
        return "Hit" 
    else:
        return "Miss"
    
def damage(hit_damage):
    min_damage, max_damage = hit_damage
    return random.randint(min_damage, max_damage)
  
weapons = {
    "Weapon Bow": (30, 60),
    "Weapon Sword": (25, 75),
    "Weapon Degger": (20, 50)
}



chosen_weapons = random.choice(list(weapons.keys()))
max_damage = (weapons[chosen_weapons])
dmg = damage(max_damage)


"""for weapons, chance in weapons.items():
    attacks = 0
    results = []


    while attacks < 5:
        attacks = attacks + 1
        results.append(weapon_hit(chance))
    
    count_results = Counter(results)
    hits = count_results['Hit']
    misses = count_results['Miss']
    hit_percentage = (hits / 5) * 100"""


   

print(f"The chosen weapon is '{chosen_weapons}' and the result of the shot is {dmg}.")