from request_ability import get_ability

def main():
    pokemon = input("Please inform the pokemon you want know the abilities: ")
    get_ability(pokemon=pokemon)

if __name__ == '__main__':
    main()