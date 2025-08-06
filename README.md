# Hello Ubucon! Welcome to 12-factor Go app!

<p align="center">
    <img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR069DA1jDGVM8x3_8vpwJtjjyabv40qNkm7A5NTiJyRzIYPf38vO8SW4v7R4YcvekCdjCZ6smEpvMk6j3pHTK05QH8PSkP0Dy8IjA-Y-th">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This is a simple example of a 12-factor Spring Boot application. It's initialized using the 
Spring Initializr tool, packaged as a snap.

This application exposes 3 endpoints:

- /health
- /fibonacci/:number (requires postgresql database)
- /keys

## Prerequisites

- java

```bash
sudo apt install -y default-jdk
```

- (Optional) devpack-for-spring snap

```bash
sudo snap install devpack-for-spring --classic
devpack-for-spring boot start \
  --path spring-hello-world \
  --project maven-project \
  --language java \
  --boot-version 3.4.4 \
  --version 0.0.1 \
  --group com.example \
  --artifact spring-hello-world \
  --name spring-hello-world \
  --description "Demo project for Spring Boot" \
  --package-name com.example.spring-hello-world \
  --dependencies web \
  --packaging jar \
  --java-version 21
```

## 🏃 How to run it locally?

1. Change the working directory

```bash
cd spring-hello-world
```

2. Run the server

```bash
./mvnw spring-boot:run
```

3. Test the endpoints using the following curl commands

```
curl http://localhost:8080/health
curl http://localhost:8080/fibonacci/9
```

4. Congratulations! You've finished exploring the Spring Hello World project!

## Next steps

Let's start packaging! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/tree/springboot-01-rock) `git checkout springboot-01-rock`
