"""
Francesco Gerratana 2020, www.nextechnics.com
Simple example web scrape with python and BeautifulSoup,
to see in action the method requests.get,rsplit,os.path.isfile ,urlretrieve etc...
Run before pip install to install the necessary packages
"""

from bs4 import BeautifulSoup
import urllib.request
import requests
import os
import re

'Remove illegal char windows'
def cleanpath(dpath):
    invalid = '<>:"/\|?*'
    for char in invalid:
        dpath = dpath.replace(char, ' ')
    return dpath


url = "http://www.coverbrowser.com/covers/dreamcast-games"
ext = "jpg"
dest = os.path.join(os.getcwd(),"img")
if not os.path.exists(dest):
    os.makedirs(dest)

page = requests.get(url).text
soup = BeautifulSoup(page, "html.parser")

data = soup.find_all("p",class_="cover")


for a in data:
    z = a.find_all("img")[0].get("src")
    n = a.find_all("img")[0].get("alt")
    
    files = cleanpath(n)+os.path.splitext(z)[1]
    imgx = dest+"\\"+files.replace("Dreamcast Games -", "")
    urllib.request.urlretrieve('http://www.coverbrowser.com'+z,imgx)
