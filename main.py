import random
from pokemon_data import pokemon_names



def bot_choice():
    pass



def player_choice():
    player_input = input("chooseYour Pokemon!")
    for values in pokemon_names.values():
        for x in values:
            if x == player_input:
                     print(f"You choose{player_input}!!!")
        



def main():
     pass



    
player_choice()    
    
    