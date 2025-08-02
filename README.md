# Hello Ubucon! Welcome to 12-factor Flask rock!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

This section guides you to packing the flask-hello-world project into an OCI compliant image
using [Rockcraft](https://github.com/canonical/rockcraft)'s `flask-framework` extension.

## Prerequisites

- rockcraft: `sudo snap install rockcraft --channel=latest/edge`
- lxd: `sudo snap install lxd && lxd init --auto`
- (optional): [docker](https://docs.docker.com/engine/install/)
- (optional): [dive](https://github.com/wagoodman/dive) to inspect OCI images

## How to pack a Flask application

0. Change the working directory: `cd flask-hello-world`
1. Initialize the project with rockcraft: `rockcraft init --profile flask-framework`
  - Inspect the rockcraft extension `export ROCKCRAFT_ENABLE_EXPERIMENTAL_EXTENSIONS=True && rockcraft expand-extensions`
2. Pack the rock: `rockcraft pack`
  - If you're on ARM based architecture, modify the `platforms` section of the `rockcraft.yaml` file.
    ```diff
      platforms:
    -   amd64:
    -   # arm64:
    +   # amd64:
    +   arm64:
    ```
3. (Optional) Push the image to the local Docker registry:
    ```bash
    rockcraft.skopeo copy \
      --insecure-policy \
      --dest-tls-verify=false \
      oci-archive:./flask-hello-world_0.1_$(dpkg --print-architecture).rock \
      docker-daemon:flask-hello-world:0.1
    ```
4. (Optional) Inspect the image: `dive flask-hello-world:0.1`
5. Congratulations! You now have an OCI image for flask-hello-world application!

## Next steps

Let's start charming! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/tree/flask-02-charm) `git checkout flask-02-charm`
