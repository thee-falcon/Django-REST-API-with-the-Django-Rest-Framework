import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello World!"})
print(get_response.json())

post_response = requests.post(endpoint, params={"abc": 123}, json={"title": None})
print(post_response.json())

# print (get_response.text)
# print(get_response.status_code)