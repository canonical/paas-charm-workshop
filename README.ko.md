# 안녕하세요, Ubucon! 12-factor Spring Boot 배포에 오신 것을 환영합니다!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_450,h_366/https://assets.ubuntu.com/v1/8e1d3bf5-juju-hero-juju.is.svg">
</p>

\*다른 언어로 읽기: [English](README.md), [한국어](README.ko.md)

이 섹션은 Juju와 K8s에서 Spring Boot 애플리케이션을 배포하는 방법을 안내합니다!

## 🚀 Spring Boot 애플리케이션을 Juju에 배포하는 방법

1. Juju 연결 테스트

```bash
juju controllers
juju models
```

2. Juju 모델로 전환

```bash
export MODEL_NAME=<your-model-name>
juju switch $MODEL_NAME
```

3. SaaS 오퍼 찾기

```bash
juju find-offers ubucon-controller:
```

4. SaaS 애플리케이션 가져오기

```bash
juju consume admin/postgres.postgresql-k8s
juju consume admin/cos.prometheus-k8s
juju consume admin/cos.loki-k8s
juju consume admin/cos.grafana-k8s
```

5. 애플리케이션을 Juju에 배포

```bash
export APPLICATION_NAME=<your-model-name>
juju deploy ./spring-hello-world/charm/spring-hello-world_amd64.charm \
  $APPLICATION_NAME \
  --resource app-image=localhost:32000/spring-hello-world:0.1
```

6. 배포된 애플리케이션을 데이터베이스에 연결

```bash
juju relate $APPLICATION_NAME postgresql-k8s
juju status --watch=5s
```

7. IP 주소를 사용하여 애플리케이션 테스트

```bash
UNIT_IP=<your application unit IP>
curl http://$UNIT_IP:8000/health
```

8. ingress-configurator charm 배포

```bash
export SERVICE_HOSTNAME="$MODEL_NAME.ubuntu.local"
juju deploy ingress-configurator --trust \
  --config paths="/" \
  --config hostname=$SERVICE_HOSTNAME
```

9. 애플리케이션을 ingress-configurator에 연결

```bash
juju relate $APPLICATION_NAME ingress-configurator
```

   - ingress-configurator 단위 상태에서 ingress IP가 표시될 때까지 대기

      ```bash
      juju status --relations --watch 5s
      ```

11. 비밀 저장

```bash
curl -X POST http://$SERVICE_HOSTNAME/keys/ -H "Content-Type: application/json" --data '{"value": "저 사실 민초파입니다."}' -Lkv
```

12. 비밀 검색

```bash
curl http://$SERVICE_HOSTNAME/keys/<key-id>
```

13. Canonical Observability Stack (COS) 연결

```bash
juju relate $APPLICATION_NAME prometheus-k8s
juju relate $APPLICATION_NAME loki-k8s
juju relate $APPLICATION_NAME grafana-k8s
juju status --watch=5s
```

14. Grafana URL 방문 (링크 및 자격 증명은 스프레드시트에서 확인)

## 추가 정보

전체 튜토리얼은 [12-factor application read the docs](https://canonical-12-factor-app-support.readthedocs-hosted.com/latest/tutorial/)에서 확인할 수 있습니다!
