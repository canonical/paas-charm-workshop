# 안녕하세요, Ubucon! 12-factor Django rock에 오신 것을 환영합니다!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

이번 세션에서는 [Rockcraft](https://github.com/canonical/rockcraft)의 `django-framework` 확장팩을 사용하여 django-hello-world 프로젝트를 OCI 이미지로 패키징하는 방법을 안내합니다.

## 📝 필수 조건

- (선택 사항): 🤿 [dive](https://github.com/wagoodman/dive)OCI 이미지 분석 도구

## 📦 Django 애플리케이션 패키징 방법

1. 작업 디렉토리 변경
   ```bash
   cd django-hello-world
   ```
2. rockcraft로 프로젝트 초기화
   ```bash
   rockcraft init --profile django-framework
   ```
3. rock 패키징

```bash
rockcraft pack
```

4. (선택 사항) 이미지 검사

```
dive docker-archive://django-hello-world_0.1_amd64.rock
```

5. 축하합니다! 이제 django-hello-world 애플리케이션을 위한 OCI 이미지가 준비되었습니다!

## 다음 단계

쥬쥬 시작! [다음 브랜치](https://github.com/canonical/paas-charm-workshop/tree/django-02-charm) `git checkout django-02-charm`을 확인하세요.
