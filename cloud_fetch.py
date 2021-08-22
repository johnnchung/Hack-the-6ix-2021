import json
import requests

import os
from dotenv import load_dotenv

load_dotenv()


def cloud_response(links):
    try:
        ENDPOINT = os.getenv('ENDPOINT')
        
        payload = {"features": links} 
        
        ml_response = requests.post(ENDPOINT, json=payload)

        phishing_result = json.loads(ml_response.text)
        
        return phishing_result["response"]
    except:
        return None
