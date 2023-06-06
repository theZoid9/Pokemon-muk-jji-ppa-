import random
import time
from pokemon_data import pokemon_names
from pokemon_data import pokemon_n_only
from pokemon_data import pokemon_moves

def bot_pokemon_choice():
    
    pokemon_list = list(pokemon_names.values())
    pokemon_list = random.choice(pokemon_list)
    bot = random.choice(pokemon_list)
    return bot
    

def player_pokemon_choice():
    
    player_input = input("choose Your Pokemon! \n")
    for values in pokemon_names.values():
        for x in values:
            if x == player_input:
                return player_input
                
        


def player_pokemon_type(player_pokemon):
    

     for key, val in pokemon_names.items():
         if player_pokemon in val:
             print(f"Pokemon Type: {key}")
             return key



def bot_pokemon_type():
    pass


def pokemon_move():
    
    pk_move = player_pokemon_choice()
    print("hey")
    
    for pokemon in pokemon_moves:
        moves = pokemon_moves[pokemon]
        if pk_move == pokemon:
            print(moves)
            return moves
            
            
            
            
 



def countdown():
    
     print("waiting for trainer...")
     time.sleep(1)
     print("waiting for trainer...")
     time.sleep(1)
     print("waiting for trainer...") 
     time.sleep(1)
     print("\n")
 




def main():
    
    print(tuple(pokemon_n_only))
    player_pokemon = player_pokemon_choice()
    time.sleep(3)
    print(f"lets Go !! {player_pokemon}! \n")
    countdown()
    bot_player = bot_pokemon_choice()
    time.sleep(3)
    print(f"Trainer player: I choose {bot_player} ..lets Fight!!\n")
    time.sleep(5)
    print(f"{player_pokemon} vs {bot_player}\n")
    player_pokemon_type(player_pokemon)
    

main()

