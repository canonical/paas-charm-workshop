# Hello Ubucon! Welcome to 12-factor Go rock!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This section guides you to packing the go-hello-world project into an OCI compliant image
using [Rockcraft](https://github.com/canonical/rockcraft)'s `go-framework` extension.

## 📝 Prerequisites

- 🪨 rockcraft
  ```
  sudo snap install rockcraft --channel=latest/edge --classic
  ```
- ☁️ lxd
  ```
  sudo snap install lxd && lxd init --auto
  ```
- (optional): 🤿 [dive](https://github.com/wagoodman/dive) to inspect OCI images

## 📦 How to pack a Go application

1. Change the working directory
  ```bash
  cd go-hello-world
  ```
2. Initialize the project with rockcraft
  ```bash
  rockcraft init --profile go-framework
  ```
  - Inspect the rockcraft extension
    ```bash
    export ROCKCRAFT_ENABLE_EXPERIMENTAL_EXTENSIONS=True
    rockcraft expand-extensions
    ```
  - Add the postgresql-client package to the runtime
    ```bash
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
    ```bash
    dpkg --print-architecture | grep arm64 && sed -i 's/# arm64/arm64/' rockcraft.yaml
    ```
2. Pack the rock
  ```
  rockcraft pack
  ```
3. (Optional) Inspect the image
  ```bash
  dive docker-archive://go-hello-world_0.1_$(dpkg --print-architecture).rock
  ```
5. Congratulations! You now have an OCI image for go-hello-world application!

## Next steps

Let's start charming! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/tree/go-02-charm) `git checkout go-02-charm`
