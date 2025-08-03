# Hello Ubucon! Welcome to 12-factor Go deployment!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_450,h_366/https://assets.ubuntu.com/v1/8e1d3bf5-juju-hero-juju.is.svg">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This section guides you through deploying a Go application on Juju and Microk8s!

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

## 🚀 How to deploy a Go application on Juju

In this section, to be nice to our network, we've already populated the go application image
on MicroK8s.

We'll also be using a shared Juju + Microk8s cluster :)

1. Test your juju connection
   ```
   juju controllers
   juju models
   ```
2. Switch to your Juju model
   ```
   juju switch <your-model-name>
   ```
3. Find SaaS offers
   ```
   juju find-offers ubucon-controller:
   ```
4. Import SaaS applications
   ```
   juju consume admin/database.postgresql
   juju consume admin/cos.prometheus-k8s
   juju consume admin/cos.loki-k8s
   juju consume admin/cos.grafana-k8s
   ```
5. Deploy the application to Juju
   ```bash
   juju deploy ./go-hello-world/charm/go-hello-world_$(dpkg --print-architecture).charm --resource app-image=localhost:32000/go-hello-world:0.1
   ```
6. Relate the deployed application to database
   ```
   juju relate go-hello-world postgresql
   juju status
   ```
7. Test the application using the unit IP address
   ```bash
   UNIT_IP=<your application's unit IP>
   curl http://$UNIT_IP:8000/health
   ```
8. Deploy nginx-ingress-integrator charm
   ```
   juju deploy nginx-ingress-integrator --trust --config path-routes=/ --config service-hostname=<your-model-name>
   ```
9. Relate the application application to nginx-ingress-integrator
   ```
   juju relate go-hello-world nginx-ingress-integrator
   ```
   - Wait for the ingress IP to show up on the nginx-ingress-integrator unit status
     ```
     juju status --relations --watch 5s
     ```
10. Add your application endpoint to `/etc/hosts` file
    ```
    INGRESS_IP=<ingress-ip>
    MODEL_NAME=<your-model-name>
    echo "$INGRESS_IP $MODEL_NAME" | sudo tee -a /etc/hosts
    ```
11. Store your secret
    ```
    curl -X POST http://$INGRESS_IP/keys/ -H "Content-Type: application/json" --data '{"value": "I like mint flavored ice-cream and pizza with pineapples"}' -Lkv
    ```
12. Retrieve your secret
    ```
    curl http://$INGRESS_IP/keys/<key-id>
    ```
13. Relate Canonical Observability Stack (COS)
    ```
    juju relate go-hello-world prometheus-k8s
    juju relate go-hello-world loki-k8s
    juju relate go-hello-world grafana-k8s
    ```
14. Visit the Grafana URL (link & credentials in spreadsheet)

## Further information

The complete documentation and tutorial is available at [12-factor application read the docs](https://canonical-12-factor-app-support.readthedocs-hosted.com/latest/tutorial/)!
