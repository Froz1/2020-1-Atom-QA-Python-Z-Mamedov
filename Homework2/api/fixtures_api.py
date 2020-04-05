import pytest
from random import randint

from api.client import ApiClient


@pytest.fixture(scope='function')
def api_client():
    email = 'test_atom1@mail.ru'
    password = '12ab..'
    
    return ApiClient(email, password)
    
@pytest.fixture(scope='function')
def authorization():
    return ('test_atom1@mail.ru', '12ab..')
    
@pytest.fixture(scope='function')
def new_data():
    data_1 = randint(100, 100000)
    data = {
        'name': f'test_name {data_1}',
        'pass_condition': 1,
        'relations': [
            {'object_type': "remarketing_player", 'params': {"type": "positive", "left": 365, "right": 0}}
        ],
        'logicType': "or"
    }
    return data
  