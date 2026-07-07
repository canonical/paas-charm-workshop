# Hello Ubucon! Welcome to 12-factor ExpressJS rock!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This section guides you to packing the expressjs-hello-world project into an OCI compliant image
using [Rockcraft](https://github.com/canonical/rockcraft)'s `expressjs-framework` extension.

## 📝 Prerequisites

- (optional): 🤿 [dive](https://github.com/wagoodman/dive) to inspect OCI images

## 📦 How to pack a ExpressJS application

1. Change the working directory
   ```bash
   cd expressjs-hello-world
   ```
2. Initialize the project with rockcraft
   ```bash
   export ROCKCRAFT_ENABLE_EXPERIMENTAL_EXTENSIONS=True
   rockcraft init --profile expressjs-framework
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
3. Pack the rock
   ```bash
   rockcraft pack
   ```
4. (Optional) Inspect the image
   ```bash
   dive docker-archive://expressjs-hello-world_0.1_amd64.rock
   ```
5. Congratulations! You now have an OCI image for expressjs-hello-world application!

## Next steps

Let's start charming! Check out the [next branch](https://github.com/canonical/paas-charm-workshop/tree/expressjs-02-charm) `git checkout expressjs-02-charm`
