import cv2
import datetime
import os
import sys
import requests
import urllib.request
from PIL import Image, ImageDraw
import json

video_capture = cv2.VideoCapture(0)
file = "";
while (True):

    grabbed, frame = video_capture.read()
    cv2.imshow('Original Video', frame)

    key = cv2.waitKey(1);
    if key == ord('q'):
        break
    elif key == ord('s'):
        file = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f") + '.jpg'
        cv2.imwrite(file, frame)
        print(file, ' saved')

video_capture.release()
cv2.destroyAllWindows()


client_id = "fp9y6twxi9"
client_secret = "rooJa994NhlBUmwtRsWU3zEjeqMfrLYkJ7EQXBOY"
url = "https://naveropenapi.apigw.ntruss.com/vision/v1/celebrity"
#files = {'image': open(file, 'rb')}
# file = 'KakaoTalk_20210206_135942828.jpg'
files = {'image': open(file, 'rb')}
headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
#    print("Error Code:" + rescode)
    print("에러")
image = Image.open(file)    
image.show()    

json_data = json.loads(response.text)
gender, gen_confidence = json_data['faces'][0]['celebrity'].values() # 성별

result = """
결과: %s (%s)

""" % (
    gender, gen_confidence,
)
print(result)