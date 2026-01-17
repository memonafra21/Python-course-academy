import requests

# API URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Send GET request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Print only the title
print("Title:", data["title"])
