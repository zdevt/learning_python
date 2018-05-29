#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import requests

from bs4 import BeautifulSoup

url = 'http://tieba.baidu.com/p/2166231880'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
img_urls = soup.findAll('img', bdwater='杉本有美吧,1280,860')

shutil.rmtree('013_pic')
os.makedirs('013_pic')

for img_url in img_urls:
    print img_url
    img_src = img_url['src']
    os.path.split(img_src)[1]
    with open('013_pic/' + os.path.split(img_src)[1], 'wb') as f:
        f.write(requests.get(img_src).content)
