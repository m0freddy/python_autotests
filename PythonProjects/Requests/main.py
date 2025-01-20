import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cc3d5a41bd6641ccd14075ce46013843'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_1 = {
    "name": "generate",
    "photo_id": -1
}

response_1 = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_1)
print(response_1.json())

POKEMON_ID = response_1.json()['id']

body_2 = {
    "pokemon_id": POKEMON_ID,
    "name": "Morty",
    "photo_id": -1
}

response_2 = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_2)
print(response_2.json())

body_3 = {
    "pokemon_id": POKEMON_ID
}

response_3 = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_3)
print(response_3.json())