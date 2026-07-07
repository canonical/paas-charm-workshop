# Hello Ubucon! Welcome to 12-factor Django app!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJ9iCTco4K9EbOUZleXxEvUyFvLXGEHCyg9Q&s">
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This is a simple example of a 12-factor Django application. It's built using the Django framework.
This application is built using the [django-admin](https://docs.djangoproject.com/en/5.2/ref/django-admin/)
and exposes 3 endpoints:

- /health
- /fibonacci/:number
- /keys

## 🏃 How to run it locally?

1. Change the working directory

```
cd django-hello-world
```

2. Install the dependencies with [uv](https://docs.astral.sh/uv/) with [uv](https://docs.astral.sh/uv/)

```
uv sync
```

3. Run the server

```
DJANGO_DEBUG=true DJANGO_ALLOWED_HOSTS='["*"]' uv run ./django_hello_world/manage.py runserver
```

4. Run the database migration script

```
uv run uv run uv run ./django_hello_world/manage.py migrate
```

5. Test the endpoints using the following curl commands

```
curl http://localhost:8000/health
curl http://localhost:8000/fibonacci/9
curl -X POST http://localhost:8000/keys/ -H "Content-Type: application/json" --data '{"value": "golden snitch"}'
curl http://localhost:8000/keys/<key_id>
```

5. Congratulations! You've finished exploring the Django Hello World project!

## Next steps

Let's start packaging! Check out the [next branch](https://github.com/canonical/paas-charm-workshop/tree/django-01-rock) `git checkout django-01-rock`
