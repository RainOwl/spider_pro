#_author_ : duany_000
#_date_ : 2018/2/8
from bs4 import BeautifulSoup
import requests

url = "http://www.autohome.com.cn/news/"
response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "lxml")
content_div = soup.find(name='div',id='auto-channel-lazyload-article')
# img_div = content_div.find_all(name='div',_class='article-pic')
li_list = content_div.find_all(name='li')
for li in li_list:
    a = li.find('a')
    if a:
        print(a)
        img_div = a.find(name='img')
        print(img_div.attrs.get('src'))

# print(img_div)
# print(soup)
