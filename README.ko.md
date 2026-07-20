# 안녕하세요, Ubucon! 12-factor Go rock에 오신 것을 환영합니다!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

\*다른 언어로 읽기: [English](README.md), [한국어](README.ko.md)

이 섹션은 [Rockcraft](https://github.com/canonical/rockcraft)의 `go-framework` 확장을 사용하여 go-hello-world 프로젝트를 OCI 이미지로 패키징하는 방법을 안내합니다.

## 📦 Go 애플리케이션 패키징 방법

1. 작업 디렉토리 변경
   ```bash
   cd go-hello-world
   ```
2. rockcraft로 프로젝트 초기화
   ```bash
   rockcraft init --profile go-framework
   ```
   - rockcraft 확장 검사
   ```bash
   export ROCKCRAFT_ENABLE_EXPERIMENTAL_EXTENSIONS=True
   rockcraft expand-extensions
   ```
   - runtime에 postgresql-client 패키지 추가
   ```bash
   cat <<EOF >> rockcraft.yaml
   parts:
      runtime-debs:
         plugin: nil
         stage-packages:
         # Added manually for the migrations
         - postgresql-client
   EOF
   ```
3. rock 패키징
   ```bash
   rockcraft pack
   ```
3. (선택 사항) 이미지 분석
   ```bash
   dive docker-archive://go-hello-world_0.1_amd64.rock
   ```
6. 축하합니다! 이제 go-hello-world 애플리케이션을 위한 OCI 이미지가 준비되었습니다!

## 다음 단계

쥬쥬 시작! [다음 브랜치](https://github.com/canonical/paas-charm-workshop/tree/go-02-charm) `git checkout go-02-charm`을 확인하세요.
