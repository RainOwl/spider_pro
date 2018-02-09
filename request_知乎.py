from bs4 import BeautifulSoup
import requests, time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
           'Referer':'https://www.zhihu.com/',
           'Host':'www.zhihu.com'
           }
session = requests.session()
url_xsrf = session.get('https://www.zhihu.com',headers=headers)
html_xsrf = BeautifulSoup(url_xsrf.content,'lxml')
# print('html_xsrf-->',html_xsrf)
xsrf = html_xsrf.find('input')
print('xsrf-->',xsrf)

captcha_url = 'https://www.zhihu.com/captcha.gif?r='+str(int(time.time()*1000))+'&type=login&lang=en'
req_captcha = session.get(captcha_url,headers=headers)
with open('../captcha.gif','wb') as f:
    f.write(req_captcha.content)

captcha = input('please input captcha>>>')

data = {'phone_num':'xxxxx',
       'password': 'xxxxx',
        'captcha_type':'en',
        'captcha':captcha,
        '_xsrf':xsrf
       }

req = session.post('https://www.zhihu.com/login/phone_num',headers=headers,data=data)
print(req.json()['msg'])

i4 = session.get(
    url='https://www.zhihu.com/settings/profile',
    headers=headers
)

soup4 = BeautifulSoup(i4.text, 'lxml')
tag = soup4.find(id='rename-section')
nick_name = tag.find('span',class_='name').string
print(nick_name)