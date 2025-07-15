# Deploy a 12-factor application of your choice end-to-end!

This repository is the starting point of the seminar "Deploy a 12-factor application of your
choice end-to-end!". Choose a framework of your choice and deploy it to an environment. Each step
of the seminar is a branch in this repository, so don't worry if you don't have time for all steps.

## How to start

1. Clone this repository
2. Choose one of the following frameworks:
  - Django (`git checkout django`)
  - ExpressJS (`git checkout expressjs`)
  - FastAPI (`git checkout fastapi`)
  - Flask (`git checkout flask`)
  - Go (`git checkout go`)
  - Spring Boot
3. Switch the branch to the framework you chose (e.g., `git checkout django`)
4. Follow the instructions in the `README.md`!

## Intended outcomes

- You should be able to deploy a 12-factor application of your choice end-to-end! This means that:
   - The application OCI image is created and pushed to a repository.
   - The application is deployed to a Juju + Microk8s environment.

## Prerequisites

The following snaps are required for the tutorial.

- [Rockcraft](https://snapcraft.io/rockcraft)
- [Charmcraft](https://snapcraft.io/charmcraft)
- [Juju](https://snapcraft.io/juju)
- [LXD](https://snapcraft.io/lxd)
