# Hello Ubucon! Welcome to 12-factor ExpressJS deployment!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_450,h_366/https://assets.ubuntu.com/v1/8e1d3bf5-juju-hero-juju.is.svg">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This section guides you through deploying a ExpressJS application on Juju and K8s!

## 🚀 How to deploy a ExpressJS application on Juju

1. Test your juju connection

```bash
juju controllers
juju models
```

2. Login to charmcraft

```bash
charmcraft login
```

3. Upload the charm and rock to the local registry

```bash
charmcraft upload ./expressjs-hello-world_amd64.charm
charmcraft upload-resource expressjs-hello-world app-image --image=oci-archive:../expressjs-hello-world_0.1_amd64.rock
charmcraft release expressjs-hello-world --revision=1 --channel=latest/edge --resource=app-image:1
```

4. Deploy the application to Juju

```bash
juju deploy expressjs-hello-world --channel=latest/edge
```

5. Integrate the deployed application with the database

```bash
juju integrate expressjs-hello-world postgresql-k8s
juju status --watch=5s
```

6. Integrate the application with ingress-configurator

```bash
juju integrate expressjs-hello-world ingress-configurator
```

  - Wait for the ingress IP to show up on the ingress-configurator unit status

    ```bash
    juju status --relations --watch 5s
    ```

7. Add the hostname to /etc/hosts

```bash
export INGRESS_IP=$(juju status --format=json | jq -r '.applications["ingress-configurator"].units["ingress-configurator/0"]["address"]')
export SERVICE_HOSTNAME=$(juju config ingress-configurator hostname)
echo "$INGRESS_IP $SERVICE_HOSTNAME" | sudo tee -a /etc/hosts
```

8. Store your secret

```bash
curl -X POST http://$SERVICE_HOSTNAME/keys/ -H "Content-Type: application/json" --data '{"value": "I like mint flavored ice-cream and pizza with pineapples"}' -Lkv
```

9. Retrieve your secret

```bash
curl http://$SERVICE_HOSTNAME/keys/<key-id>
```

## Further information

The complete documentation and tutorial is available at [12-factor application documentation](https://canonical.com/juju/docs/12-factor/latest/)!
