import json
import requests
url = 'https://k8s-dash-nonprod-ctc.***.com//service1/response'
 
r = requests.get(url)
if r.status_code == 500:    
    print(r.json())

