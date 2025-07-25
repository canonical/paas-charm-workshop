# Hello Ubucon! Welcome to 12-factor Go app!

<p align="center">
    <img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR069DA1jDGVM8x3_8vpwJtjjyabv40qNkm7A5NTiJyRzIYPf38vO8SW4v7R4YcvekCdjCZ6smEpvMk6j3pHTK05QH8PSkP0Dy8IjA-Y-th">
</p>

This is a simple example of a 12-factor Go application. It's built using the Go's default web framework.
This application exposes 3 endpoints:
- /health
- /fibonacci/:number (requires postgresql database)
- /keys

## How to run it locally?

0. Change the working directory: `cd go-hello-world`
1. Run the server: `go run .`
4. Test the endpoints using the following curl commands
  - `curl http://localhost:8080/health`
  - `curl http://localhost:8080/fibonacci/9`
5. Congratulations! You've finished exploring the Go Hello World project!

## Next steps

Let's start packaging! Check out the next branch `git checkout go-01-rock`
