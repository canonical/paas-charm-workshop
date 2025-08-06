# 안녕하세요, Ubucon! 12-factor Go 앱에 오신 것을 환영합니다!

<p align="center">
    <img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR069DA1jDGVM8x3_8vpwJtjjyabv40qNkm7A5NTiJyRzIYPf38vO8SW4v7R4YcvekCdjCZ6smEpvMk6j3pHTK05QH8PSkP0Dy8IjA-Y-th">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

이 앱은 12-factor Spring Boot 애플리케이션의 간단한 예입니다. Spring Boot의 Spring Initializr를 사용하여 초기화되었습니다.

이 애플리케이션은 3개의 엔드포인트를 제공합니다:

- /health
- /fibonacci/:number (postgresql 데이터베이스 필요)
- /keys

## 필요 사항

- java

```bash
sudo apt install -y default-jdk
```

- (선택사항) devpack-for-spring snap

```bash
sudo snap install devpack-for-spring --classic
devpack-for-spring boot start \
  --path spring-hello-world \
  --project maven-project \
  --language java \
  --boot-version 3.4.4 \
  --version 0.0.1 \
  --group com.example \
  --artifact spring-hello-world \
  --name spring-hello-world \
  --description "Demo project for Spring Boot" \
  --package-name com.example.spring-hello-world \
  --dependencies web \
  --packaging jar \
  --java-version 21
```

## 🏃 로컬에서 실행하는 방법

1. 작업 디렉토리 변경

```bash
cd spring-hello-world
```


2. 서버 실행

```bash
./mvnw spring-boot:run
```

3. 다음 curl 명령어를 사용하여 엔드포인트 테스트

```
curl http://localhost:8080/health
curl http://localhost:8080/fibonacci/9
```

4. 축하합니다! Spring Hello World 프로젝트 탐색을 완료했습니다!

## 다음 단계

패키징 시작! [다음 브랜치](https://github.com/yanksyoon/hello-ubucon/tree/springboot-01-rock) `git checkout springboot-01-rock`을 확인하세요.
