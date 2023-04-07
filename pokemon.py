import requests
import pandas as pd
import time

def get_all_pokemon(url="https://pokeapi.co/api/v2/pokemon", df=None):
    if df is None or df.empty:
        df = pd.DataFrame([])
    else:
        pass
    
    response = requests.get(url)
    data = response.json()    
    df = pd.concat([df, pd.json_normalize(data['results'])], ignore_index=True)
    
    if data['next']:
        time.sleep(1)
        return get_all_pokemon(data['next'], df)
    
    return df
if __name__ == '__main__':

    url = "https://pokeapi.co/api/v2/pokemon"
    df_pokemons = get_all_pokemon(url)