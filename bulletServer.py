import requests
import wget
import time
import shutil



for counter in range(42):
	r = requests.get('http://10.42.0.' + str(counter + 100) + ':8000/start')
	print 'bulletCam started...' + str(counter)


time.sleep(4)


for counter in range(42):
	r = requests.get('http://10.42.0.' + str(counter + 100) + ':8000/stop')
	print 'bulletCam stopped...' + str(counter)

for counter in range(42):
	r = requests.get('http://10.42.0.' + str(counter + 100) + ':8000/get/' + str(counter))
	response = requests.get(url, stream=True)
	print 'trying to get image' 
	fileName = 'picture_' + str(counter) + '.png'
	with open(fileName, 'wb') as out_file:
	    shutil.copyfileobj(response.raw, out_file)
	del response
