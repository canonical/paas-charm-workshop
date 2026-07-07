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

## 📝 Prerequisites

The following snaps are required for the tutorial.

Install them with:

```bash
sudo snap install rockcraft --classic
sudo snap install charmcraft --classic
sudo snap install juju --channel=3/stable
sudo snap install lxd && lxd init --auto
```
