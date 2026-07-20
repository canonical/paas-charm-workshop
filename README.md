# Hello Ubucon! Welcome to 12-factor Spring Boot charm!

<p align="center">
    <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_200,h_200/https://api.charmhub.io/api/v1/media/download/charm_g5MbnEy7wX7GTPtr20TcB16YCvXXZu2Y_icon_e08d61629f52f85dd79e8222b8b2360a7377af42e1a0f22fceca778ec3226d7c.png">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This section guides you to extending the spring-hello-world project with operational capabilities
using [Juju charms](https://juju.is/).

## 🪄 How to extend a Spring Boot application with Juju charms

1. Change the working directory

```bash
cd spring-hello-world
```

2. Create a separate charm directory and change the working directory

```bash
mkdir charm && cd charm
```

3. Initialize the charm

```bash
charmcraft init --profile spring-boot-framework --name spring-hello-world
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

5. Pack the charm

```bash
charmcraft pack
```

6. Inspect the charm

```bash
mkdir inspect
unzip spring-hello-world_amd64.charm -d inspect
```

7. Congratulations! You have have a local charm you can deploy to Juju!

## Next steps

Let's start getting our hands dirty! Check out the [next branch](https://github.com/canonical/paas-charm-workshop/tree/springboot-03-deploy) `git checkout springboot-03-deploy`
