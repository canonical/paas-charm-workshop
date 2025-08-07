# 안녕하세요, Ubucon! 12-factor Flask rock에 오신 것을 환영합니다!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

\*다른 언어로 읽기: [English](README.md), [한국어](README.ko.md)

이 섹션은 [Rockcraft](https://github.com/canonical/rockcraft)의 `spring-boot-framework` 확장을 사용하여 spring-hello-world 프로젝트를 OCI 이미지로 패키징하는 방법을 안내합니다.

## 📝 필수 조건

- 🪨 rockcraft

```bash
sudo snap install rockcraft --channel=latest/edge --classic
```

- ☁️ lxd

```bash
sudo snap install lxd && lxd init --auto
```

- (선택 사항): 🤿 [dive](https://github.com/wagoodman/dive) OCI 이미지 분석 도구

## 📦 Flask 애플리케이션 패키징 방법

1. 작업 디렉토리 변경

```bash
cd spring-hello-world
```

2. rockcraft로 프로젝트 초기화

```bash
rockcraft init --profile spring-boot-framework
```

  - 데이터베이스 마이그레이션 스크립트 추가

    ```bash
    cat <<EOF >> rockcraft.yaml
    parts:
      runtime-debs:
          plugin: nil
          stage-packages:
              # Added manually for the migrations
              - postgresql-client
      migrate:
          plugin: dump
          source: .
          stage:
              - app/migrate.sh
          organize:
              migrate.sh: app/migrate.sh
    EOF
    ```

   - rockcraft 확장 내용 확인

  ```bash
  export ROCKCRAFT_ENABLE_EXPERIMENTAL_EXTENSIONS=True
  rockcraft expand-extensions
  ```

   - (ARM64 전용) `rockcraft.yaml` 파일의 `platforms` 섹션 수정

  ```bash
  dpkg --print-architecture | grep arm64 && sed -i 's/# arm64/arm64/' rockcraft.yaml
  ```

3. rock 패키징

```bash
rockcraft pack
```

4. (선택 사항) 이미지 분석

```bash
dive docker-archive://spring-hello-world_0.1_$(dpkg --print-architecture).rock
```

5. 축하합니다! 이제 spring-hello-world 애플리케이션을 위한 OCI 이미지가 준비되었습니다!

## 다음 단계

쥬쥬 시작! [다음 브랜치](https://github.com/yanksyoon/hello-ubucon/tree/springboot-02-charm) `git checkout springboot-02-charm`을 확인하세요.
