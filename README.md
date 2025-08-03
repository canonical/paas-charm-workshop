# Hello Ubucon! Welcome to 12-factor FastAPI rock!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This section guides you to packing the fastapi-hello-world project into an OCI compliant image
using [Rockcraft](https://github.com/canonical/rockcraft)'s `fastapi-framework` extension.

## 📝 Prerequisites

- 🪨 rockcraft
  ```
  sudo snap install rockcraft --channel=latest/edge --classic
  ```
- ☁️ lxd
  ```
  sudo snap install lxd && lxd init --auto
  ```
- (optional): 🐳 [docker](https://docs.docker.com/engine/install/)
- (optional): 🤿 [dive](https://github.com/wagoodman/dive) to inspect OCI images

## 📦 How to pack a FastAPI application

1. Change the working directory
   ```
   cd fastapi-hello-world
   ```
2. Initialize the project with rockcraft

   ```rockcraft init --profile fastapi-framework

   ```

- Inspect the rockcraft extension
  ```
  export ROCKCRAFT_ENABLE_EXPERIMENTAL_EXTENSIONS=True
  rockcraft expand-extensions
  ```
- (ARM64 only) modify the `platforms` section of the `rockcraft.yaml` file
  ```
  dpkg --print-architecture | grep arm64 && sed -i 's/# arm64/arm64/' rockcraft.yaml
  ```

3. Pack the rock
   ```
   rockcraft pack
   ```
4. (Optional) Push the image to the local Docker registry
   ```bash
   rockcraft.skopeo copy \
     --insecure-policy \
     --dest-tls-verify=false \
     oci-archive:./fastapi-hello-world_0.1_$(dpkg --print-architecture)$.rock \
     docker-daemon:fastapi-hello-world:0.1
   ```
5. (Optional) Inspect the image
   ```
   dive fastapi-hello-world:0.1
   ```
6. Congratulations! You now have an OCI image for fastapi-hello-world application!

## Next steps

Let's start charming! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/tree/fastapi-02-charm) `git checkout fastapi-02-charm`
