import requests
from bs4 import BeautifulSoup

r1 = requests.get(
    url='https://github.com/login'
)
soup1 = BeautifulSoup(r1.text, 'lxml')
token_tag = soup1.find(name='input',attrs={'name':'authenticity_token'})
authenticity_token = token_tag.get('value')
r1_cookies = r1.cookies.get_dict()
r1.close()


form_data={
    'commit':'Sign in',
    'utf8':'',
    'authenticity_token':authenticity_token,
    'login':'academxxxxx',
    'password':'ymxxx0'
}
r2 = requests.post(
    url='https://github.com/session',
    data=form_data,
    cookies=r1_cookies,
)
r2_cookies = r2.cookies.get_dict()
r1_cookies.update(r2_cookies)

r3 = requests.get(
    url='https://github.com/settings/repositories',
    cookies=r1_cookies
)

soup3 = BeautifulSoup(r3.text, 'lxml')
print('soup3-->',soup3)
list_group = soup3.find(name='div', class_='listgroup')

from bs4.element import Tag
for item_chil in list_group.children:
    if isinstance(item_chil,Tag):
        project_tag = item_chil.find(name='a', class_='mr-1')
        size_tag = item_chil.find(name='small')
        temp = "项目:%s(%s); 项目路径:%s" % (project_tag.get('href'),size_tag.string,project_tag.string)
        print(temp)




