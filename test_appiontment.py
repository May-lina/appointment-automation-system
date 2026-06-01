import requests

data={
    "patient_name": "amina",
    "appiontment":"2026-04-19",
    "doctor": "Abdullahi Bala",
    "Hospital":"Noma hospital"
}

response=requests.post("http://127.0.0.1:5000/appiontment", json=data)
print(response.status_code)
print(response.text)