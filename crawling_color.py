import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from nickname.models import Color


def name_color():
    # 1페이지 : https://ko.wiktionary.org/wiki/%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EC%83%89%EA%B9%94
    # 2페이지 : https://ko.wiktionary.org/w/index.php?title=%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EC%83%89%EA%B9%94&pagefrom=%EC%9E%90%EC%A3%BC#mw-pages
    req = requests.get('https://ko.wiktionary.org/w/index.php?title=%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EC%83%89%EA%B9%94&pagefrom=%EC%9E%90%EC%A3%BC#mw-pages')
    html = req.content.decode('utf-8','replace') #한글이 깨져서 넣어주었다.
    soup = BeautifulSoup(html, 'html.parser')
    #select하는데 자꾸 td별로 구분되어서 아예 젤 마지막 부분으로 분류하였더니 하나씩 구분되었다.
    color_name = soup.select('#mw-pages > div > div > div > ul > li > a')

    color_list = []
    for name in color_name:
        if (name.text.find("색") > 0):
            color_list.append(name.text.strip())
        #color_list안에 이름들이 하나씩 저장되었다.
    return color_list

#print(name_color())

if __name__ == '__main__':
    i=0
    while(i<len(name_color())):
        a = Color(name=name_color()[i])
        a.save()
        i+=1
