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
    
    pokemon_list = list(pokemon_names.values())
    pokemon_list = random.choice(pokemon_list)
    player = random.choice(pokemon_list)
    return player
                

        
def player_pokemon_type(player_pokemon):

     for key, val in pokemon_names.items():
         if player_pokemon in val:
             print(f"Player Pokemon Type: {key}")
             return key


def bot_pokemon_type(bot_pokemon):
    
     for key, val in pokemon_names.items():
         if bot_pokemon in val:
             print(f"Bot Pokemon Type: {key}")
             return key


def pokemon_move(player_pokemon):
    
    
    for pokemon in pokemon_moves:
        
         moves = pokemon_moves[pokemon]
         if player_pokemon == pokemon:
             print(f"{player_pokemon} Moves: {moves}")
             return moves
             
         if player_pokemon == pokemon:
             break
                  
            
            
def countdown():
    
     print("waiting for trainer...")
     time.sleep(1)
     print("waiting for trainer...")
     time.sleep(1)
     print("waiting for trainer...") 
     time.sleep(1)
     print("\n")
 

def main():
    
    print(tuple(pokemon_n_only),"\n")
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
    bot_pokemon_type(bot_player)
    rand = pokemon_move(player_pokemon)
    rand = random.choice(rand)
    print(rand)

main()

