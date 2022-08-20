import requests
import fake_useragent
from bs4 import BeautifulSoup
from tqdm import tqdm
import time


page = ("https://ru.hitmotop.com/search?q=")
a = str(input("Введите название песни: "))

responce = requests.get(page+a).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', class_ = 'track__info')
#print(block)
sound = block.find_all('div', class_= 'track__info-r')
for image in sound:
    music_link = image.find('a').get('href')
    print(music_link)

    music_bytes = requests.get(music_link).content


with open(f'music.mp3', 'wb') as file:
    file.write(music_bytes)
    for i in tqdm(music_bytes):
       pass
    print("Песня загружена")