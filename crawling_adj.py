import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from nickname.models import Adjective


def name_adjective():
    req = requests.get('https://ko.wiktionary.org/wiki/%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EA%B4%80%ED%98%95%EC%82%AC%ED%98%95(%ED%98%95%EC%9A%A9%EC%82%AC)')
    html = req.content.decode('utf-8','replace') #한글이 깨져서 넣어주었다.
    soup = BeautifulSoup(html, 'html.parser')
    #select하는데 자꾸 td별로 구분되어서 아예 젤 마지막 부분으로 분류하였더니 하나씩 구분되었다.
    adjective_name = soup.select('#mw-pages > div > div > div > ul > li > a')

    adjective_list = []
    for name in adjective_name:
        adjective_list.append(name.text.strip())
        #adjective_list안에 이름들이 하나씩 저장되었다.
    return adjective_list

#print(name_adjective())

if __name__ == '__main__':
    i=0
    while(i<len(name_adjective())):
        a = Adjective(name=name_adjective()[i])
        a.save()
        i+=1
