# Hello Ubucon! Welcome to 12-factor Go charm!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_200,h_200/https://api.charmhub.io/api/v1/media/download/charm_g5MbnEy7wX7GTPtr20TcB16YCvXXZu2Y_icon_e08d61629f52f85dd79e8222b8b2360a7377af42e1a0f22fceca778ec3226d7c.png">
</p>

This section guides you to extending the go-hello-world project with operational capabilities
using [Juju charms](https://juju.is/).

## Prerequisites

- charmcraft
  ```
  sudo snap install charmcraft --classic
  ```
- unzip
  ```
  sudo apt install unzip
  ```

## How to extend a Go application with Juju charms

1. Change the working directory
   ```
   cd go-hello-world
   ```
2. Create a separate charm directory and change the working directory
   ```
   mkdir charm && cd charm
   ```
3. Initialize the charm
   ```
   charmcraft init --profile go-framework --name go-hello-world
   ```
4. Uncomment the database relation in `charmcraft.yaml`
  ```diff
  + requires:
  +   postgresql:
  +     interface: postgresql_client
  +     optional: false
  +     limit: 1
  ```
  ```bash
  # or append the contents to the file
  cat <<EOF >> charmcraft.yaml
  requires:
    postgresql:
      interface: postgresql_client
      optional: false
      limit: 1
  EOF
  ```
4. (Recommended) modify the `requirements.txt` in the same `charm` directory by adding the following line into the beginning of the file.
  ```diff
  + --no-binary=:none:
  ops ~= 2.17
  paas-charm>=1.0,<2
  ```
  ```bash
  # or use sed:
  sed -i '1s/^/--no-binary=:none:\n/' requirements.txt
  ```
5. (ARM64 only) modify the `platforms` section of the `charmcraft.yaml` file
    ```
    dpkg --print-architecture | grep arm64 && sed -i 's/# arm64/arm64/' charmcraft.yaml
    ```
6. Pack the charm
   ```
   charmcraft pack
   ```
7. Inspect the charm
   ```
   tar -xvzf go-hello-world_$(dpkg --print-architecture).charm
   ```
9. Congratulations! You have have a local charm you can deploy to Juju!

## Next steps

Let's start getting our hands dirty! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/tree/go-03-deploy) `git checkout go-03-deploy`
