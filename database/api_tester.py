import requests
import json


def test_get():
    url = 'http://127.0.0.1:5000/get-csrf-token'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        access_token = data['csrf_token']
    else:
        print(f"Failed to retrieve csrf token. Status code: {response.status_code}")
        return

    url = 'http://127.0.0.1:5000/thesaurus/get_words'

    response = requests.get(url,
                            headers={'Authorization': access_token})

    if response.status_code == 200:
        data = response.json()  # Get the JSON data from the response
        print()
        for items in data:
            print(items) # print the data
            print()
        print("Number of Words:", len(data))
    else:
        print(f"Failed to retrieve words endpoint. Status code: {response.status_code}")
    
def test_insert():
    url = 'http://127.0.0.1:5000/create'
    data = {
        'words': 
            {
                'hello': {
                    'definition': 'Noun. A salutation that is said when meeting someone.',
                    'synonyms': ['greetings', 'saluations', 'hi', 'yo', 'wassup', 'cheerio', 'guten tag', 'welcome', 'beinvenue']
                }
            }
    }
    data = json.dumps(data)
    response = requests.post(url, data=data, headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        print("Word inserted successfully.")
    else:
        print(f"Failed to insert word. Status code: {response.status_code}")


test_get()
