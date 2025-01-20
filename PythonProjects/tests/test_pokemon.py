import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cc3d5a41bd6641ccd14075ce46013843'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '9663'

def test_1():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200

def test_2():
    response_2 = requests.get(url=f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response_2.json()["data"][0]["trainer_name"] == 'Mfreddy'