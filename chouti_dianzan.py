#_author_ : duany_000
#_date_ : 2018/2/9
import requests

headers1={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64)'
                 ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Content-Type':'text/html; charset=UTF-8',
}
url1 = "http://dig.chouti.com/help/service"
r1 = requests.get(url=url1,
                  headers=headers1
                  )
r1_cookie = r1.cookies.get_dict()
print('r1_cookie-->',r1_cookie)

form_data = {
    'phone':'861821069xxxx',
    'password':'ymj123456',
    'oneMonth':'1',
}
headers2={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64)'
                 ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer':'http://dig.chouti.com/',
}
r2 = requests.post(
    url="http://dig.chouti.com/login",
    data=form_data,
    cookies = r1_cookie,
    headers=headers2,
)
print(r2.text)

headers3={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64)'
                 ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Content-Type':'text/plain; charset=utf-8',
    'Referer':'http://dig.chouti.com/',
}
r3 = requests.post(
    url="http://dig.chouti.com/link/vote?linksId=17370086",
    cookies = r1_cookie,
    headers=headers3,
)
print(r3.text)





