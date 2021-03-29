# web_emr_data
> 헬스케어 데이터를 활용한 django 실습

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

- [x] 