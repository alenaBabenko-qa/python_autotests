import requests
import pytest

URL = "https://api.pokemonbattle.me/v2"
HEADER = {"Content-Type":"application/json","trainer_token":"475585d17770d611782bf5d4bb7ef0f6"}

def test_get_trainers():

    '''
    KTI-1. Get trainers by code
    '''

    response = requests.get(url=f'{URL}/trainers', headers=HEADER, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

    
def test_get_trainers_name():
    response = requests.get(url=f'{URL}/trainers', params = {"trainer_id":132}, headers=HEADER)
    assert response.json()['data'][0]["trainer_name"] == "Максим"