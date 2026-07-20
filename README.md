# Hello Ubucon! Welcome to 12-factor Spring Boot deployment!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_450,h_366/https://assets.ubuntu.com/v1/8e1d3bf5-juju-hero-juju.is.svg">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This section guides you through deploying a Spring Boot application on Juju and K8s!

## 🚀 How to deploy a Spring Boot application on Juju

1. Test your juju connection

```bash
juju controllers
juju models
```

2. Switch to your Juju model

```bash
export MODEL_NAME=<your-model-name>
juju switch $MODEL_NAME
```

3. Find SaaS offers

```bash
juju find-offers ubucon-controller:
```

4. Import SaaS applications

```bash
juju consume admin/postgres.postgresql-k8s
juju consume admin/cos.prometheus-k8s
juju consume admin/cos.loki-k8s
juju consume admin/cos.grafana-k8s
```

5. Deploy the application to Juju

```bash
export APPLICATION_NAME=<your-model-name>
juju deploy ./spring-hello-world/charm/spring-hello-world_amd64.charm \
  $APPLICATION_NAME \
  --resource app-image=localhost:32000/spring-hello-world:0.1
```

6. Relate the deployed application to database

```bash
juju relate $APPLICATION_NAME postgresql-k8s
juju status --watch=5s
```

7. Test the application using the unit IP address

```bash
UNIT_IP=<your application unit IP>
curl http://$UNIT_IP:8000/health
```

8. Deploy ingress-configurator charm

```bash
export SERVICE_HOSTNAME="$MODEL_NAME.ubuntu.local"
juju deploy ingress-configurator --trust \
  --config paths="/" \
  --config hostname=$SERVICE_HOSTNAME
```

9. Relate the application application to ingress-configurator

```bash
juju relate $APPLICATION_NAME ingress-configurator
```

  - Wait for the ingress IP to show up on the ingress-configurator unit status

    ```bash
    juju status --relations --watch 5s
    ```

11. Store your secret

```bash
curl -X POST http://$SERVICE_HOSTNAME/keys/ -H "Content-Type: application/json" --data '{"value": "I like mint flavored ice-cream and pizza with pineapples"}' -Lkv
```

12. Retrieve your secret

```bash
curl http://$SERVICE_HOSTNAME/keys/<key-id>
```

13. Relate Canonical Observability Stack (COS)

```bash
juju relate $APPLICATION_NAME prometheus-k8s
juju relate $APPLICATION_NAME loki-k8s
juju relate $APPLICATION_NAME grafana-k8s
juju status --watch=5s
```


## Further information

The complete documentation and tutorial is available at [12-factor application read the docs](https://canonical-12-factor-app-support.readthedocs-hosted.com/latest/tutorial/)!
