# 안녕하세요, Ubucon! 12-factor Django charm에 오신 것을 환영합니다!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_200,h_200/https://api.charmhub.io/api/v1/media/download/charm_g5MbnEy7wX7GTPtr20TcB16YCvXXZu2Y_icon_e08d61629f52f85dd79e8222b8b2360a7377af42e1a0f22fceca778ec3226d7c.png">
</p>

\*다른 언어로 읽기: [English](README.md), [한국어](README.ko.md)

이 섹션은 [Juju charms](https://juju.is/)를 사용하여 django-hello-world 프로젝트에 운영 능력을 확장하는 방법을 안내합니다.

## 📝 필수 조건

## 🪄 Django 애플리케이션을 Juju charms로 확장하는 방법

1. 작업 디렉토리 변경
   ```bash
   cd django-hello-world
   ```
2. 별도의 charm 디렉토리 생성 및 작업 디렉토리 변경
   ```bash
   mkdir charm && cd charm
   ```
3. charm 초기화
   ```bash
   charmcraft init --profile django-framework --name django-hello-world
   ```
4. `charmcraft.yaml`에서 데이터베이스 관계 주석 해제

```diff
+ requires:
+   postgresql:
+     interface: postgresql_client
+     optional: false
+     limit: 1
```

```bash
# 또는 파일에 내용을 추가
cat <<EOF >> charmcraft.yaml
requires:
  postgresql:
    interface: postgresql_client
    optional: false
    limit: 1
EOF
```

5. charm 패키징
   ```bash
   charmcraft pack
   ```
6. charm 검사
   ```bash
   mkdir inspect
   unzip django-hello-world_ubuntu-22.04-amd64.charm -d inspect
   ```
7. 축하합니다! 이제 Juju에 배포할 수 있는 로컬 charm이 준비되었습니다!

## 다음 단계

배포 시작! [다음 브랜치](https://github.com/canonical/paas-charm-workshop/tree/django-03-deploy) `git checkout django-03-deploy`을 확인하세요.
