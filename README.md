# Hello Ubucon! Welcome to 12-factor ExpressJS app!

<p align="center">
    <img width="554" height="554" alt="image" src="https://github.com/user-attachments/assets/5815e8c8-8297-48f4-84d9-394ad3d1b5bf" />
</p>

\*Read this in other languages: [English](README.md), [한국어](README.ko.md)

This is a simple example of a 12-factor ExpressJS application. It's built using the ExpressJS framework.
This application is built using the [express-generator](https://expressjs.com/en/starter/generator.html)
and exposes 3 endpoints:

- /health
- /fibonacci/:number (requires postgresql database)
- /keys

## 📝 Prerequisites

- [NodeJS & NPM](https://nodejs.org/en/download)

## 🏃 How to run it locally?

1. Change the working directory

```
cd expressjs-hello-world/app
```

2. Install dependencies

```
npm install
```

3. Run the server

```
npm start
```

4. Test the endpoints using the following curl commands

```
curl http://localhost:3000/health
curl http://localhost:3000/fibonacci/9
```

5. Congratulations! You've finished exploring the ExpressJS Hello World project!

## Next steps

Let's start packaging! Check out the [next branch](https://github.com/canonical/paas-charm-workshop/tree/expressjs-01-rock) `git checkout expressjs-01-rock`
