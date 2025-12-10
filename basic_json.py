import requests

endpoint = "https://httpbun.com/anything"
endpoints = "https://httpbun.com/headers"

response = requests.get(endpoint, json={"gabe" : 'kaiel'})

print(response.json())
