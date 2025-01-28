import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "1337 School",
    "price": 342,
}

post_response = requests.post(endpoint, json=data)
print(post_response.json())