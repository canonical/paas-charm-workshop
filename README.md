# Hello Ubucon! Welcome to 12-factor Flask deployment!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_450,h_366/https://assets.ubuntu.com/v1/8e1d3bf5-juju-hero-juju.is.svg">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This section guides you through deploying a Flask application on Juju and Microk8s!

## 📝 Prerequisites

- 🔮 [Juju](https://juju.is/)
  ```
  sudo snap install juju --channel=3/stable
  ```
- 🔑 Juju credentials (we don't want to overload the network with Juju and Microk8s)
  - Go to the Google Spreadsheet link on the slides and,
    1. download the credentials
    ```
    wget <link-to-juju-controller.tar.gz>
    mkdir -p ~/.local/share/
    tar -xvzf ./juju-controller.tar.gz -C ~/.local/share
    ```
    2. choose a Juju model with your corresponding architecture, mark your name down on the "Assigned" column.

## 🚀 How to deploy a Flask application on Juju

In this section, to be nice to our network, we've already populated the flask application image
on MicroK8s.

We'll also be using a shared Juju + Microk8s cluster :)

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
juju deploy ./flask-hello-world/charm/flask-hello-world_ubuntu-22.04-$(dpkg --print-architecture).charm \
  $APPLICATION_NAME \
  --resource flask-app-image=localhost:32000/flask-hello-world:0.1
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

8. Deploy nginx-ingress-integrator charm

```bash
export SERVICE_HOSTNAME="$MODEL_NAME.ubuntu.local"
juju deploy nginx-ingress-integrator --trust \
  --config path-routes="/" \
  --config service-hostname=$SERVICE_HOSTNAME
```

9. Relate the application application to nginx-ingress-integrator

```bash
juju relate $APPLICATION_NAME nginx-ingress-integrator
```

  - Wait for the ingress IP to show up on the nginx-ingress-integrator unit status

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
```

14. Visit the Grafana URL (link & credentials in spreadsheet)

## Further information

The complete documentation and tutorial is available at [12-factor application read the docs](https://canonical-12-factor-app-support.readthedocs-hosted.com/latest/tutorial/)!
