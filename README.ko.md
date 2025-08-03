# 안녕하세요, Ubucon! 12-factor Go 배포에 오신 것을 환영합니다!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_450,h_366/https://assets.ubuntu.com/v1/8e1d3bf5-juju-hero-juju.is.svg">
</p>

\*다른 언어로 읽기: [English](README.md), [한국어](README.ko.md)

이 섹션은 Juju와 Microk8s에서 Go 애플리케이션을 배포하는 방법을 안내합니다!

## 📝 필수 조건

- 🔮 [Juju](https://juju.is/)
  ```bash
  sudo snap install juju --channel=3/stable
  ```
- 🔑 Juju 서버 세팅/접속키 다운로드 (네트워크 과부하를 방지하기 위해 준비했습니다~)
  - 슬라이드의 Google 스프레드시트 링크에서 쥬쥬 세팅/접속키를 다운로드합니다.
    ```bash
    wget <link-to-juju-controller.tar.gz>
    mkdir -p ~/.local/share/
    tar -xvzf ./juju-controller.tar.gz -C ~/.local/share
    ```
    - 해당 아키텍처에 맞는 Juju 모델을 선택하고 "Assigned" 열에 이름을 기록해주세요.

## 🚀 Go 애플리케이션을 Juju에 배포하는 방법

1. Juju 연결 테스트
   ```bash
   juju controllers
   juju models
   ```
2. Juju 모델로 전환
   ```bash
   juju switch <your-model-name>
   ```
3. SaaS 오퍼 찾기
   ```bash
   juju find-offers ubucon-controller:
   ```
4. SaaS 애플리케이션 가져오기
   ```bash
   juju consume admin/database.postgresql
   juju consume admin/cos.prometheus-k8s
   juju consume admin/cos.loki-k8s
   juju consume admin/cos.grafana-k8s
   ```
5. 애플리케이션을 Juju에 배포
   ```bash
   juju deploy ./go-hello-world/charm/go-hello-world_$(dpkg --print-architecture).charm --resource app-image=localhost:32000/go-hello-world:0.1
   ```
6. 배포된 애플리케이션을 데이터베이스에 연결
   ```bash
   juju relate go-hello-world postgresql
   juju status
   ```
7. IP 주소를 사용하여 애플리케이션 테스트
   ```bash
   UNIT_IP=<your application's unit IP>
   curl http://$UNIT_IP:8000/health
   ```
8. nginx-ingress-integrator charm 배포
   ```bash
   juju deploy nginx-ingress-integrator --trust --config path-routes=/ --config service-hostname=<your-model-name>
   ```
9. 애플리케이션을 nginx-ingress-integrator에 연결
   ```bash
   juju relate go-hello-world nginx-ingress-integrator
   ```
   - nginx-ingress-integrator 단위 상태에서 ingress IP가 표시될 때까지 대기
     ```bash
     juju status --relations --watch 5s
     ```
10. `/etc/hosts` 파일에 애플리케이션 엔드포인트 추가
    ```bash
    INGRESS_IP=<ingress-ip>
    MODEL_NAME=<your-model-name>
    echo "$INGRESS_IP $MODEL_NAME" | sudo tee -a /etc/hosts
    ```
11. 비밀 저장
    ```bash
    curl -X POST http://$INGRESS_IP/keys/ -H "Content-Type: application/json" --data '{"value": "저 사실 민초파입니다."}' -Lkv
    ```
12. 비밀 검색
    ```bash
    curl http://$INGRESS_IP/keys/<key-id>
    ```
13. Canonical Observability Stack (COS) 연결
    ```bash
    juju relate go-hello-world prometheus-k8s
    juju relate go-hello-world loki-k8s
    juju relate go-hello-world grafana-k8s
    ```
14. Grafana URL 방문 (링크 및 자격 증명은 스프레드시트에서 확인)

## 추가 정보

전체 튜토리얼은 [12-factor application read the docs](https://canonical-12-factor-app-support.readthedocs-hosted.com/latest/tutorial/)에서 확인할 수 있습니다!
