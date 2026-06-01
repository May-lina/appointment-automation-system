import requests
import json
from datetime import  datetime


fetch_url="https://jsonplaceholder.typicode.com/posts/1"
send_url="https://jsonplaceholder.typicode.com/posts"

def fetch_from_system_b(url):
    try:
        response=requests.get(url, timeout=10)
        response.raise_for_status()
        data=response.json()
        return data
    except requests.exceptions.ConnectionError:
        print("No internet connection")
    except requests.exceptions.Timeout:
        print('request timed-out')    
    except Exception as e:
        print(f'something went wrong: {e}')
        return None
payload={"title": "test", "user_id":1, "body":"something weird"}    
def send_to_system_b(url):    
    try:
        response=requests.post(
            url,
            json=payload,
            timeout=10
        )
        print(response.status_code)
        print(response.json())
        return response.json()
    except requests.exceptions.ConnectionError:
        print("No ineternet connection")
    except Exception as e:
        print(f"somethimg went wrong:{e}")
        return None

def log_data(data,result):
    record={
       'data_processed':data,
       'send_to_system_b':result,
       'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    with open("automation_log.json", "a") as f:
        json.dump(record, f)
        f.write("\n")

        print("logged successfully!")

def run_automation(fetch_url, send_url):

    data=fetch_from_system_b(fetch_url)

    if data is None:
        print("couldn't fetch, stop automating")   
        return
    
    result=send_to_system_b(send_url)

    if result is None:
        print("send failed")  
        return
    
    log_data(data, result)

run_automation(fetch_url, send_url)       


        

        
    

