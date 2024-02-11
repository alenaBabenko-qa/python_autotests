import requests

URL = "https://api.pokemonbattle.me/v2"
HEADER = {"Content-Type":"application/json","trainer_token":"475585d17770d611782bf5d4bb7ef0f6"}



body = {
    "name":"Боря",
    "photo":"https://dolnikov.ru/pokemons/albums/005.png"}

response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)

print(f'Статус код: {response.status_code}. Сообщение {response.json() ["message"]}')



body = {
    "pokemon_id": "140",
    "name": "Гена",
    "photo": "https://dolnikov.ru/pokemons/albums/036.png"
}

response = requests.patch(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}.Сообщение {response.json() ["message"]}')



body = {
    "pokemon_id": "140"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}.Сообщение {response.json() ["message"]}')