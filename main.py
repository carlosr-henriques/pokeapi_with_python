from ability import get_ability
from pokemon import get_all_pokemon
from IPython.display import display
from pandas import set_option
set_option('display.max_rows', 1300)

def main():
    print("What do you want?", "1 - List all pokemons", "2 - List a pokemon's abilities")
    response = input("Digit: ")
    if response == '1':
        df = get_all_pokemon()
        display(df['name'])
    else:
        pokemon = input("Please inform the pokemon you want know the abilities: ")
        get_ability(pokemon=pokemon)

if __name__ == '__main__':
    main()
