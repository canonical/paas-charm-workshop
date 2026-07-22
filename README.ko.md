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

2. charmcraft 로그인

```bash
charmcraft login
```

3. 로컬 레지스트리에 charm과 rock 업로드

```bash
charmcraft upload ./spring-hello-world_amd64.charm
charmcraft upload-resource spring-hello-world app-image --image=oci-archive:../spring-hello-world_0.1_amd64.rock
charmcraft release spring-hello-world --revision=1 --channel=latest/edge --resource=app-image:1
```

4. 애플리케이션을 Juju에 배포

```bash
juju deploy spring-hello-world --channel=latest/edge
```

5. 배포된 애플리케이션을 데이터베이스에 연결

```bash
juju integrate spring-hello-world postgresql-k8s
juju status --watch=5s
```

6. 애플리케이션을 ingress-configurator에 연결

```bash
juju integrate spring-hello-world ingress-configurator
```

   - ingress-configurator 단위 상태에서 ingress IP가 표시될 때까지 대기

      ```bash
      juju status --relations --watch 5s
      ```

7. /etc/hosts에 호스트명 추가

```bash
export INGRESS_IP=$(juju status --format=json | jq -r '.applications["ingress-configurator"].units["ingress-configurator/0"]["address"]')
export SERVICE_HOSTNAME=$(juju config ingress-configurator hostname)
echo "$INGRESS_IP $SERVICE_HOSTNAME" | sudo tee -a /etc/hosts
```

8. 비밀 저장

```bash
curl -X POST http://$SERVICE_HOSTNAME/keys -H "Content-Type: application/json" --data '{"value": "저 사실 민초파입니다."}' -Lkv
```

9. 비밀 검색

```bash
curl http://$SERVICE_HOSTNAME/keys/<key-id>
```

## 추가 정보

전체 튜토리얼은 [12-factor application read the docs](https://canonical-12-factor-app-support.readthedocs-hosted.com/latest/tutorial/)에서 확인할 수 있습니다!
