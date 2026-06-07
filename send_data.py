import requests

payload={
    "title": "My first post",
    "body" : "This is the conetent",
    "userId" : "1"
}
try:

   response=requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload, 
    timeout=10
     )

   print(response.status_code)
   print(response.json())
except requests.exceptions.ConnectionError:
   print("No internet connection")
except requests.exceptions.Timeout:
  print("request timed out")   
   