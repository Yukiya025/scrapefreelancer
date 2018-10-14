# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import csv
import re
import warnings
warnings.filterwarnings('ignore')

r = requests.get("https://www.freelancer.com/archives/python/2018-40/")
soup_content = BeautifulSoup(r.content, "html.parser")
f1 = open('r.txt', 'w')
f1.write(r.text)
f1.close

soup = BeautifulSoup(r.text)
std_lnk = "https://www.freelancer.com"
with open('pythonHref.csv', 'w+',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    for link in soup.find_all('a', {'href': re.compile(r'^/projects/python/')}):
        title = link.get_text()
        writer.writerow([title, std_lnk + link.get('href')])


