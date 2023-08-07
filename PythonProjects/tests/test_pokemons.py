import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '4deb1a4178648d0657f58a758e6d9850'

def test_status_code():
    response = requests.get( f'{host}/trainers',params={'trainer_id':1910})
    assert response.status_code == 200


def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id':1910})
    assert response.json() ['trainer_name']=='pythonius'
