# randomname_site
옵션을 선택하여 원하는 테마의 랜덤 닉네임을 얻을 수 있다.

DB안에 각 테마별 단어들을 crawling하여 DB(postrgreSQL)안에 저장하였다.(예를들면 동물이나 음식 등)

사용자는 단어테마를 선택할 수 있고 선택하면 랜덤으로 단어와 조합된 닉네임이 생성된다.

어느정도 구성만 짜뒀고 계속 데이터베이스 추가할 예정이다.

### 4월 15일
heroku로 배포 완료
- https://teorandomname.herokuapp.com/

### 4월 17일
추가로 사는 지역 적어서 '강동 멋쟁이' 같이 지역별 닉네임도 만들 수 있게 생성

문제는 어떻게 멋쟁이 와 같은 db를 넣을 것인지 고민... 일단은 내가 직접 몇개 적어두었지만 한계가 있음.

### 4월 19일
공유 버튼을 추가하였고, 광고를 삽입하려 했으나 뭔가 너무 상업적인거 같아서 일단은 보류함. 조금 더 수정해보고 알맞은 사용자수가 확보되면 고려해볼 듯.
사용자 수를 늘리기 위해 SEO설정함. 네이버 웹마스터도구에서 추가 후 robot추가. sitemap추가는 조금 복잡해서 추후 추가 예정
