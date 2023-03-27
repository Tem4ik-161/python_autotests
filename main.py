import requests

token =  '86de45ed52510a22abfc031448d11230'

response_pokemons = requests.post('https://pokemonbattle.me:9104/pokemons',
              headers = {'Content-Type': 'application/json',
                         'trainer_token':token}, 
              json = {
    "name": "Google",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
})

print(response_pokemons.text)

response_edit_name = requests.put ('https://pokemonbattle.me:9104/pokemons',
              headers = {'Content-Type': 'application/json',
                         'trainer_token':token},
                         json = {
    "pokemon_id": "7764",
    "name": "Google2",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
})

print(response_edit_name.text)

response_add_pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball',
              headers = {'Content-Type': 'application/json',
                         'trainer_token':token},
                         json = {
    "pokemon_id": "7764"
})

print(response_add_pokeball.text)