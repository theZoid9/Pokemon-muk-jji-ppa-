import random
import pokemon_data




def pokemon_names():
     print(pokemon_data.pokemon_names)
     return pokemon_data.pokemon_names


def pokemon_weakness():
    print(pokemon_data.type_weaknesses)
    return pokemon_data.type_weaknesses


def bot_choice():
    poke_list = pokemon_names().values()
    bot = random.choice(poke_list)
    print(bot)
    return 


def player_choice():
    pass


def main():
    pass



bot_choice()

    
    
    