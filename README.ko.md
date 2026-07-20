# 안녕하세요, Ubucon! 12-factor FastAPI 앱에 오신 것을 환영합니다!

<p align="center">
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png">
</p>

\*다른 언어로 읽기: [English](README.md), [한국어](README.ko.md)

이 앱은 12-factor FastAPI 애플리케이션의 간단한 예입니다. FastAPI 프레임워크를 사용하여 구축되었습니다.
이 애플리케이션은 3개의 엔드포인트를 제공합니다:

- /health
- /fibonacci/:number (postgresql 데이터베이스 필요)
- /keys

## 🏃 로컬에서 실행하는 방법

1. 작업 디렉토리 변경

```
cd fastapi-hello-world
```

2. [uv](https://docs.astral.sh/uv/)로 패키지 설치

```
uv sync
```

3. 서버 실행

```
uv run fastapi dev app.py
```

4. 다음 curl 명령어를 사용하여 엔드포인트 테스트

```
curl http://localhost:8000/health
curl http://localhost:8000/fibonacci/9
```

5. 축하합니다! FastAPI Hello World 프로젝트를 완료했습니다!

## 다음 단계

패키징 시작! [다음 브랜치](https://github.com/canonical/paas-charm-workshop/tree/fastapi-01-rock) `git checkout fastapi-01-rock`를 확인하세요.
