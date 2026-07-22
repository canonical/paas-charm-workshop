# Hello Ubucon! Welcome to 12-factor Flask deployment!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_450,h_366/https://assets.ubuntu.com/v1/8e1d3bf5-juju-hero-juju.is.svg">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This section guides you through deploying a Flask application on Juju and K8s!

## 🚀 How to deploy a Flask application on Juju

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

3. Upload the charm and rock to the local registry

```bash
charmcraft upload ./flask-hello-world/charm/flask-hello-world_ubuntu-22.04-amd64.charm
charmcraft upload-resource flask-hello-world flask-app-image --image=oci-archive:./flask-hello-world_0.1_amd64.rock
charmcraft release flask-hello-world --revision=1 --channel=latest/edge --resource=flask-app-image:1
```

4. Deploy the application to Juju

```bash
export APPLICATION_NAME=<your-model-name>
juju deploy flask-hello-world $APPLICATION_NAME --channel=latest/edge
```

5. Relate the deployed application to database

```bash
juju relate $APPLICATION_NAME postgresql-k8s
juju status --watch=5s
```

6. Relate the application to ingress-configurator

```bash
export SERVICE_HOSTNAME="$MODEL_NAME.ubuntu.lan"
juju relate $APPLICATION_NAME ingress-configurator
```

  - Wait for the ingress IP to show up on the ingress-configurator unit status

    ```bash
    juju status --relations --watch 5s
    ```

7. Store your secret

```bash
curl -X POST http://$SERVICE_HOSTNAME/keys/ -H "Content-Type: application/json" --data '{"value": "I like mint flavored ice-cream and pizza with pineapples"}' -Lkv
```

8. Retrieve your secret

```bash
curl http://$SERVICE_HOSTNAME/keys/<key-id>
```

## Further information

The complete documentation and tutorial is available at [12-factor application read the docs](https://canonical-12-factor-app-support.readthedocs-hosted.com/latest/tutorial/)!
