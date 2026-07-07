# 안녕하세요, Ubucon! 12-factor Django 앱에 오신 것을 환영합니다!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJ9iCTco4K9EbOUZleXxEvUyFvLXGEHCyg9Q&s">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

이 앱은 12-factor Django 애플리케이션의 간단한 예입니다. Django 프레임워크를 사용하여 구축되었습니다.
이 애플리케이션은 [django-admin](https://docs.djangoproject.com/en/5.2/ref/django-admin/)을 사용하여 구축되었으며, 3개의 엔드포인트를 제공합니다:

- /health
- /fibonacci/:number
- /keys

## 🏃 로컬에서 실행하는 방법

1. 작업 디렉토리 변경

```
cd django-hello-world
```

2. [uv](https://docs.astral.sh/uv/)로 [uv](https://docs.astral.sh/uv/)로 패키지 설치

```
uv sync
```

3. 서버 실행

```
DJANGO_DEBUG=true DJANGO_ALLOWED_HOSTS='["*"]' uv run ./django_hello_world/manage.py runserver
```

4. 데이터베이스 마이그레이션 스크립트 실행

```
uv run uv run uv run uv run ./django_hello_world/manage.py migrate
```

5. 다음 curl 명령어를 사용하여 엔드포인트 테스트

```
curl http://localhost:8000/health
curl http://localhost:8000/fibonacci/9
curl -X POST http://localhost:8000/keys/ -H "Content-Type: application/json" --data '{"value": "golden snitch"}'
curl http://localhost:8000/keys/<key_id>
```

6. 축하합니다! Django Hello World 프로젝트를 완성했습니다!

## 다음 단계

패키징 시작! [다음 브랜치](https://github.com/canonical/paas-charm-workshop/tree/django-01-rock) `git checkout django-01-rock`을 확인하세요.
