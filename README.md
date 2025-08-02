# Hello Ubucon! Welcome to 12-factor ExpressJS deployment!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_450,h_366/https://assets.ubuntu.com/v1/8e1d3bf5-juju-hero-juju.is.svg">
</p>

This section guides you through deploying a ExpressJS application on Juju and Microk8s!

## Prerequisites

- [Juju](https://juju.is/): `sudo snap install juju --channel=3/stable`
- Juju credentials (we don't want to overload the network with Juju and Microk8s)
  - Go to the Google Spreadsheet link on the slides and,
    1. download the credentials
    2. choose a Juju model with your corresponding architecture, mark your name down on the "Assigned" column.

## How to deploy a ExpressJS application on Juju

In this section, to be nice to our network, we've already populated the expressjs application image
on MicroK8s.

We'll also be using a shared Juju + Microk8s cluster, please ask for credentials :)

0. Setup your Juju connection to the shared Juju controller: `tar -xvzf juju_credentials.tar.gz -C ~/.local/share/juju`
1. Test your Juju connection: `juju controllers`, `juju models`
2. Switch to your Juju model: `juju switch <your-model-name>`
3. Find SaaS offers: `juju find-offers ubucon-controller`
4. Import SaaS applications:
   - `juju consume admin/database.postgresql`
   - `juju consume admin/cos.prometheus`
   - `juju consume admin/cos.loki`
   - `juju consume admin/cos.grafana`
5. Deploy the application to Juju
    ```bash
    juju deploy ./expressjs-hello-world/charm/expressjs-hello-world_$(dpkg --print-architecture).charm --resource app-image=localhost:32000/expressjs-hello-world:0.1
    ```
6. Relate the deployed application to database: `juju relate expressjs-hello-world postgresql`
7. Test the application using the unit IP address:
    ```bash
    UNIT_IP=<your application's unit IP>
    curl http://$UNIT_IP:8080/health
    ```
8. Deploy nginx-ingress-integrator charm: `juju deploy nginx-ingress-integrator --trust --config path-routes=/ --config service-hostname=<your-model-name>`
9. Relate the application application to nginx-ingress-integrator: `juju relate expressjs-hello-world nginx-ingress-integrator`
   - Wait for the ingress IP to show up on the nginx-ingress-integrator unit status: `juju status --relations --watch 5s`
11. Add your application endpoint to `/etc/hosts` file: `echo "<ingress-ip> <your-model-name>" | sudo tee -a /etc/hosts`
12. Store your secret: `curl -X POST http://<ingress-ip>/keys/ -H "Content-Type: application/json" --data '{"value": "I like mint flavored ice-cream and pizza with pineapples"}' -Lkv`
13. Retrieve your secret: `curl http://<ingress-ip>/keys/<key-id>`

## Further information

The complete documentation and tutorial is available at [12-factor application read the docs](https://canonical-12-factor-app-support.readthedocs-hosted.com/latest/tutorial/)!
