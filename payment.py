import requests
import hashlib
import json
API_ID = '****'
API_KEY = '****'
project_id = '****'
sign = hashlib.sha256(f'balance{API_ID}{API_KEY}'.encode())
responce = requests.get(f"https://anypay.io/api/payments/{API_ID}", params={
    "sign":sign.hexdigest(),
    "project_id": project_id,
})
143145141414141