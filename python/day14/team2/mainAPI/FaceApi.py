import os
import sys
import requests
client_id = "fp9y6twxi9"
client_secret = "rooJa994NhlBUmwtRsWU3zEjeqMfrLYkJ7EQXBOY"
url = "https://naveropenapi.apigw.ntruss.com/vision/v1/celebrity" # 유명인 얼굴인식
files = {'image': open('seo.jpg', 'rb')}
headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print("Error Code:" + rescode)