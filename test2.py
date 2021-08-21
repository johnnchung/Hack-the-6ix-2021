from flask import Flask, render_template, request
import json
import sys
import requests
import browserurl 

url = ["www.google.ca", "www.youtube.ca"] 
payload = {"features": url} 
        
model_endpoint = 'https://us-east1-turnkey-brook-323601.cloudfunctions.net/phishing-predictions'
response = requests.post(model_endpoint, json=payload)

links = response.text
print (response.text)


# for a in links:
        
#     print(links)