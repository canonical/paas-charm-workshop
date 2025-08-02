# Hello Ubucon! Welcome to 12-factor ExpressJS rock!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

This section guides you to packing the expressjs-hello-world project into an OCI compliant image
using [Rockcraft](https://github.com/canonical/rockcraft)'s `expressjs-framework` extension.

## Prerequisites

- rockcraft
  ```
  sudo snap install rockcraft --channel=latest/edge --classic
  ```
- lxd
  ```
  sudo snap install lxd && lxd init --auto
  ```
- (optional): [docker](https://docs.docker.com/engine/install/)
- (optional): [dive](https://github.com/wagoodman/dive) to inspect OCI images

## How to pack a FastAPI application

1. Change the working directory
   ```
   cd expressjs-hello-world
   ```
2. Initialize the project with rockcraft
   ```
   export ROCKCRAFT_ENABLE_EXPERIMENTAL_EXTENSIONS=True
   rockcraft init --profile expressjs-framework
   ```
  - Inspect the rockcraft extension
    ```
    rockcraft expand-extensions
    ```
  - Add the postgresql-client package to the runtime
    ```
    cat <<EOF >> rockcraft.yaml
    parts:
      runtime-debs:
        plugin: nil
        stage-packages:
          # Added manually for the migrations
          - postgresql-client
    EOF
    ```
  - (ARM64 only) modify the `platforms` section of the `rockcraft.yaml` file
    ```
    dpkg --print-architecture | grep arm64 && sed -i 's/# arm64/arm64' rockcraft.yaml
    ```
2. Pack the rock
   ```
   rockcraft pack
   ```
3. (Optional) Push the image to the local Docker registry
    ```bash
    rockcraft.skopeo copy \
      --insecure-policy \
      --dest-tls-verify=false \
      oci-archive:./expressjs-hello-world_0.1_$(dpkg --print-architecture).rock \
      docker-daemon:expressjs-hello-world:0.1
    ```
4. (Optional) Inspect the image
   ```
   dive expressjs-hello-world:0.1
   ```
5. Congratulations! You now have an OCI image for expressjs-hello-world application!

## Next steps

Let's start charming! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/tree/expressjs-02-charm) `git checkout expressjs-02-charm`
