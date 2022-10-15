import requests

baseURL = "https://api.nal.usda.gov/fdc/v1"
foodURL = baseURL+"/foods"

API_KEY="vGX5hsJJobITEeTOWfP3HbAh5FqBwif8m8NeQN5H"

def getFoodsByName(name):
    response = requests.get(foodURL+"/search", params={
        "api_key": API_KEY,
        "query": "apples"
    })
    foods = response.json()["foods"]
