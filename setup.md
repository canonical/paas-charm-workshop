# Workshop Environment Setup

This document describes the exact environment setup that is provisioned for workshop users.

## Host preparation

The workshop hosts are Ubuntu machines prepared with the following base packages and snaps.

System packages:

```bash
sudo apt update
sudo apt install -y unzip jq ca-certificates curl
```

Required snaps:

```bash
sudo snap install juju --channel=3.6/stable
sudo snap install charmcraft --classic
sudo snap install rockcraft --classic
sudo snap install lxd
```

Optional inspection utility:

```bash
sudo snap install dive
```

LXD initialization:

```bash
sudo lxd init --auto
```

## Canonical Kubernetes setup

The local Kubernetes substrate is provided by Canonical Kubernetes.

Install the k8s snap:

```bash
sudo snap install k8s --classic --channel=1.35-classic/stable
```

Bootstrap the cluster and wait until ready:

```bash
sudo k8s bootstrap
sudo k8s status --wait-ready
```

Configure the load balancer:

```bash
sudo k8s enable load-balancer
sudo k8s set load-balancer.cidrs=10.3.254.45-10.3.254.48 load-balancer.l2-mode=true
```

Verify Canonical Kubernetes feature state:

```bash
sudo k8s status
```

You should see the following output:

```bash
ubuntu@d2-8-2026-07-17-12-23:~$ sudo k8s status
cluster status:           ready
control plane nodes:      51.79.143.96:6400 (voter)
high availability:        no
datastore:                etcd
network:                  enabled
dns:                      enabled at 10.152.183.246
ingress:                  disabled
load-balancer:            enabled, L2 mode
local-storage:            enabled at /var/snap/k8s/common/rawfile-storage
gateway                   enabled
```

Prepare kube config for the ubuntu user:

```bash
mkdir -p /home/ubuntu/.kube
sudo k8s config > /home/ubuntu/.kube/config
sudo chown ubuntu:ubuntu /home/ubuntu/.kube/config
```

Bootstrap the k8s cloud on to Juju:

```bash
sudo k8s config | juju add-k8s local-k8s --client
juju bootstrap local-k8s workshop
```

**NOTE**: All the above manual steps (installation and configuration of the Juju environment) can be automatically done with [Concierge](https://github.com/canonical/concierge).

## Private charm registry setup (Spellbook)

The workshop environment includes a custom private charm registry backed by Spellbook. This is an optional step. Users can directly upload to the official CharmHub registry if required (or even directly deploy the locally packaged charm without uploading). But for the purpose of this workshop, we are creating a private registry. 

Install and configure Spellbook:

```bash
sudo snap install spellbook
sudo snap set spellbook \
   oci.secret-key='replace-this-with-a-long-random-secret' \
   insecure-dev-auth=true admin.usernames=admin \
   public-registry-url=https://<your-ip>:5000 \
   public-api-url=http://<your-ip>:8080 \
   public-storage-url=http://<your-ip>:8080 \
   limits.max-archive-file-bytes=32MB \
   limits.max-upload-bytes=128MB \
   charmhub.max-artifact-bytes=128MB
sudo snap start spellbook
```

Configure Charmcraft endpoints for the custom registry:

```bash
export CHARMCRAFT_STORE_API_URL=http://<your-ip>:8080
export CHARMCRAFT_REGISTRY_URL=https://<your-ip>:5000
export CHARMCRAFT_UPLOAD_URL=http://<your-ip>:8080
```

Trust the local registry certificate on the host:

```bash
sudo cp /var/snap/spellbook/common/certs/oci.crt /usr/local/share/ca-certificates/charm-registry-oci.crt
sudo update-ca-certificates
```

Sync required charms into the private registry from CharmHub:

```bash
spellbook.charm-registryctl sync add postgresql-k8s --track 16
spellbook.charm-registryctl sync add gateway-api-integrator --track 1
spellbook.charm-registryctl sync add ingress-configurator
spellbook.charm-registryctl sync add self-signed-certificates --track 1
```

Ensure all charms show `ok` status before proceeding.
```bash
spellbook.charm-registryctl sync list
```

## Model creation

Create a new model and configure it to use the private charm registry:

```bash

echo "charmhub-url: http://<your-ip>:8080" > ~/juju-config.yaml
juju add-model app --config ~/juju-config.yaml
juju switch workshop:app
```

## Charm deployment

The app model is pre-populated with the following applications and channels:

```bash
juju deploy gateway-api-integrator --channel 1/edge
juju deploy ingress-configurator --channel latest/edge
juju deploy postgresql-k8s --channel 16/edge
juju deploy self-signed-certificates --channel 1/stable
juju integrate gateway-api-integrator self-signed-certificates
juju integrate gateway-api-integrator ingress-configurator
```

## Final Juju status

At this point, setup is complete. The environment should look like this when you run:

```bash
juju status --relations
```

Expected output:

```bash
ubuntu@d2-8-2026-07-17-12-23:~$ juju status --relations
Model  Controller  Cloud/Region  Version  SLA          Timestamp
app    workshop    local-k8s     3.6.25   unsupported  05:28:15Z

App                       Version  Status   Scale  Charm                     Channel      Rev  Address         Exposed  Message
gateway-api-integrator             active       1  gateway-api-integrator    1/edge       170  10.152.183.42   no       Gateway addresses: 10.3.254.45
ingress-configurator               blocked      1  ingress-configurator      latest/edge   95  10.152.183.226  no       Ingress relation required.
postgresql-k8s                     active       1  postgresql-k8s            16/edge      931  10.152.183.237  no
self-signed-certificates           active       1  self-signed-certificates  1/stable     588  10.152.183.254  no

Unit                         Workload  Agent  Address     Ports  Message
gateway-api-integrator/0*    active    idle   10.1.0.197         Gateway addresses: 10.3.254.45
ingress-configurator/0*      blocked   idle   10.1.0.196         Ingress relation required.
postgresql-k8s/0*            active    idle   10.1.0.188         Primary
self-signed-certificates/0*  active    idle   10.1.0.10

Integration provider                   Requirer                             Interface         Type     Message
gateway-api-integrator:gateway-route   ingress-configurator:gateway-route   gateway-route     regular
postgresql-k8s:database-peers          postgresql-k8s:database-peers        postgresql_peers  peer
postgresql-k8s:refresh-v-three         postgresql-k8s:refresh-v-three       refresh           peer
postgresql-k8s:restart                 postgresql-k8s:restart               rolling_op        peer
self-signed-certificates:certificates  gateway-api-integrator:certificates  tls-certificates  regular
```

