# Hello Ubucon! Welcome to 12-factor Flask rock!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This section guides you to packing the flask-hello-world project into an OCI compliant image
using [Rockcraft](https://github.com/canonical/rockcraft)'s `flask-framework` extension.

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

## 📦 How to pack a Flask application

1. Change the working directory
  ```bash
  cd flask-hello-world
  ```
2. Initialize the project with rockcraft
  ```bash
  rockcraft init --profile flask-framework
  ```
  - Inspect the rockcraft extension
    ```bash
    export ROCKCRAFT_ENABLE_EXPERIMENTAL_EXTENSIONS=True
    rockcraft expand-extensions
    ```
  - (ARM64 only) modify the `platforms` section of the `rockcraft.yaml` file
    ```bash
    dpkg --print-architecture | grep arm64 && sed -i 's/# arm64/arm64/' rockcraft.yaml
    ```

3. Pack the rock
  ```bash
  rockcraft pack
  ```
4. (Optional) Inspect the image
  ```
  dive docker-archive://flask-hello-world_0.1_$(dpkg --print-architecture).rock
  ```
5. Congratulations! You now have an OCI image for flask-hello-world application!

## Next steps

Let's start charming! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/tree/flask-02-charm) `git checkout flask-02-charm`
