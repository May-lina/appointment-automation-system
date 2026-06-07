import requests
import json
from datetime import datetime 


def fetch_patient_details(patient_name):  #but my url has no patient details?
    url="https://jsonplaceholder.typicode.com/users/1"        
    try:
        response=requests.get(url, timeout=10)
        response.raise_for_status
        data=response.json()
        return data
    except requests.exceptions.ConnectionError:
        print("No internet connection")
    except requests.exceptions.Timeout:
        print("Request timed-out")
    except Exception as e:
        print(f"something went werong : {e}")      
        return None

def send_to_doctor_system(appiontment,patient): 
    url="https://jsonplaceholder.typicode.com/users"  
    payload={
        "patient":patient,
        "appiontment":appiontment
    }
    try:
        response=requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"something went wrong:{e}")

def log_appiontment(appiontment, patient, result):
    record={
        "appiontment":appiontment,
        "patient":patient,
        "sent_to_doctor":result,
        "timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     }
          
    with open("appiontment.json", "a") as f:
        json.dump(record, f)
        f.write("\n")  
    print("appiontment logged successfully")    

def process_appiontment(appiontment):
    print(f"processing appiontment:{appiontment['patient_name']}")

    patient=fetch_patient_details(appiontment['patient_name'])
    if patient is None:
        print("could not fetch patient's details")
        return
    result=send_to_doctor_system(appiontment,patient)
    if result is None:
        print("Could not send to doctor's system")
        return
    log_appiontment(appiontment,patient,result)
    print(f"appiontment process successful")
    
  




