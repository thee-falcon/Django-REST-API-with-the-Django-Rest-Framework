import requests

endpoint = "http://localhost:8000/api/products/1"

get_response = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello World!"})
print(get_response.json())
