import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/52')
response_users = requests.get('https://jsonplaceholder.typicode.com/users/1')
data = response.json()
data_users = response_users.json()

print(data['title'])
print(data_users['name'])
print(data['body'])