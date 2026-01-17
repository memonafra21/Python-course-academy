import requests

# define endpoint
ENDPOINT = "https://jsonplaceholder.typicode.com/users/1"

# request endpoint for response

response = requests.get(ENDPOINT)

# convert into readable format

data = response.json()
print(response.status_code)
print(data["name"]) 

 