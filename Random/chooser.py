""""
choice - zwraca losowy element
choices = zwraca listę elementów i ma większe możliwości


import random 

movie_list = [ "Title1", "Title2", "Title3", "Title4", "Title5", "Title6"]
event = ["death", "win", "lose", "gold loss", "lifeloss"]
treasure_chest = ["green", "purple", "orange", "gold", "legendary"]

from collections import Counter
print(Counter(random.choices(treasure_chest, [0.70, 0.15, 0.10, 0.04, 0.01], k = 1000)))
"""

import random

#random.shuffle() tasuje listę w miejscu – czyli zmienia kolejność elementów w liście losowo, nie tworząc nowej listy.

# Stworz liste która przechowuje karty jednego gracza i drugiego gracza tak zeby sciagało z głownej listy 

# variables 

signs = ["♠", "♥", "♦", "♣"]
card_lists = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

# Loop for 
deck = [card + sign for sign in signs for card in card_lists]

round_number = 0
while round_number <= len(deck) >= 10:
    player1 =[deck.pop() for _ in range(5)] 
    player2 = [deck.pop() for _ in range(5)]



    random.shuffle(deck)
    round_number = round_number + 1
    print(f"Runda: {round_number}")
    print(player1)
    print(player2)
    print(f"Cards is: {len(deck)}")

# Add the ask about continue
    play_again = input(f"Do you want continue? y/n: ").lower()
    if play_again != 'y':
        print("Game stopped!")
        break

print(f"Cards left: {len(deck)} -> {deck}")

"""
import random
# sample - probka

def choose_random_numbers(amount, total_amount):
    print(random.sample(range(total_amount + 1), amount))

choose_random_numbers(6,49)
"""