# Hello Ubucon! Welcome to 12-factor ExpressJS rock!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

This section guides you to packing the expressjs-hello-world project into an OCI compliant image
using [Rockcraft](https://github.com/canonical/rockcraft)'s `expressjs-framework` extension.

## Prerequisites

- rockcraft: `sudo snap install rockcraft --channel=latest/edge`
- lxd: `sudo snap install lxd && lxd init --auto`
- (optional): [dive](https://github.com/wagoodman/dive) to inspect OCI images

## How to pack a FastAPI application

0. Change the working directory: `cd expressjs-hello-world`
1. Initialize the project with rockcraft: `rockcraft init --profile expressjs-framework`
  - Inspect the rockcraft extension `rockcraft expand-extensions`
2. Pack the rock: `rockcraft pack`
3. Push the image to the local Docker registry:
    ```bash
    rockcraft.skopeo copy \
      --insecure-policy \
      --dest-tls-verify=false \
      oci-archive:./fastapi-hello-world_0.1_amd64.rock \
      docker://expressjs-hello-world:0.1
    ```
4. (Optional) Inspect the image: `dive expressjs-hello-world:0.1`
5. Congratulations! You now have an OCI image for expressjs-hello-world application!

## Next steps

Let's start charming! Check out the next branch `git checkout expressjs-02-charm`