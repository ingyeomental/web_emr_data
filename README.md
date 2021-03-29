# web_emr_data
> 헬스케어 데이터를 활용한 Django API 개발(미완성)

## directory tree
```
.
├── README.md
├── app
│   ├── .env               # Django Key, DB env
│   ├── config             # Djanog Config
│   ├── db.sqlite3
│   ├── manage.py            
│   ├── models_total.py    # EMR Dataset Model
│   └── person             # Person API
├── docker
│   ├── nginx              # Web Image
│   ├── postgres           # DB Image
│   └── python             # Django Image
└── docker-compose.yml
```

## Dependence
- Python 3.7-alpine
- Django 2.2
- PostgreSQL >= 13.2


## Get Started

### Step.1 git clone repository
```
$ git clone https://github.com/ingyeomental/Django-React-TodoApp.git
```

### Step2. Create or Start Django + Web + Postgre Container
```
$ docker-compose up --build
```

### Step3. Start Django
```
# 우선 python container에 접속
# vscode "REMOTE EXPLORER"로 "/var/www/html" 경로로 접속하는 걸 추천
$ ./manage.py runserver --settings=config.settings.prod
```

## Issue
- [ ] 500 error 발생
- [ ] 원격 DB에서 불러온 데이터를 계산해서 리턴하는 API 테스트

## Todo List
> 우선순위를 고려

- [x] PostgreSQL 원격서버 접속 및 데이터 확인
- [x] Docker-Compose로 환경구성
- [x] Django Setting(dev용 DB / prod용 DB 구분)
- [x] 전체 환자 수 리턴하는 API 구상
    ```
    {
        'count': 00
    }
    ```
- [ ] API 구현을 위한 에러 해결
- [ ] 다른 테이블 값에 대한 통계도 제공하는 API 개발
    - 환자에 대한 통계는 person/view.py에서 개발
    - 방문에 대한 통계는 새로운 django app을 생성해서 개발
- [ ] 각 테이블에 사용된 concept_id 정보 리턴하는 API 개발
- [ ] 각 테이블의 row를 조회하는 API를 구현
