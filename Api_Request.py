import requests

response=requests.get("https://jsonplaceholder.typicode.com/posts")
data=response.json()
print(data)
# print(data["title"])
# print(data["id"])
# print(data["body"])
# print(response.status_code)

print(type(data))
print(len(data))
print(data[0])
print(data[0]["title"])

for post in data[:5]:
    print(post["title"])