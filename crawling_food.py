import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from nickname.models import Food


def name_food():
    # 1페이지 : https://ko.wiktionary.org/wiki/%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EC%9D%8C%EC%8B%9D
    # 2페이지 : https://ko.wiktionary.org/w/index.php?title=%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EC%9D%8C%EC%8B%9D&pagefrom=%EC%85%94%EB%B2%97#mw-pages
    req = requests.get('https://ko.wiktionary.org/w/index.php?title=%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EC%9D%8C%EC%8B%9D&pagefrom=%EC%85%94%EB%B2%97#mw-pages')
    html = req.content.decode('utf-8','replace') #한글이 깨져서 넣어주었다.
    soup = BeautifulSoup(html, 'html.parser')
    #select하는데 자꾸 td별로 구분되어서 아예 젤 마지막 부분으로 분류하였더니 하나씩 구분되었다.
    food_name = soup.select('#mw-pages > div > div > div > ul > li > a')

    food_list = []
    for name in food_name:
        food_list.append(name.text.strip())
        #food_list안에 이름들이 하나씩 저장되었다.
    return food_list

#print(name_food())


if __name__ == '__main__':
    i=0
    while(i<len(name_food())):
        a = Food(name=name_food()[i])
        a.save()
        i+=1
