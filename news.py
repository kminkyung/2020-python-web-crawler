from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B6%94%EC%84%9D"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select("#main_pack > div.news.mynews.section._prs_nws > ul > li")

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])

for article in articles:
    title = article.select_one('dt > a').text
    url = article.select_one('dt > a')['href']
    company = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사', '')
    thumbnail = article.select_one('div > a > img')['src']

    ws1.append([title, url, company, thumbnail])


driver.quit()
wb.save(filename='articles.xlsx')
