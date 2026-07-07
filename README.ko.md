# 안녕하세요, Ubucon! 12-factor Flask 앱에 오신 것을 환영합니다!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7sHccHQUzTTgVX3-vKj2a-Sl1QniFKUvu2mQM1WJIRS0qmLD6V4AnSXVlRtCOlnK7exaAQiLhaDzORMCQfyfy_Oxi08PzT2Rm2aZuMo93vA">
</p>

12-factor Flask 애플리케이션의 간단한 예제 예제입니다. Flask 프레임워크를 사용하여 구축되었습니다.
이 애플리케이션은 3개의 엔드포인트를 제공합니다:

- /health
- /fibonacci/:number (postgresql 데이터베이스 필요)
- /keys

## 🏃 로컬에서 실행하는 방법은?

1. 작업 디렉토리 변경

```
cd flask-hello-world
```

2. [uv](https://docs.astral.sh/uv/)로 패키지 설치

```
uv sync
```

3. 서버 실행

```
uv run python3 app.py
```

4. curl 명령어를 사용하여 엔드포인트 확인

```
curl http://localhost:3000/health
curl http://localhost:3000/fibonacci/9
```

5. 축하합니다! Flask Hello World 프로젝트 탐색을 완료했습니다!

## 다음 단계

패키징을 시작합시다! [다음 브랜치](https://github.com/canonical/paas-charm-workshop/tree/flask-01-rock)를 확인하세요 `git checkout flask-01-rock`
