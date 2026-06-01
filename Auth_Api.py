import requests
import json 
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
city="SOKOTO"




url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

def fetch_data(url):
    try:
       response=requests.get(url, timeout=10)
       response.raise_for_status()
       data=response.json()
     


     # if i want to view the whole data 
     #    print(json.dumps(data))
     #    response.status_code 


       print(f"City: {data['name']}")
       print(f"Temperature: {data['main']['temp']}C")
       print(f"Weather: {data['weather'][0]['description']}")
       print(f'Humidity: {data["main"]['humidity']}')
       print(f"wind speed: {data['wind'] ["speed"]}")
       print(f"feels like:{data["main"]['feels_like']}")
       
       return data

    except requests.exceptions.ConnectionError:
        print("No internert Error")
    except requests.exceptions.Timeout:
        print("request timeout")    
    except Exception as e:
        print(f"Something went wrong : {e}")  
        return None    
    
fetch_data(url)  


