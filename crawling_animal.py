import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from nickname.models import Animal
from multiprocessing import Pool

def name_animal():
    req = requests.get('http://animal.memozee.com/animal/Dic/')
    html = req.content.decode('euc-kr','replace')
    soup = BeautifulSoup(html, 'html.parser')
    #select하는데 자꾸 td별로 구분되어서 아예 젤 마지막 부분으로 분류하였더니 하나씩 구분되었다.
    animal_name = soup.select('li > a')

    animal_list = []
    for name in animal_name:
        animal_list.append(name.text.strip())
        #animal_list안에 이름들이 하나씩 저장되었다.
    return animal_list

def save_name(i):
    a = Animal(name=name_animal()[i])
    a.save()

b = []    # 빈 리스트 생성
for j in range(len(name_animal())):
    b.append(j) 

if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(save_name, b)


