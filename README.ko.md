# 안녕하세요, Ubucon! 12-factor Django rock에 오신 것을 환영합니다!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

이번 세션에서는 [Rockcraft](https://github.com/canonical/rockcraft)의 `django-framework` 확장팩을 사용하여 django-hello-world 프로젝트를 OCI 이미지로 패키징하는 방법을 안내합니다.

## 📝 필수 조건

- 🪨 rockcraft
  ```bash
  sudo snap install rockcraft --channel=latest/edge --classic
  ```
- ☁️ lxd
  ```bash
  sudo snap install lxd && lxd init --auto
  ```
- (선택 사항): 🐳 [docker](https://docs.docker.com/engine/install/)
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
   - rockcraft 확장 내용 확인
   ```bash
   ROCKCRAFT_ENABLE_EXPERIMENTAL_EXTENSIONS=True
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
4. (선택 사항) 이미지를 로컬 Docker 레지스트리에 등록:
   ```bash
   rockcraft.skopeo copy \
     --insecure-policy \
     --dest-tls-verify=false \
     oci-archive:./django-hello-world_0.1_$(dpkg --print-architecture).rock \
     docker-daemon:django-hello-world:0.1
   ```
5. (선택 사항) 이미지 검사
   ```bash
   dive django-hello-world:0.1
   ```
6. 축하합니다! 이제 django-hello-world 애플리케이션을 위한 OCI 이미지가 준비되었습니다!

## 다음 단계

쥬쥬 시작! [다음 브랜치](https://github.com/yanksyoon/hello-ubucon/blob/django-02-charm/README.md) `git checkout django-02-charm`을 확인하세요.
