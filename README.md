# Hello Ubucon! Welcome to 12-factor Go rock!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

This section guides you to packing the go-hello-world project into an OCI compliant image
using [Rockcraft](https://github.com/canonical/rockcraft)'s `go-framework` extension.

## Prerequisites

- rockcraft: `sudo snap install rockcraft --channel=latest/edge`
- lxd: `sudo snap install lxd && lxd init --auto`
- (optional): [dive](https://github.com/wagoodman/dive) to inspect OCI images

## How to pack a Go application

0. Change the working directory: `cd go-hello-world`
1. Initialize the project with rockcraft: `rockcraft init --profile go-framework`
  - Inspect the rockcraft extension `rockcraft expand-extensions`
2. Pack the rock: `rockcraft pack`
  - If you're on ARM based architecture, modify the `platforms` section of the `rockcraft.yaml` file.
    ```diff
      platforms:
    -   amd64:
    -   # arm64:
    +   # amd64:
    +   arm64:
    ```
3. Push the image to the local Docker registry:
    ```bash
    rockcraft.skopeo copy \
      --insecure-policy \
      --dest-tls-verify=false \
      oci-archive:./go-hello-world_0.1_$(dpkg --print-architecture).rock \
      docker-daemon:go-hello-world:0.1
    ```
4. (Optional) Inspect the image: `dive go-hello-world:0.1`
5. Congratulations! You now have an OCI image for go-hello-world application!

## Next steps

Let's start charming! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/tree/go-02-charm) `git checkout go-02-charm`
