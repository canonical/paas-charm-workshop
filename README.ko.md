# 🚀 12-Factor 애플리케이션을 선택하여 끝까지 배포하기!

<p align="center">
  <img src="./docs/juju_status.png">
</p>

\*다른 언어로 읽기: [English](README.md), [한국어](README.ko.md)

이 리포지토리는 "선택한 12-factor 애플리케이션을 끝까지 배포하기!" 세미나의 시작점입니다. 원하는 프레임워크를 선택하고 환경에 배포하세요.
세미나의 각 단계는 이 리포지토리의 브랜치로 되어 있으니, 모든 단계를 수행할 시간이 없더라도 걱정하지 마세요!

## 🌱 시작하는 방법

1. 이 리포지토리를 복제합니다.

   ```bash
   git clone https://github.com/canonical/paas-charm-workshop.git
   ```

2. 다음 프레임워크 중 하나를 선택합니다:

- [Django](https://github.com/canonical/paas-charm-workshop/tree/django) (`git checkout django`)
- [ExpressJS](https://github.com/canonical/paas-charm-workshop/tree/expressjs) (`git checkout expressjs`)
- [FastAPI](https://github.com/canonical/paas-charm-workshop/tree/fastapi) (`git checkout fastapi`)
- [Flask](https://github.com/canonical/paas-charm-workshop/tree/flask) (`git checkout flask`)
- [Go](https://github.com/canonical/paas-charm-workshop/tree/go) (`git checkout go`)
- [Spring Boot](https://github.com/canonical/paas-charm-workshop/tree/springboot) (`git checkout springboot`)

3. 선택한 프레임워크의 브랜치로 전환합니다 (예: `git checkout django`)

4. `README.md`의 지침을 따릅니다!

## 👨🏻‍💻 이 세미나가 끝나면

- 선택한 12-factor 애플리케이션을 끝까지 배포할 수 있습니다!
  - 애플리케이션 OCI 이미지를 생성하고 저장소에 올립니다.
  - 애플리케이션을 Juju + K8s 환경에 배포합니다.

## 📝 필수 조건

세미나를 위해 필요한 도구는 다음과 같습니다.

- [Rockcraft](https://snapcraft.io/rockcraft)
  ```bash
  sudo snap install rockcraft --classic
  ```
- [Charmcraft](https://snapcraft.io/charmcraft)
  ```bash
  sudo snap install charmcraft --classic
  ```
- [Juju](https://snapcraft.io/juju)
  ```bash
  sudo snap install juju --channel=3.6/stable
  ```
- [Canonical Kubernetes](https://snapcraft.io/k8s)
  ```bash
  sudo snap install k8s --classic --channel=1.35-classic/stable
  ```
- [LXD](https://snapcraft.io/lxd)
  ```bash
  sudo snap install lxd && lxd init --auto
  ```
- (선택 사항) [unzip](https://packages.ubuntu.com/search?keywords=unzip) charm 패키지 내용을 확인하기 위한 도구
  ```bash
  sudo apt install unzip
  ```
- (선택 사항) 🤿 [dive](https://github.com/wagoodman/dive) OCI 이미지 분석 도구
  ```bash
  sudo snap install dive
  ```
