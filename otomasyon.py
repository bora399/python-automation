from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import requests

driver = webdriver.Chrome("C:\Program Files (x86)\Chrome Driver\chromedriver.exe")
driver.get("https://onurdayibasi.com/react-ui-mechanics/?")
r = requests.get("https://onurdayibasi.com/react-ui-mechanics/?")
time.sleep(4)
hrefList = []
kodList = []
soup = bs(r.content,"lxml")
columnDiv = soup.find_all("a",attrs={"rel":"noopener noreferrer"})
del columnDiv[0:4]
print(columnDiv)
for i in columnDiv:
    hrefList.append(i.get("href"))
for i in hrefList:
    i = i[::-1]
    i = i[0:12]
    i = i[::-1]
    kodList.append(i)
kodList.append("56abdafa64")
print(kodList)

for i in kodList:
    driver.get("https://onurdayibasi.com/react-ui-mechanics/?"+i)
    time.sleep(1)
    driver.execute_script("window.history.go(-1)")        

# column 1 xpath : /html/body/div/div/div/main/div/div[1]/

