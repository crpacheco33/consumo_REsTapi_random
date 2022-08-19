from flask import Flask
import random
import requests

app = Flask(__name__)

@app.route("/")
def random_number():
    a= str(random.randrange(100))
    data= {'n' : a}
    #r = requests.get("http://127.0.0.1:5000/get", params = data)
    r = requests.get("http://127.0.0.1:5000/fibonacci/get", params = data)
    return r.text