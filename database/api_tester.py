import requests
import json


def test_get():
    base_url = 'http://127.0.0.1:8000'
    
    auth_url = f'{base_url}/auth/get-auth-token'
    response = requests.get(auth_url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Successfully retrieved auth token:\n{data}\n")
        access_token = data['auth_token']
    else:
        print(f"❌ Failed to retrieve auth token. Status code: {response.status_code}")
        return
    
    words_url = f'{base_url}/thesaurus/get_words'
    headers = {
        'Authorization': access_token
    }
    words_response = requests.get(words_url, headers=headers)

    if words_response.status_code == 200:
        data = words_response.json()
        print(f"✅ Successfully retrieved words! Number of words: {len(data)}\n")
        for item in data:
            print(item)
            print()
    else:
        print(f"❌ Failed to retrieve words. Status code: {words_response.status_code}")
    
    # Test ML Words GET
    ml_words_url = f'{base_url}/ml/get_ml_words'
    ml_words_response = requests.get(ml_words_url, headers=headers)
    
    if ml_words_response.status_code == 200:
        data = ml_words_response.json()
        print(f"✅ Successfully retrieved ML words! Number of words: {len(data)}\n")
        print(data)
    else:
        print(f"❌ Failed to retrieve ML words. Status code: {ml_words_response.status_code}")
    
    # Test ML Inference
    ml_inference_url = f'{base_url}/ml/get_inference'
    word_guess = {
        'word1': "absolute",
        'word2': "downright"
    }
    ml_headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }
    ml_response = requests.post(ml_inference_url, json=word_guess, headers=ml_headers)
    
    if ml_response.status_code == 200:
        data = ml_response.json()
        print("✅ Successfully performed synonym inference!")
        print(data)
    else:
        print(f"❌ Failed to retrieve ml inference. Status code: {ml_response.status_code}")
    
    
    
    

# def test_insert():
#     url = 'http://127.0.0.1:5000/create'
#     data = {
#         'words': 
#             {
#                 'hello': {
#                     'definition': 'Noun. A salutation that is said when meeting someone.',
#                     'synonyms': ['greetings', 'saluations', 'hi', 'yo', 'wassup', 'cheerio', 'guten tag', 'welcome', 'beinvenue']
#                 }
#             }
#     }
#     data = json.dumps(data)
#     response = requests.post(url, data=data, headers={'Content-Type': 'application/json'})
#     if response.status_code == 200:
#         print("Word inserted successfully.")
#     else:
#         print(f"Failed to insert word. Status code: {response.status_code}")

if __name__ == "__main__":
    test_get()
