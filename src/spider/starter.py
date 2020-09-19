import requests
from bs4 import BeautifulSoup
import lxml

url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
print(strhtml.text)
soup = BeautifulSoup(strhtml,',lxml')
data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
print(data)