from flask import Flask, request
from appiontment_handler import process_appiontment

app=Flask(__name__)

@app.route("/appiontment", methods=["POST"])
def handle_webhook():
    data=request.json
    process_appiontment(data)
    print(f"Recieved:{data}")
    return "OK", 200

if __name__== "__main__":
 app.run(port=5000)