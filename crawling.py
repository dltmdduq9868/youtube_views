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
import csv
from time import localtime, strftime
import pandas as pd



# Selenium doc url : https://selenium-python.readthedocs.io/locating-elements.html
extract_date = strftime("%Y/%m/%d %H:%M:%S", localtime())
print("수집시간 : ",extract_date)

#수집 대상 url
driver = webdriver.Chrome('C:/chromedriver.exe')
driver.implicitly_wait(3)
# driver.get('https://www.youtube.com/channel/UCbBYCeXeSyZ3-38DXs3LPQQ/videos')
driver.get('https://www.youtube.com')

#로그인 버튼 클릭
driver.find_element_by_xpath("//yt-formatted-string[@class='style-scope ytd-button-renderer style-suggestive size-small']").click()
driver.find_element_by_id('identifierId').send_keys('sylee@gaion.kr')
driver.find_element_by_id('identifierNext').click()
# driver.find_element_by_xpath("//yt-formatted-string[@id='password']/div[1]/div/div[1]/input]").send_keys('duq458658')
# //*[@id="password"]/div[1]/div/div[1]/input
driver.find_element_by_name('password').send_keys('duq458658')
# driver.find_element_by_id('passwordNext').click()
#비밀번호 입력 후 다음 버튼 클릭
# Enter Key 입력 방법 : https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys
driver.find_element_by_xpath("//div[@class='U26fgb O0WRkf zZhnYe e3Duub C0oVfc nDKKZc DL0QTb']").send_keys(u'\ue007')

# //*[@id="items"]/ytd-mini-guide-entry-renderer[3]
# driver.find_element_by_xpath("//ytd-guide-entry-renderer[@id='items']/ytd-mini-guide-entry-renderer[3]").click()
# //*[@id="items"]/ytd-guide-entry-renderer[1]
#첫번째 추천 동영상 유투버  style-scope ytd-channel-name complex-string
driver.find_element_by_xpath("//yt-formatted-string[@class='style-scope ytd-channel-name complex-string']").click()
#동영상 탭 클릭
driver.find_element_by_xpath("//*[@id='tabsContent']/paper-tab[2]").click()
#크롤링 대상 url
print(driver.current_url)
driver.get(driver.current_url)

# "//form[@id='loginForm']"
#스크롤 5회 이동
endk = 5
while endk:
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(0.3)
    endk -= 1

page = driver.page_source;
print(page)

#html 테그
soup = BeautifulSoup(page, "html.parser")
all_views = soup.find_all('span','style-scope ytd-grid-video-renderer')
views = [soup.find_all('span','style-scope ytd-grid-video-renderer')[n].string for n in range(0,len(all_views))]
print("views :" ,views)

#리스트에 조회수 저장
views_list = []

x = 0 #조회수의 index 초기화
i = 0

for i in range(0, len(views)):
    if i % 2 == 0:#['조회수' : '날짜'] 중 조회수만 리스트에 저장하기 위한 조건
        views_list.append(views[i])
    # i += 2  # 조회수만 append

# print(views_list[0])
# print(views_list[1])
# print(views_list[2])
########################################################################################################################
#
# data = pd.DataFrame(extract_date)
# # print(data.head(5))
# data.to_csv("C:/Users/USER/PycharmProjects/Crawling/youtube_views.csv", encoding = 'cp949')

data = pd.DataFrame(views_list)
# print(data.head(5))
data.to_csv("C:/Users/USER/PycharmProjects/Crawling/youtube_views.csv", encoding = 'cp949')

# csvfile = open("C:/Users/USER/PycharmProjects/Crawling/YouTube_views.csv","w",newline="")
# csvwriter = csv.writer(csvfile)
# for row in views_list:
#     csvwriter.writerow(row)
# csvfile.close()

del(views_list)#리스트 초기화



