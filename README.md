# Hello Ubucon! Welcome to 12-factor Spring Boot rock!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This section guides you to packing the spring-hello-world project into an OCI compliant image
using [Rockcraft](https://github.com/canonical/rockcraft)'s `spring-boot-framework` extension.

## 📦 How to pack a Spring Boot application

1. Change the working directory

```bash
cd spring-hello-world
```

2. Initialize the project with rockcraft

```bash
rockcraft init --profile spring-boot-framework
```
  - Add the migration script to the image

    ```bash
    cat <<EOF >> rockcraft.yaml
    parts:
      runtime-debs:
          plugin: nil
          stage-packages:
              # Added manually for the migrations
              - postgresql-client
      migrate:
          plugin: dump
          source: .
          stage:
              - app/migrate.sh
          organize:
              migrate.sh: app/migrate.sh
    EOF
    ```

3. Pack the rock

```bash
rockcraft pack
```

4. (Optional) Inspect the image

```
dive docker-archive://spring-hello-world_0.1_amd64.rock
```

5. Congratulations! You now have an OCI image for spring-hello-world application!

## Next steps

Let's start charming! Check out the [next branch](https://github.com/canonical/paas-charm-workshop/tree/springboot-02-charm) `git checkout springboot-02-charm`
