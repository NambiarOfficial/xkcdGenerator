import requests
from bs4 import BeautifulSoup
import random
import json

url = 'https://xkcd.com/info.0.json'
response_1 = requests.get(url)
json_file_1 = json.loads(response_1.text)
curr_num = json_file_1['num']

pic_num = random.randint(1,curr_num)
print('Fetching ' + str(pic_num))

new_url = 'https://xkcd.com/' + str(pic_num) + '/info.0.json'
response = requests.get(new_url)
json_file = json.loads(response.text)

img_url = json_file['img']
img_response = requests.get(img_url)
# print(img_url)
filename = str(pic_num) + ' - ' + json_file['title'] + img_url[-4:]

with open(filename,'wb') as f:
	for chunk in img_response:
		f.write(chunk)