# Hello Ubucon! Welcome to 12-factor FastAPI deployment!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_450,h_366/https://assets.ubuntu.com/v1/8e1d3bf5-juju-hero-juju.is.svg">
</p>

This section guides you through deploying a FastAPI application on Juju and Microk8s!

## Prerequisites

- [Juju](https://juju.is/): `sudo snap install juju --channel=3/stable`
- Juju credentials (we don't want to overload the network with Juju and Microk8s)

## How to deploy a FastAPI application on Juju

In this section, to be nice to our network, we've already populated the fastapi application image
on MicroK8s.

We'll also be using a shared Juju + Microk8s cluster, please ask for credentials :)

0. Setup your Juju connection to the shared Juju controller: `tar -xvzf juju_credentials.tar.gz -C ~/.local/share/juju`
1. Test your Juju connection: `juju controllers`, `juju models`
2. Switch to your Juju model: `juju switch <your-model-name>`
3. Deploy the application to Juju
    ```bash
    juju deploy ./fastapi-hello-world/charm/fastapi-hello-world_$(dpkg --print-architecture).charm --resource app-image=localhost:32000/fastapi-hello-world:0.1
    ```
4. Relate the deployed application to database: `juju relate fastapi-hello-world postgresql`
5. Test the application using the unit IP address:
    ```bash
    UNIT_IP=<your application's unit IP>
    curl http://$UNIT_IP:8080/health
    ```

## Further information

The complete documentation and tutorial is available at [12-factor application read the docs](https://canonical-12-factor-app-support.readthedocs-hosted.com/latest/tutorial/)!
