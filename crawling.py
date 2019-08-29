from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import time
import urllib.request #
from selenium.webdriver import Chrome
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import datetime as dt
from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://www.youtube.com/channel/UC0uDM1xZMNBAoW2xnzhAQ7g')
page = driver.page_source;
print(page)
# driver.find_element_by_name('id').send_keys('dltmdduq3862')
# driver.find_element_by_name('pw').send_keys('!lsy458658')

soup = BeautifulSoup(page, "html.parser")
all_views = soup.find_all('span','style-scope ytd-grid-video-renderer')
views = [soup.find_all('span','style-scope ytd-grid-video-renderer')[n].string for n in range(0,len(all_views))]
print(views)


try:
    html = urlopen("https://www.youtube.com/channel/UC0uDM1xZMNBAoW2xnzhAQ7g")
except HTTPError as e:
    print(e)
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.title)

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.perser")
        # nameList = bsObj.find_all("a",class_="style-scope ytd-grid-video-renderer");
        nameList = bsObj.p['class']
    except AttributeError as e:
        return None

    print(nameList[0].get_text());
