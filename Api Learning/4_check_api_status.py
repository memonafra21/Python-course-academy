import requests

# API URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Send GET request
response = requests.get(url)

# Check status code
if response.status_code == 200:
    data = response.json()  # Convert to JSON
    print(data)  # Print the data
else:
    print("Failed to fetch data from API")
