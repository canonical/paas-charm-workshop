# 🚀 Deploy a 12-factor application of your choice end-to-end!

<p align="center">
  <img src="./docs/juju_status.png">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This repository is the starting point of the seminar "Deploy a 12-factor application of your
choice end-to-end!". Choose a framework of your choice and deploy it to an environment. Each step
of the seminar is a branch in this repository, so don't worry if you don't have time for all steps.

## 🌱 How to start

1. Clone this repository

```bash
git clone https://github.com/canonical/paas-charm-workshop.git
```

2. Choose one of the following frameworks:

- [Django](https://github.com/canonical/paas-charm-workshop/tree/django) (`git checkout django`)
- [ExpressJS](https://github.com/canonical/paas-charm-workshop/tree/expressjs) (`git checkout expressjs`)
- [FastAPI](https://github.com/canonical/paas-charm-workshop/tree/fastapi) (`git checkout fastapi`)
- [Flask](https://github.com/canonical/paas-charm-workshop/tree/flask) (`git checkout flask`)
- [Go](https://github.com/canonical/paas-charm-workshop/tree/go) (`git checkout go`)
- [Spring Boot](https://github.com/canonical/paas-charm-workshop/tree/springboot) (`git checkout springboot`)

3. Switch the branch to the framework you chose (e.g., `git checkout django`)
4. Follow the instructions in the `README.md`!

## 👨🏻‍💻 Intended outcomes

- You should be able to deploy a 12-factor application of your choice end-to-end! This means that:
  - The application OCI image is created and pushed to a repository.
  - The application is deployed to a Juju + K8s environment.

## 📚 Further reading

- [Workshop environment setup details](setup.md): If you're interesting in learning more about the exact setup steps for the pre-provisioned Juju environment users receive at the workshop.

## 📝 Prerequisites

The following tools are required for the tutorial.

- [Rockcraft](https://snapcraft.io/rockcraft)
  ```bash
  sudo snap install rockcraft --classic
  ```
- [Charmcraft](https://snapcraft.io/charmcraft)
  ```bash
  sudo snap install charmcraft --classic
  ```
- [Juju](https://snapcraft.io/juju)
  ```bash
  sudo snap install juju --channel=3.6/stable
  ```
- [Canonical Kubernetes](https://snapcraft.io/k8s)
  ```bash
  sudo snap install k8s --classic --channel=1.35-classic/stable
  ```
- [LXD](https://snapcraft.io/lxd)
  ```bash
  sudo snap install lxd && lxd init --auto
  ```
- (optional) [unzip](https://packages.ubuntu.com/search?keywords=unzip) to inspect the charm package contents.
  ```bash
  sudo apt install unzip
  ```
- (optional) 🤿 [dive](https://github.com/wagoodman/dive) to inspect OCI images
  ```bash
  sudo snap install dive
  ```
