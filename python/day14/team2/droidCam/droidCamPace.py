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
url = "https://naveropenapi.apigw.ntruss.com/vision/v1/face"
print(file)
files = {'image': open(file, 'rb')}
headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
#    print("Error Code:" + rescode)
    print("에러")
    
json_data = json.loads(response.text)
x, y, w, h = json_data['faces'][0]['roi'].values()

target_image = Image.open(file)
draw = ImageDraw.Draw(target_image)
draw.rectangle(((x,y), (x+w,y+h)), outline="red")
target_image.show()    


gender, gen_confidence = json_data['faces'][0]['gender'].values() # 성별
age, age_confidence = json_data['faces'][0]['age'].values() # 나이
emotion, emotion_confidence = json_data['faces'][0]['emotion'].values() # 감정
pose, pose_confidence = json_data['faces'][0]['pose'].values() # 얼굴 방향

result = """
성별: %s (%s)
나이: %s (%s)
감정: %s (%s)
방향: %s (%s)
""" % (
    gender, gen_confidence,
    age, age_confidence,
    emotion, emotion_confidence,
    pose, pose_confidence
)
print(result)