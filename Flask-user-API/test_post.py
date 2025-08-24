import requests

url = "http://localhost:5000/users"
data = {
    "name": "Mohan",
    "email": "mohan@example.com"
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())
