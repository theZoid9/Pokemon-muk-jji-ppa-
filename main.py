import random
import time
from pokemon_data import pokemon_names
from pokemon_data import pokemon_n_only


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
                
        


def player_pokemon_type():
    pass


def bot_pokemon_type():
    pass



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
    
    
    
main()