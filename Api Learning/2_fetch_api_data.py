import requests

# API URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Send GET request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Print required fields
print("ID:", data["id"])
print("Title:", data["title"])
print("Body:", data["body"])
