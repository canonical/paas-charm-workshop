# 안녕하세요, Ubucon! 12-factor Go 배포에 오신 것을 환영합니다!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_450,h_366/https://assets.ubuntu.com/v1/8e1d3bf5-juju-hero-juju.is.svg">
</p>

\*다른 언어로 읽기: [English](README.md), [한국어](README.ko.md)

이 섹션은 Juju와 K8s에서 Go 애플리케이션을 배포하는 방법을 안내합니다!

## 🚀 Go 애플리케이션을 Juju에 배포하는 방법

1. Juju 연결 테스트

```bash
juju controllers
juju models
```

2. Juju 모델 전환

```bash
export MODEL_NAME=<your-model-name>
juju switch $MODEL_NAME
```

3. 애플리케이션을 Juju에 배포

```bash
export APPLICATION_NAME=<your-model-name>
juju deploy ./go-hello-world/charm/go-hello-world_amd64.charm \
   $APPLICATION_NAME \
   --resource app-image=localhost:32000/go-hello-world:0.1
```

4. 배포된 애플리케이션을 데이터베이스에 연결

```bash
juju relate $APPLICATION_NAME postgresql-k8s
juju status --watch=5s
```

5. ingress-configurator charm 배포

```bash
export SERVICE_HOSTNAME="$MODEL_NAME.ubuntu.local"
juju deploy ingress-configurator --trust --config paths=/ --config hostname=$SERVICE_HOSTNAME
```

6. 애플리케이션을 ingress-configurator에 연결

```bash
juju relate $APPLICATION_NAME ingress-configurator
```

   - ingress-configurator 상태에서 ingress IP가 표시될 때까지 대기

      ```bash
      juju status --relations --watch 5s
      ```

7. 비밀 저장

```bash
curl -X POST http://$SERVICE_HOSTNAME/keys/ -H "Content-Type: application/json" --data '{"value": "저 사실 민초파입니다."}' -Lkv
```

8. 비밀 검색

```bash
curl http://$SERVICE_HOSTNAME/keys/<key-id>
```

## 추가 정보

전체 튜토리얼은 [12-factor application read the docs](https://canonical-12-factor-app-support.readthedocs-hosted.com/latest/tutorial/)에서 확인할 수 있습니다!
