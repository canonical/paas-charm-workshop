# Hello Ubucon! Welcome to 12-factor FastAPI app!

<p align="center">
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This is a simple example of a 12-factor FastAPI application. It's built using the FastAPI framework.
This application exposes 3 endpoints:

- /health
- /fibonacci/:number (requires postgresql database)
- /keys

## 🏃 How to run it locally?

1. Change the working directory

```
cd django-hello-world
```

2. Create a virtual environment and install the dependencies

```
python3 -m venv .venv && source .venv/bin/activate && pip3 install -r requirements.txt
```

3. Run the server

```
fastapi dev app.py
```

4. Test the endpoints using the following curl commands

```
curl http://localhost:8000/health
curl http://localhost:8000/fibonacci/9
```

5. Congratulations! You've finished exploring the FastAPI Hello World project!

## Next steps

Let's start packaging! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/tree/fastapi-01-rock) `git checkout fastapi-01-rock`
