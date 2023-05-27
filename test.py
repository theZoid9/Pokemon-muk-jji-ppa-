import random
import time
from pokemon_data import pokemon_names
from pokemon_data import pokemon_n_only
from pokemon_data import pokemon_moves



    
for pokemon in pokemon_moves:
        
        moves = pokemon_moves[pokemon]
        print("Moves for", pokemon, ":")
        for move in moves:
            print(move)
        print()
            