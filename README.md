# Hello Ubucon! Welcome to 12-factor Django rock!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_7ioYr9T6uh35rT46Z_cyNVtMM_SgbHppA&s">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This section guides you to packing the django-hello-world project into an OCI compliant image
using [Rockcraft](https://github.com/canonical/rockcraft)'s `django-framework` extension.

## 📦 How to pack a Django application

1. Change the working directory
   ```
   cd django-hello-world
   ```
2. Initialize the project with rockcraft
   ```
   rockcraft init --profile django-framework
   ```
   - Inspect the rockcraft extension
     ```bash
     export ROCKCRAFT_ENABLE_EXPERIMENTAL_EXTENSIONS=True
     rockcraft expand-extensions
     ```
3. Pack the rock

   ```
   rockcraft pack
   ```
   
4. (Optional) Inspect the image

```
dive docker-archive://django-hello-world_0.1_amd64.rock
```

5. Congratulations! You now have an OCI image for django-hello-world application!

## Next steps

Let's start charming! Check out the [next branch](https://github.com/canonical/paas-charm-workshop/tree/django-02-charm) `git checkout django-02-charm`
