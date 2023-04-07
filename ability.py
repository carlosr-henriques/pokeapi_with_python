from requests import get

def get_ability(pokemon):
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    
    response = get(api)
    pokemon_json = response.json()

    abilities = ''

    for get_ability in pokemon_json['abilities']:
        abilities += get_ability['ability']['name'] + ', '   
    
    print(f'The abilities of {pokemon} is: {abilities[:-2]}.')
