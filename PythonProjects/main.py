import requests

token = '4deb1a4178648d0657f58a758e6d9850'

'''response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json = {
    "trainer_token": token,
     "email": "ytd2u@greencafe24.com",
    "password": "Krygerok91"
}, headers= {'Content-Type':'application/json'})'''



'''response_activation = requests.post('https://api.pokemonbattle.me:9104/trainers/confirm_email', json = {
    "trainer_token": token
})'''


'''response_add_pokemon = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "trainer_token": token,
    "name": "dimasikmolodec"
}, headers= {'Content-Type':'application/json', 'trainer_token': token})

print(response_add_pokemon.text)''' 

'''response_pokemon_rename = requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": "5832",
    "name": "dimasiksnovamolodec"
    
}, headers= {'Content-Type':'application/json', 'trainer_token': token})

print(response_pokemon_rename.text)
'''
"""
response_addpokeball = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = {
    "pokemon_id": "5832"
}, headers = {'Content-Type':'application/json', 'trainer_token': token} ) 

print(response_addpokeball.text)"""