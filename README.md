# Hello Ubucon! Welcome to 12-factor ExpressJS deployment!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_450,h_366/https://assets.ubuntu.com/v1/8e1d3bf5-juju-hero-juju.is.svg">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This section guides you through deploying a ExpressJS application on Juju and K8s!

## 📝 Prerequisites

- 🔮 [Juju](https://juju.is/)
  ```
  sudo snap install juju --channel=3/stable
  ```
## 🚀 How to deploy a ExpressJS application on Juju

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
juju find-offers
```
  
4. Import SaaS applications

```bash
juju consume admin/postgres.postgresql-k8s
```

```bash
juju consume admin/cos.prometheus
juju consume admin/cos.loki
juju consume admin/cos.grafana
```

5. Deploy the application to Juju

```bash
export APPLICATION_NAME=<your-model-name>
juju deploy ./expressjs-hello-world/charm/expressjs-hello-world_amd64.charm \
  $APPLICATION_NAME \
  --resource app-image=localhost:32000/expressjs-hello-world:0.1
```

6. Relate the deployed application to database

```bash
juju relate $APPLICATION_NAME postgresql-k8s
juju status --watch=5s
```

7. Deploy ingress-configurator charm

```bash
export SERVICE_HOSTNAME="$MODEL_NAME.ubuntu.lan"
juju deploy ingress-configurator --trust \
  --config paths="/" \
  --config hostname=$SERVICE_HOSTNAME
```

8. Relate the application to ingress-configurator

```bash
juju relate $APPLICATION_NAME ingress-configurator
```

  - Wait for the ingress IP to show up on the ingress-configurator unit status

    ```bash
    juju status --relations --watch 5s
    ```

9. Store your secret

```bash
curl -X POST http://$SERVICE_HOSTNAME/keys/ -H "Content-Type: application/json" --data '{"value": "I like mint flavored ice-cream and pizza with pineapples"}' -Lkv
```

10. Retrieve your secret

```bash
curl http://$SERVICE_HOSTNAME/keys/<key-id>
```
    
11. Relate Canonical Observability Stack (COS)

```bash
juju relate $APPLICATION_NAME prometheus
juju relate $APPLICATION_NAME loki
juju relate $APPLICATION_NAME grafana
juju status --watch=5s
```

## Further information

The complete documentation and tutorial is available at [12-factor application read the docs](https://canonical-12-factor-app-support.readthedocs-hosted.com/latest/tutorial/)!
