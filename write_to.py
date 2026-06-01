from Auth_Api import fetch_data, url
import json
from datetime import datetime

data=fetch_data(url)

if data is None:
    print("failed to fetch data, check my API key")
else:    

    weather_Record ={
                "city": data['name'],
                "temperature":data['main']['temp'],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "weather": data["weather"][0]["description"],
                "recorded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open("weather_log.json", "a") as f:
        json.dump(weather_Record, f)
        f.write("\n")

    print("File saved succesfully")
    print(weather_Record)
