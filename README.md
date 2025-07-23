# Hello Ubucon! Welcome to 12-factor Flask deployment!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_450,h_366/https://assets.ubuntu.com/v1/8e1d3bf5-juju-hero-juju.is.svg">
</p>

This section guides you through deploying a Flask application on Juju and Microk8s!

## Prerequisites

- [Juju](https://juju.is/): `sudo snap install juju --channel=3/stable`
- Juju credentials (we don't want to overload the network with Juju and Microk8s)

## How to deploy a Flask application on Juju

In this section, to be nice to our network, we've already populated the flask application image
on MicroK8s. You can do so on your local microk8s deployment using the following command:
```bash
rockcraft.skopeo --insecure-policy copy --dest-tls-verify=false \
  oci-archive:flask-hello-world_0.1_$(dpkg --print-architecture).rock \
  docker://localhost:32000/flask-hello-world:0.1
```

We'll also be using a shared Juju + Microk8s cluster, please ask for credentials :)

0. Setup your Juju connection to the shared Juju controller: `tar -xvzf juju_credentials.tar.gz -C ~/.local/share/juju`
1. Test your juju connection: `juju controllers`, `juju models`
3. Deploy the application to Juju
    ```bash
    APPLICATION_NAME=<your-name-with-no-spaces>
    juju deploy ./flask-hello-world/charm/flask-hello-world_ubuntu-22.04-amd64.charm --resource app-image=localhost:32000/flask-hello-world:0.1 "$APPLICATION_NAME"
    ```
4. Relate the deployed application to database: `juju relate $APPLICATION_NAME postgresql`
5. Test the application using the unit IP address:
    ```bash
    UNIT_IP=<your application's unit IP>
    curl http://$UNIT_IP:8000/health
    ```

## Further information

The complete documentation and tutorial is available at [12-factor application read the docs](https://canonical-12-factor-app-support.readthedocs-hosted.com/latest/tutorial/)!