# 안녕하세요, Ubucon! 12-factor Spring Boot charm에 오신 것을 환영합니다!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_200,h_200/https://api.charmhub.io/api/v1/media/download/charm_g5MbnEy7wX7GTPtr20TcB16YCvXXZu2Y_icon_e08d61629f52f85dd79e8222b8b2360a7377af42e1a0f22fceca778ec3226d7c.png">
</p>

\*다른 언어로 읽기: [English](README.md), [한국어](README.ko.md)

이 섹션은 [Juju charms](https://juju.is/)를 사용하여 spring-hello-world 프로젝트에 운영 능력을 확장하는 방법을 안내합니다.

## 📝 필수 조건

- ✨ charmcraft

```bash
sudo snap install charmcraft --classic --channel=latest/edge
```

- 📂 unzip

```bash
sudo apt install unzip
```

## 🪄 Spring Boot 애플리케이션을 Juju charms로 확장하는 방법

1. 작업 디렉토리 변경

```bash
cd spring-hello-world
```

2. 별도의 charm 디렉토리 생성 및 작업 디렉토리 변경

```bash
mkdir charm && cd charm
```

3. charm 초기화

```bash
charmcraft init --profile spring-boot-framework --name spring-hello-world
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

5. (권장) 같은 `charm` 디렉토리의 `requirements.txt` 파일을 수정하여 다음 줄 추가

```diff
+ --no-binary=:none:
ops ~= 2.17
paas-charm>=1.0,<2
```

```bash
# 또는 sed 사용:
sed -i '1s/^/--no-binary=:none:\n/' requirements.txt
```

6. (ARM64 전용) `charmcraft.yaml` 파일의 `platforms` 섹션 수정

```bash
dpkg --print-architecture | grep arm64 && sed -i 's/# arm64/arm64/' charmcraft.yaml
```

7. charm 패키징

```bash
charmcraft pack
```

8. charm 내용 확인

```bash
mkdir inspect
unzip spring-hello-world_$(dpkg --print-architecture).charm -d inspect
```
   
9. 축하합니다! 이제 Juju에 배포할 수 있는 로컬 charm이 준비되었습니다!

## 다음 단계

배포 시작! [다음 브랜치](https://github.com/yanksyoon/hello-ubucon/tree/spring-03-deploy) `git checkout spring-03-deploy`을 확인하세요.
