# Hello Ubucon! Welcome to 12-factor FastAPI charm!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_200,h_200/https://api.charmhub.io/api/v1/media/download/charm_g5MbnEy7wX7GTPtr20TcB16YCvXXZu2Y_icon_e08d61629f52f85dd79e8222b8b2360a7377af42e1a0f22fceca778ec3226d7c.png">
</p>

This section guides you to extending the fastapi-hello-world project with operational capabilities
using [Juju charms](https://juju.is/).

## Prerequisites

- charmcraft: `sudo snap install charmcraft --classic`

## How to extend a FastAPI application with Juju charms

0. Change the working directory: `cd fastapi-hello-world`
1. Create a separate charm directory and change the working directory: `mkdir charm && cd charm`
2. Initialize the charm: `charmcraft init --profile fastapi-framework --name fastapi-hello-world`
3. Pack the charm: `charmcraft pack`
4. Inspect the charm: `mkdir inspect && unzip fastapi-hello-world_$(dpkg --print-architecture).charm -d inspect`
5. Congratulations! You have have a local charm you can deploy to Juju!

## Next steps

Let's start getting our hands dirty! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/tree/fastapi-03-deploy) `git checkout fastapi-03-deploy`
