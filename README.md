# Hello Ubucon! Welcome to 12-factor Flask charm!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_200,h_200/https://api.charmhub.io/api/v1/media/download/charm_g5MbnEy7wX7GTPtr20TcB16YCvXXZu2Y_icon_e08d61629f52f85dd79e8222b8b2360a7377af42e1a0f22fceca778ec3226d7c.png">
</p>

This section guides you to extending the flask-hello-world project with operational capabilities
using [Juju charms](https://juju.is/).

## Prerequisites

- charmcraft: `sudo snap install charmcraft --classic`

## How to extend a Flask application with Juju charms

0. Change the working directory: `cd flask-hello-world`
1. Create a separate charm directory and change the working directory: `mkdir charm && cd charm`
2. Initialize the charm: `charmcraft init --profile flask-framework --name flask-hello-world`
3. Uncomment the database relation in `charmcraft.yaml`
  ```diff
  + requires:
  +   postgresql:
  +     interface: postgresql_client
  +     optional: false
  +     limit: 1
  ```
4. (Recommended) modify the `requirements.txt` in the same `charm` directory by adding the following line into the beginning of the file.
  ```diff
  + --no-binary=:none:
  ops ~= 2.17
  paas-charm>=1.0,<2
  ```
5. Pack the charm: `charmcraft pack`
6. Inspect the charm: `mkdir inspect && unzip flask-hello-world_ubuntu-22.04-$(dpkg --print-architecture).charm -d inspect`
7. Congratulations! You have have a local charm you can deploy to Juju!

## Next steps

Let's start getting our hands dirty! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/tree/flask-03-deploy) `git checkout flask-03-deploy`
