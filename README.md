# Hello Ubucon! Welcome to 12-factor Django rock!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

This section guides you to packing the django-hello-world project into an OCI compliant image
using [Rockcraft](https://github.com/canonical/rockcraft)'s `django-framework` extension.

## Prerequisites

- rockcraft: `sudo snap install rockcraft --channel=latest/edge`
- lxd: `sudo snap install lxd && lxd init --auto`
- (optional): [docker](https://docs.docker.com/engine/install/)
- (optional): [dive](https://github.com/wagoodman/dive) to inspect OCI images

## How to pack a Django application

0. Change the working directory: `cd django-hello-world`
1. Initialize the project with rockcraft: `rockcraft init --profile django-framework`
  - Inspect the rockcraft extension `rockcraft expand-extensions`
2. Pack the rock: `rockcraft pack`
3. Push the image to the local Docker registry:
    ```bash
    rockcraft.skopeo copy \
      --insecure-policy \
      --dest-tls-verify=false \
      oci-archive:./django-hello-world_0.1_$(dpkg --print-architecture).rock \
      docker-daemon:django-hello-world:0.1
    ```
4. (Optional) Inspect the image: `dive django-hello-world:0.1`
5. Congratulations! You now have an OCI image for django-hello-world application!

## Next steps

Let's start charming! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/blob/django-02-charm/README.md) `git checkout django-02-charm`
