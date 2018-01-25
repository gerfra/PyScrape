"""
Francesco Gerratana 2018, www.nextechnics.com
Simple example web scrape with python and BeautifulSoup,
to see in action the method requests.get,rsplit,os.path.isfile ,urlretrieve etc...
Run before pip install to install the necessary packages
"""

from bs4 import BeautifulSoup
import requests
from urllib import urlretrieve
import os

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
    print "Url: http://www.coverbrowser.com"+z+"\n path: "+z.rsplit("/",1)[0]+"\n Name file: "+z.rsplit("/",1)[1]
    files = os.path.join(dest,z.rsplit("/",1)[1])
    if os.path.isfile(files):
        print "---Warning File exists!!!"
    else:
        print "Write file to: "+files
    urlretrieve('http://www.coverbrowser.com'+z,files)

                                              
                                              
    
  
