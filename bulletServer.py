import requests
import wget
import time
import shutil

r = requests.get('http://10.42.0.102:8000/start')
print 'bulletCam started...'
print''
time.sleep(4)

r = requests.get('http://10.42.0.102:8000/stop')
print 'bulletCam stopped...'


url = 'http://10.42.0.102:8000/get/10'
response = requests.get(url, stream=True)
print 'trying to get image'
with open('10.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response
