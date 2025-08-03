# 안녕하세요, Ubucon! 12-factor ExpressJS 앱에 오신 것을 환영합니다!

<p align="center">
    <img src="https://res.cloudinary.com/practicaldev/image/fetch/s--MgAyrZbI--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn-images-1.medium.com/max/1024/1%2AhYfdBkfKgvtMoDcqk_LjWA.png">
</p>

\*다른 언어로 읽기: [English](README.md), [한국어](README.ko.md)

이 앱은 12-factor ExpressJS 애플리케이션의 간단한 예입니다. ExpressJS 프레임워크를 사용하여 구축되었습니다.
이 애플리케이션은 [express-generator](https://expressjs.com/en/starter/generator.html)를 사용하여 구축되었으며, 3개의 엔드포인트를 제공합니다:

- /health
- /fibonacci/:number (postgresql 데이터베이스 필요)
- /keys

## 📝 필수 조건

- [NodeJS & NPM](https://nodejs.org/en/download)

## 🏃 로컬에서 실행하는 방법

1. 작업 디렉토리 변경

```
cd expressjs-hello-world/app
```

2. 패키지 설치

```
npm install
```

3. 서버 실행

```
npm start
```

4. 다음 curl 명령어를 사용하여 엔드포인트 테스트

```
curl http://localhost:3000/health
curl http://localhost:3000/fibonacci/9
```

5. 축하합니다! ExpressJS Hello World 프로젝트를 완료했습니다!

## 다음 단계

패키징 시작! [다음 브랜치](https://github.com/yanksyoon/hello-ubucon/tree/expressjs-01-rock) `git checkout expressjs-01-rock`를 확인하세요.
