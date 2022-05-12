import pytest # Pytest is a good tool to test your application
import json

from app import app # Import your API

@pytest.fixture # Fixtures are reusable mocked object in Python
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client # Return an in memory API for launching the test

def test_hello_world(client): # Instanciate the API in memory
    res = client.get('/hello_world') # Send a GET request on the route /hello_world
    assert b'Hello World!' == res.data # Verify that the result is correct

# def test_prediction(client):
#     res = client.get('/spacy/prediction/We%20study%20at%20ENSAE%20Paristech%20in%20Paris') # Send a GET request on the route /spacy/prediction/<text>
#     data = json.loads(res.data) # Convert binary result res.data to Dict
#     assert data == {'ENSAE Paristech': 'FAC', 'Paris': 'GPE'}

# def test_prediction_json(client):
#     res = client.post('/spacy/prediction',
#                       json={'text': "When Sebastian Thrun started working on self-driving cars \
#                           at Google in 2007, few people outside of the company took him seriously. \
#                               I can tell you very senior CEOs of major American car companies would \
#                                   shake my hand and turn away because I wasn’t worth talking to, said \
#                                       Thrun, in an interview with Recode earlier this week.)"}) 
#                                       # Send a POST request on the route /spacy/prediction
#     data = json.loads(res.data) # Convert binary result res.data to Dict

#     expected_result = {
#         '2007': 'DATE',
#         'American': 'NORP',
#         'Recode': 'ORG',
#         'Sebastian Thrun': 'PERSON',
#         'earlier this week': 'DATE',
#     }

#     assert data == expected_result
