from flask import Flask, render_template, request
import json
import sys
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__) 

load_dotenv()

ENDPOINT = os.getenv('ENDPOINT')
# reference current file as an instance of the class

@app.route('/', methods=['GET', 'POST']) # endpoint
def get_model_request(): 
    
    url = ["www.google.ca", "www.youtube.ca"] 
    payload = {"features": url} 
        
    model_endpoint = ENDPOINT
    response = requests.post(model_endpoint, json=payload)
    return response.text


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=105, debug = True)

# def get_arg(name: str, default: str = ""):
#     json_obj = request.get_json(silent=True)
#     if json_obj is not None and name in json_obj: return json_obj[name]
#     return request.values[name] if name in request.values else default



# # Receive response from GCP 
# @app.route('/', methods=['GET'])
# # GET https://ml.googleapis.com/v1/{name=projects/*}:getConfig
# def check_phising():


# "0", "1" represent phising/safe 


# Duck Mover
