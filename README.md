# Hello Ubucon! Welcome to 12-factor Flask app!

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7sHccHQUzTTgVX3-vKj2a-Sl1QniFKUvu2mQM1WJIRS0qmLD6V4AnSXVlRtCOlnK7exaAQiLhaDzORMCQfyfy_Oxi08PzT2Rm2aZuMo93vA">
</p>

This is a simple example of a 12-factor Flask application. It's built using the Flask framework.
This application exposes 3 endpoints:
- /health
- /fibonacci/:number (requires postgresql database)
- /keys

## How to run it locally?

0. Change the working directory: `cd flask-hello-world`
1. Create a virtual environment and install the dependencies: `python3 -m venv .venv && source .venv/bin/activate && pip3 install -r requirements.txt`
2. Run the server: `python3 app.py`
4. Test the endpoints using the following curl commands
  - `curl http://localhost:3000/health`
  - `curl http://localhost:3000/fibonacci/9`
5. Congratulations! You've finished exploring the Flask Hello World project!

## Next steps

Let's start packaging! Check out the [next branch](https://github.com/yanksyoon/hello-ubucon/tree/flask-01-rock) `git checkout flask-01-rock`
